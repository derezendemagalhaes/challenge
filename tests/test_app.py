""" Test the Flask api endpoints. """
import os
import pandas as pd
import pytest
import tempfile
from faker import Faker
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
    fake_ride_data = create_fake_ride_data()

    with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.csv') as temp_file:
        fake_ride_data.to_csv(temp_file.name, index=False)
        ride_data_app = BusRideAnalyzer(ride_data_path=temp_file.name)
        ride_data_app.load_dataset()

    chosen_country = fake_ride_data.from_country[0]
    response = ride_data_app.app.test_client().get(f'/{chosen_country}')

    data = response.get_json()
    expected_avg_duration = round(ride_data_app.avg_duration_per_country[chosen_country])
    
    assert data is not None, "Response data is None"
    assert 'average_duration' in data
    assert data['average_duration'] == expected_avg_duration
    os.remove(temp_file.name)


def test_invalid_country_code():
    fake_ride_data = create_fake_ride_data()

    with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.csv') as temp_file:
        fake_ride_data.to_csv(temp_file.name, index=False)

        ride_data_app = BusRideAnalyzer(ride_data_path=temp_file.name)
        ride_data_app.load_dataset()  # New line to process dataset

    chosen_country = fake.country_code(representation='alpha-2')
    while chosen_country in fake_ride_data['from_country'].values:
        chosen_country = fake.country_code(representation='alpha-2')

    response = ride_data_app.app.test_client().get(f'/{chosen_country}')
    data = response.get_json()

    assert data is not None, "Response data is None"
    assert 'error' in data
    assert data['error'] == f"No data available for '{chosen_country}'"
    os.remove(temp_file.name)
