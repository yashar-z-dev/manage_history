from parser import get_args
from controller import run

def main():
    args = get_args()
    if args.debug:
        print("[DEBUG] Parsed arguments:", vars(args))
    run(args, debug=args.debug)

if __name__ == "__main__":
    main()
