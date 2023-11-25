# import libraries
import pymongo
import json
import pandas as pd
from urllib.parse import quote_plus
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import sys

def get_secrets():
    with open('secrets.json') as secrets_file:
        secrets = json.load(secrets_file)

    return secrets

secrets = get_secrets()


def connect_to_mongodb():
    # Escape username and password
    escaped_username = quote_plus(secrets.get("USERNAME"))
    escaped_password = quote_plus(secrets.get("PASSWORD"))
    cluster_url = secrets.get("CLUSTER_URL")

    # Build MongoDB URI
    mongo_uri = f"mongodb+srv://{escaped_username}:{escaped_password}@{cluster_url}/?retryWrites=true&w=majority"

    try:
        # Create a new client and connect to the server
        client = MongoClient(mongo_uri, server_api=ServerApi('1'))

        # Send a ping to confirm a successful connection
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")

        return client, client[secrets.get("DATABASE_NAME")][secrets.get("COLLECTION_NAME")]

    except pymongo.errors.ConfigurationError:
        print("An Invalid URI host error was received. Is your Atlas host name correct in your connection string?")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred during MongoDB connection: {e}")
        sys.exit(1)

# Connect to MongoDB
client, my_collection = connect_to_mongodb()


# Find all documents in the collection
cursor = my_collection.find()

# Convert cursor to list of dictionaries
documents = list(cursor)

# Check if documents are found
if not documents:
    print("No documents found.")
else:
    # Create a DataFrame
    df = pd.DataFrame(documents)

    # Display the DataFrame
    print(df.tail())