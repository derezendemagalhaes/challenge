import argparse

def argument_parser() -> argparse.ArgumentParser:
    """
    Create an ArgumentParser object with predefined command line arguments.

    Returns:
    argparse.ArgumentParser: The ArgumentParser object with predefined arguments.
    """
    parser = argparse.ArgumentParser(
        description="API implementing the calculation of the average ride duration in seconds per country."
    )

    parser.add_argument(
        "--ride-data-path",
        type=str,
        required=True,
        help="Path to a ride data file.",
    )
    
    return parser
