import re

def parse_line_range(line_range, debug=False):
    if not line_range:
        if debug:
            print("[DEBUG] No line range provided.")
        return set()

    match = re.match(r"(\d+)-(\d+)", line_range)
    if match:
        start, end = int(match.group(1)), int(match.group(2))
        if debug:
            print(f"[DEBUG] Parsed line range: {start} to {end}")
        return set(range(start, end + 1))

    print("❌ Invalid line range format. Use format like: 12-15")
    return set()
