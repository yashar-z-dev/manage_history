import os
import re

def find_backup_filename(directory, ext=".txt", digits=3, debug=False):
    # Ensure the backup directory exists
    os.makedirs(directory, exist_ok=True)
    if debug:
        print(f"[DEBUG] Ensuring backup directory exists: {directory}")

    # List existing files with the specified extension
    existing_files = [f for f in os.listdir(directory) if f.endswith(ext)]
    numbers = []
    for f in existing_files:
        # Extract numeric part from filename
        match = re.match(r"(\d+)" + re.escape(ext) + r"$", f)
        if match:
            numbers.append(int(match.group(1)))

    # Determine the next available number
    next_number = max(numbers, default=0) + 1
    filename = os.path.join(directory, f"{str(next_number).zfill(digits)}{ext}")
    if debug:
        print(f"[DEBUG] Backup filename selected: {filename}")
    return filename
