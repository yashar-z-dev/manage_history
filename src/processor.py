import re

def process_history(raw_lines, args, debug=False):
    decoded_lines = []
    lines_to_delete = []
    line_numbers_to_remove = args.line_numbers
    regex_pattern = re.compile(args.regex) if args.regex else None

    if debug:
        print("[DEBUG] Starting process_history()")
        print(f"[DEBUG] Total raw lines: {len(raw_lines)}")
        print(f"[DEBUG] Keyword: {args.keyword}, Regex: {args.regex}, Exclude: {args.exclude}")
        print(f"[DEBUG] Line numbers to remove: {line_numbers_to_remove}")

    for idx, raw_line in enumerate(raw_lines, start=1):
        try:
            line = raw_line.decode("utf-8")
        except UnicodeDecodeError:
            line = raw_line.decode("utf-8", errors="replace")
            lines_to_delete.append((idx, line))
            if debug:
                print(f"[DEBUG] Line {idx} had decoding error and was marked for deletion.")
            continue

        remove = False

        if args.keyword and args.keyword in line:
            if args.exclude and args.exclude in line:
                if debug:
                    print(f"[DEBUG] Line {idx} contains keyword but also exclude string. Skipped.")
                continue
            remove = True
            if debug:
                print(f"[DEBUG] Line {idx} matched keyword.")

        if idx in line_numbers_to_remove:
            remove = True
            if debug:
                print(f"[DEBUG] Line {idx} matched line number filter.")

        if regex_pattern and regex_pattern.search(line):
            if args.exclude and args.exclude in line:
                if debug:
                    print(f"[DEBUG] Line {idx} matched regex but also exclude string. Skipped.")
                continue
            remove = True
            if debug:
                print(f"[DEBUG] Line {idx} matched regex.")

        if remove:
            lines_to_delete.append((idx, line))
        else:
            decoded_lines.append(line)

    if debug:
        print(f"[DEBUG] Lines to delete: {len(lines_to_delete)}")
        print(f"[DEBUG] Lines to keep: {len(decoded_lines)}")

    return decoded_lines, lines_to_delete


def sort_and_clean_lines(input_path=None, input_stream=None, debug=False):
    seen = set()
    result = []

    if debug:
        print("[DEBUG] Starting sort_and_clean_lines()")

    # Select input source
    if input_path:
        if debug:
            print(f"[DEBUG] Reading from input file: {input_path}")
        with open(input_path, encoding="utf-8") as f:
            lines = f.readlines()
    elif input_stream:
        if debug:
            print("[DEBUG] Reading from input stream")
        lines = input_stream
    else:
        raise ValueError("❌ No input source provided.")

    for idx, raw_line in enumerate(lines, start=1):
        try:
            line = raw_line.strip()
            cleaned = re.sub(r'^\d+\s+', '', line)
            if cleaned and cleaned not in seen:
                seen.add(cleaned)
                result.append(cleaned)
                if debug:
                    print(f"[DEBUG] Line {idx} added: {cleaned}")
        except UnicodeDecodeError:
            if debug:
                print(f"[DEBUG] Line {idx} had decoding error. Skipped.")
            continue

    sorted_lines = [f"{i} {line}" for i, line in enumerate(result, start=1)]

    if debug:
        print(f"[DEBUG] Total unique cleaned lines: {len(sorted_lines)}")

    return sorted_lines
