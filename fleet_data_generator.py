import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

--- FleetHealth-AI: Predictive Maintenance Data Simulator ---
def generate_fleet_data(vehicles=5, readings=20):
data = []
start_date = datetime.now()

if name == "main":
fleet_df = generate_fleet_data()
fleet_df.to_csv('fleet_telematics_sample.csv', index=False)
print("Success! Data created.")
