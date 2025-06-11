from sqlite3.dbapi2 import Timestamp
from azure.storage.blob import BlobServiceClient
import json
import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

AZURE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=imgresizerr;AccountKey=clG44PbwxK6iHgcOCXKxTVaTfv3HIXhX3YT08xCm3RZOQj7TIQG1mDPDr9UZFltTWf9YHwFTMr+g+AStcYh/8g==;EndpointSuffix=core.windows.net"
CONTAINER_NAME = "weather-data"
def upload_weather_to_blob(city, weather_data):
    print("📤 Starting upload to Azure Blob...")

    try:
        if not AZURE_CONNECTION_STRING: 
            print("❌ Connection string is missing from environment variables.")
            return

        container_name = "weather-data" 
        blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)

        blob_name = f"{city.lower()}_{Timestamp}.json"
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

        blob_client.upload_blob(json.dumps(weather_data), overwrite=True)
        print(f"✅ Successfully uploaded {blob_name} to {container_name}")

    except Exception as e:
        print(f"❌ Failed to upload to blob: {e}")

