import argparse

def argument_parser() -> argparse.ArgumentParser:
    # Define command line inputs.
    parser = argparse.ArgumentParser(description=".")

    parser.add_argument(
        "--ride-data-path",
        type=str,
        default=None,
        help="Path to a ride data file.",
    )
    
    return parser
