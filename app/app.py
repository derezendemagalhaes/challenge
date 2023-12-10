"""
File that contains a Flask web application for analyzing bus ride data.
"""
import pandas as pd
from cloudpathlib import AnyPath
from flask import Flask, render_template, jsonify
from typing import Optional
from werkzeug.wrappers import Response

class BusRideAnalyzer:
    """
    Class for analyzing bus ride data using a Flask web application.
    """

    def __init__(self: 'BusRideAnalyzer', ride_data_path: Optional[str] = None) -> None:
        """
        Initializes the BusRideAnalyzer.

        Parameters:
        - ride_data_path (str): Path to the CSV file containing ride data.
        """
        self.initialize(ride_data_path)

    def initialize(self: 'BusRideAnalyzer', ride_data_path: Optional[str]) -> None:
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

    def load_dataset(self: 'BusRideAnalyzer') -> None:
        """
        Loads the dataset from the specified CSV file path.
        """
        self.dataset_path = AnyPath(self.ride_data_path)
        self.dataset = pd.read_csv(self.dataset_path)

    def create_routes(self: 'BusRideAnalyzer') -> None:
        """
        Defines Flask routes for the web application.
        """
        @self.app.route('/')
        def index() -> 'Response':
            """
            Renders the index.html template.

            Returns:
            - rendered HTML template
            """
            return render_template('index.html')

        @self.app.route('/<string:country>')
        def average_duration(country: str) -> 'Response':
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
                    return jsonify({"error": f"No data available for '{country}'"}), 404

                avg_duration = round(country_data['duration'].mean())
                return jsonify({'average_duration': avg_duration})

            except Exception as e:
                return jsonify({"error": str(e)}), 500

    def run(self: 'BusRideAnalyzer') -> None:
        """
        Runs the Flask web application.
        """
        self.app.run(host='0.0.0.0', port=5000, debug=False)
