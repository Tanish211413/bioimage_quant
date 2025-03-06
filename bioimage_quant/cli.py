import argparse

def cli():
    parser = argparse.ArgumentParser(description="GelQuant CLI")
    parser.add_argument('test', nargs='?', help="Test argument (optional)")

    try:
        args = parser.parse_args()
        print(args.test if args.test else "No argument provided")
    except SystemExit:
        print("Usage: gelquant <test_argument>")

if __name__ == "__main__":
    cli()

