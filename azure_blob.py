from sqlite3.dbapi2 import Timestamp
from azure.storage.blob import BlobServiceClient
import json
from dotenv import load_dotenv
import os
load_dotenv()

connection_string=os.getenv("AZURE_CONNECTION_STRING")
CONTAINER_NAME = os.getenv("container")
def upload_weather_to_blob(city, weather_data):
    print("📤 Starting upload to Azure Blob...")

    try:
        if not connection_string: 
            print("❌ Connection string is missing from environment variables.")
            return

        container_name = os.getenv("container") 
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)

        blob_name = f"{city.lower()}_{Timestamp}.json"
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

        blob_client.upload_blob(json.dumps(weather_data), overwrite=True)
        print(f"✅ Successfully uploaded {blob_name} to {container_name}")

    except Exception as e:
        print(f"❌ Failed to upload to blob: {e}")

