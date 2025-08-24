import os

def find_backup_filename(directory, ext=".txt", debug=False):
    i = 1
    os.makedirs(directory, exist_ok=True)
    if debug:
        print(f"[DEBUG] Ensuring backup directory exists: {directory}")

    while True:
        filename = os.path.join(directory, f"{i}{ext}")
        if debug:
            print(f"[DEBUG] Checking if file exists: {filename}")
        if not os.path.exists(filename):
            if debug:
                print(f"[DEBUG] Backup filename selected: {filename}")
            return filename
        i += 1
