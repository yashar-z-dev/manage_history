import sys
from app.shell import detect_shell
from app.backup import find_backup_filename
from app.processor import process_history, sort_and_clean_lines

def run(args, debug=False):
    if debug:
        print("[DEBUG] Starting run()")
        print(f"[DEBUG] Arguments received: {vars(args)}")

    # Sorting mode
    if args.sort:
        if not args.input:
            print("❌ '--input' must be specified for sorting.")
            return
        if debug:
            print(f"[DEBUG] Sorting file: {args.input}")
        sorted_lines = sort_and_clean_lines(input_path=args.input, debug=debug)
        print("\n✅ Sorted output:")
        for line in sorted_lines:
            print(line)
        return

    # Detect shell history file
    shell, history_path = detect_shell()
    if debug:
        print(f"[DEBUG] Detected shell: {shell}")
        print(f"[DEBUG] Default history path: {history_path}")

    if args.input:
        history_path = args.input
        if debug:
            print(f"[DEBUG] Overriding history path with input: {history_path}")
    elif not history_path:
        print("❌ No input file specified.")
        return

    try:
        with open(history_path, "rb") as f:
            raw_lines = f.readlines()
        if debug:
            print(f"[DEBUG] Read {len(raw_lines)} raw lines from history file.")
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return

    # Exclude-only mode
    if args.exclude and not any([args.keyword, args.regex]):
        if debug:
            print("[DEBUG] Running in exclude-only mode.")
        for idx, raw_line in enumerate(raw_lines, start=1):
            try:
                line = raw_line.decode("utf-8")
                if args.exclude in line:
                    print(f"{idx}: {line.strip()}")
            except UnicodeDecodeError:
                continue
        return

    # Default or mixed mode
    decoded_lines, lines_to_delete = process_history(raw_lines, args, debug=debug)

    if not lines_to_delete:
        print("ℹ️ No lines matched for deletion.")
        return

    print("\n⚠️ Lines marked for deletion:")
    for idx, line in lines_to_delete:
        print(f"{idx}: {line.strip()}")

    confirm = input("\n❓ Confirm deletion? (y/n): ").strip().lower()
    if confirm != "y":
        print("❌ Operation cancelled.")
        return

    backup_file = find_backup_filename(args.backup_dir)
    if debug:
        print(f"[DEBUG] Backup file path: {backup_file}")

    with open(backup_file, "w", encoding="utf-8") as f:
        f.writelines(decoded_lines + [line for _, line in lines_to_delete])
    print(f"✅ Backup saved: {backup_file}")

    with open(history_path, "w", encoding="utf-8") as f:
        f.writelines(decoded_lines)

    print(f"\n✅ {len(lines_to_delete)} lines deleted.")
