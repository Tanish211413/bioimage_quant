import argparse

def cli():
    parser = argparse.ArgumentParser(description="GelQuant CLI")
    parser.add_argument('test', nargs='?', help="Test argument (optional)", default="No argument provided")

    args = parser.parse_args()
    print(args.test)

if __name__ == "__main__":
    cli()


