import argparse
from createMig import png_to_mig
from viewMig import view_image

def main():
    parser = argparse.ArgumentParser(description="Convert PNG to MIG or view MIG image.")
    parser.add_argument("action", choices=["convert", "view"], help="Action to perform: 'convert' or 'view'")
    parser.add_argument("input", help="Input file: PNG file to convert or MIG file to view")
    parser.add_argument("--output", help="Output file (only for conversion)")
    args = parser.parse_args()

    if args.action == "convert":
        if not args.output:
            parser.error("--output is required for 'convert' action")
        png_to_mig(args.input, args.output)
    elif args.action == "view":
        view_image(args.input)

if __name__ == "__main__":
    main()
