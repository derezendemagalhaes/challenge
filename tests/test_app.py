# test_app.py
import pytest
from faker import Faker
from cloudpathlib import AnyPath
import pandas as pd
from app.app import BusRideAnalyzer

fake = Faker()

def create_fake_ride_data(num_records=20):
    fake_data = {
        'id': [fake.uuid4() for _ in range(num_records)],
        'departure_timestamp': [fake.date_time_this_decade().timestamp() for _ in range(num_records)],
        'arrival_timestamp': [fake.date_time_this_decade().timestamp() for _ in range(num_records)],
        'duration': [fake.random_int(min=600, max=3600) for _ in range(num_records)],
        'from_id': [fake.uuid4() for _ in range(num_records)],
        'to_id': [fake.uuid4() for _ in range(num_records)],
        'from_country': [fake.country_code(representation='alpha-2') for _ in range(num_records)],
        'to_country': [fake.country_code(representation='alpha-2') for _ in range(num_records)],
    }
    return pd.DataFrame(fake_data)

def test_valid_country_code():
    # Create an instance of BusRideAnalyzer with fake ride data
    fake_ride_data = create_fake_ride_data()
    ride_data_app = BusRideAnalyzer(ride_data_path=None)
    ride_data_app.dataset = fake_ride_data
    chosen_country = fake_ride_data.from_country[0]

    # Simulate a request to the Flask app
    response = ride_data_app.app.test_client().get(f'/{chosen_country}')
    
    # Calculate the actual average duration for the chosen country
    country_data = ride_data_app.dataset[ride_data_app.dataset['from_country'] == chosen_country]
    actual_avg_duration = round(country_data['duration'].mean())

    # Assert the response based on the fake ride data
    data = response.get_json()
    assert data is not None, "Response data is None"
    assert 'average_duration' in data
    assert data['average_duration'] == actual_avg_duration

def test_invalid_country_code():
    # Create an instance of BusRideAnalyzer with fake ride data
    fake_ride_data = create_fake_ride_data()
    ride_data_app = BusRideAnalyzer(ride_data_path=None)
    ride_data_app.dataset = fake_ride_data
    chosen_country = fake.country_code(representation='alpha-2')

    # Simulate a request to the Flask app
    response = ride_data_app.app.test_client().get(f'/{chosen_country}')

    # Assert the response based on the fake ride data
    data = response.get_json()
    assert data is not None, "Response data is None"
    assert 'error' in data
    assert data['error'] == f"No data available for '{chosen_country}'"
