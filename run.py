import argparse
from app.app import BusRideAnalyzer
from app.args import argument_parser

def parse_arguments():
    """
    Parse command-line arguments using the custom argument parser.

    Returns:
        argparse.Namespace: The parsed command-line arguments.
    """
    parser = argument_parser()
    return parser.parse_args()

if __name__ == '__main__':
    # Parse command-line arguments
    args = parse_arguments()

    # Instantiate BusRideAnalyzer with the provided ride data path
    bus_ride_analyzer = BusRideAnalyzer(ride_data_path=args.ride_data_path)
    
    # Run the Flask application
    bus_ride_analyzer.run()
