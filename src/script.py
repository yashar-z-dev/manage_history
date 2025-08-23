import argparse
import os
import re
import subprocess

def find_backup_filename(directory, ext=".txt"):
    i = 1
    os.makedirs(directory, exist_ok=True)
    while True:
        filename = os.path.join(directory, f"{i}{ext}")
        if not os.path.exists(filename):
            return filename
        i += 1

def parse_line_range(line_range):
    if not line_range:
        return set()
    match = re.match(r"(\d+)-(\d+)", line_range)
    if match:
        start, end = int(match.group(1)), int(match.group(2))
        return set(range(start, end + 1))
    else:
        print("❌ Invalid line range format. Use like: 12-15")
        return set()

def detect_shell():
    shell_path = os.environ.get("SHELL", "")
    shell_name = os.path.basename(shell_path)
    if shell_name == "zsh":
        return "zsh", os.path.expanduser("~/.zsh_history")
    elif shell_name == "bash":
        return "bash", os.path.expanduser("~/.bash_history")
    else:
        return None, None

def main():
    parser = argparse.ArgumentParser(description="Clean shell history with filters and confirmation.")
    parser.add_argument("-k", "--keyword", help="Keyword to remove from history")
    parser.add_argument("-l", "--lines", help="Line range to remove (e.g., 12-15)")
    parser.add_argument("-r", "--regex", help="Regex pattern to remove matching lines")
    parser.add_argument("-e", "--exclude", help="Exclude lines that contain this string")
    parser.add_argument("--backup-dir", default=os.path.expanduser("~/all-history"), help="Directory to save backup files")
    args = parser.parse_args()

    shell, history_path = detect_shell()
    if not shell or not history_path:
        print("❌ Unsupported or undetected shell. Only Bash and Zsh are supported.")
        return

    backup_file = find_backup_filename(args.backup_dir)
    line_numbers_to_remove = parse_line_range(args.lines)
    regex_pattern = re.compile(args.regex) if args.regex else None

    try:
        with open(history_path, "rb") as f:
            raw_lines = f.readlines()
    except Exception as e:
        print(f"❌ Failed to read history file: {e}")
        return

    decoded_lines = []
    lines_to_delete = []

    for idx, raw_line in enumerate(raw_lines, start=1):
        try:
            line = raw_line.decode("utf-8")
        except UnicodeDecodeError:
            line = raw_line.decode("utf-8", errors="replace")
            print(f"❌ Corrupted line at {idx}: {raw_line}")
            lines_to_delete.append((idx, line))
            continue

        remove = False

        if args.keyword and args.keyword in line:
            if args.exclude and args.exclude in line:
                continue
            remove = True

        if idx in line_numbers_to_remove:
            remove = True

        if regex_pattern and regex_pattern.search(line):
            if args.exclude and args.exclude in line:
                continue
            remove = True

        if remove:
            lines_to_delete.append((idx, line))
        else:
            decoded_lines.append(line)

    if not lines_to_delete:
        print("ℹ️ No matching lines found. Nothing to delete.")
        return

    print("\n⚠️ Lines marked for deletion:")
    for idx, line in lines_to_delete:
        print(f"{idx}: {line.strip()}")

    confirm = input("\n❓ Confirm deletion? (y/n): ").strip().lower()
    if confirm != "y":
        print("❌ Operation cancelled. No changes made.")
        return

    try:
        with open(backup_file, "w", encoding="utf-8") as f:
            f.writelines(decoded_lines + [line for _, line in lines_to_delete])
        print(f"✅ Backup saved to: {backup_file}")

        with open(history_path, "w", encoding="utf-8") as f:
            f.writelines(decoded_lines)

        if shell == "zsh":
            subprocess.run(["zsh", "-c", f"HISTFILE={history_path}; fc -R"], check=True)
        elif shell == "bash":
            subprocess.run(["bash", "-c", f"HISTFILE={history_path}; history -r"], check=True)

        print(f"\n✅ Removed {len(lines_to_delete)} lines from history")
        print("✅ History reloaded")
    except Exception as e:
        print(f"❌ Failed to update history: {e}")

if __name__ == "__main__":
    main()
