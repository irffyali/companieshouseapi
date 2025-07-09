import requests
import pandas as pd

# Define the endpoint and parameters
url = "http://localhost:8000/date_range/"
params = {
    "start_date": "2024-01-01",
    "end_date": "2025-01-01"
}

# Send request
response = requests.get(url, params=params)

# Convert response to DataFrame
if response.ok:
    data = response.json()
    data = pd.DataFrame(data)
    print(df)
else:
    print(f"❌ Error {response.status_code}: {response.text}")