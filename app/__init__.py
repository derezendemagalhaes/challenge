from flask import Flask

app = Flask(__name__)

# Import the API routes
from app import app
