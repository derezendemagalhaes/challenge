from flask import Flask, render_template, jsonify
import pandas as pd
from cloudpathlib import AnyPath
from args import argument_parser  

app = Flask(__name__)

# Parse command line arguments
args = argument_parser().parse_args()

# Use the value of ride-data-path from the command line arguments
ride_data_path = args.ride_data_path

if ride_data_path is None:
    raise ValueError("Please provide the path to the ride data file using --ride-data-path")

# Load the dataset from the specified path using AnyPath
dataset_path = AnyPath(ride_data_path)
dataset = pd.read_csv(dataset_path)

# Create a route for the index page
@app.route('/')
def index():
    return render_template('index.html')

# Create a route for the API endpoint
@app.route('/<country>')
def average_duration(country):
    try:
        # Filter dataset for the given country
        country_data = dataset[dataset['from_country'] == country]

        # Check if there is data for the given country
        if country_data.empty:
            raise Exception(f"No data available for '{country}'")

        # Calculate average duration in seconds and round to the nearest integer
        avg_duration = round(country_data['duration'].mean())
        return jsonify({'average_duration': avg_duration})

    except Exception as e:
        return jsonify({'error': str(e)}), 404

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
