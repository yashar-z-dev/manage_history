import argparse
import os
from app.utils import parse_line_range

def get_args():
    parser = argparse.ArgumentParser(description="Clean shell history with filters and confirmation.")
    parser.add_argument("-k", "--keyword", help="Keyword to remove from history")
    parser.add_argument("-l", "--lines", help="Line range to remove (e.g., 12-15)")
    parser.add_argument("-r", "--regex", help="Regex pattern to remove matching lines")
    parser.add_argument("-e", "--exclude", help="Exclude lines that contain this string")
    parser.add_argument("--backup-dir", default="~/all-history", help="Directory to save backup files")
    parser.add_argument("-s", "--sort", action="store_true", help="Sort and clean input file")
    parser.add_argument("-i", "--input", help="Custom input file for sorting or filtering")
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')

    args = parser.parse_args()

    # Expand ~ to full home path
    args.backup_dir = os.path.expanduser(args.backup_dir)

    # Create backup directory if it doesn't exist
    if not os.path.exists(args.backup_dir):
        os.makedirs(args.backup_dir, exist_ok=True)
        print(f"[INFO] Created backup directory: {args.backup_dir}")

    # Parse line range
    args.line_numbers = parse_line_range(args.lines)

    if args.debug:
        print("[DEBUG] Line range parsed:", args.line_numbers)
        print("[DEBUG] Backup directory:", args.backup_dir)

    return args
