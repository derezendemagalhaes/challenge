"""
File that contains a Flask web application for analyzing bus ride data.
"""
import pandas as pd
from cloudpathlib import AnyPath
from flask import Flask, render_template, jsonify

class BusRideAnalyzer:
    """
    Class for analyzing bus ride data using a Flask web application.
    """

    def __init__(self, ride_data_path=None):
        """
        Initializes the BusRideAnalyzer.

        Parameters:
        - ride_data_path (str): Path to the CSV file containing ride data.
        """
        self.initialize(ride_data_path)

    def initialize(self, ride_data_path):
        """
        Initializes the Flask app and loads the dataset.

        Parameters:
        - ride_data_path (str): Path to the CSV file containing ride data.
        """
        self.app = Flask(__name__)
        self.ride_data_path = ride_data_path

        if self.ride_data_path is not None:
            self.load_dataset()
    
        self.create_routes()

    def load_dataset(self):
        """
        Loads the dataset from the specified CSV file path.
        """
        self.dataset_path = AnyPath(self.ride_data_path)
        self.dataset = pd.read_csv(self.dataset_path)

    def create_routes(self):
        """
        Defines Flask routes for the web application.
        """
        @self.app.route('/')
        def index():
            """
            Renders the index.html template.

            Returns:
            - rendered HTML template
            """
            return render_template('index.html')

        @self.app.route('/<string:country>')
        def average_duration(country):
            """
            Calculates and returns the average duration of bus rides for a given country.

            Parameters:
            - country (str): The country for which to calculate the average duration.

            Returns:
            - JSON response with the average duration or an error message.
            """
            try:
                country_data = self.dataset[self.dataset['from_country'] == country]

                if country_data.empty:
                    raise Exception(f"No data available for '{country}'")

                avg_duration = round(country_data['duration'].mean())
                return jsonify({'average_duration': avg_duration})

            except Exception as e:
                return jsonify({'error': str(e)}), 404

    def run(self):
        """
        Runs the Flask web application.
        """
        self.app.run(debug=True)
