from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

# Load the dataset
dataset = pd.read_csv('ride-data.csv')

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
