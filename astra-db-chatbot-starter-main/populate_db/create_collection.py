import os
import sys

from dotenv import load_dotenv

from astrapy.db import AstraDB

load_dotenv()

# Grab the Astra token and api endpoint from the environment
token = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
api_endpoint = os.getenv("ASTRA_DB_API_ENDPOINT")
namespace = os.getenv("ASTRA_DB_NAMESPACE")
collection_name = os.getenv("ASTRA_DB_COLLECTION")
dimension = os.getenv("VECTOR_DIMENSION")

# check that dimension is defined and is an integer
if dimension == None:
    print("environment variable 'VECTOR_DIMENSION' not defined")
    sys.exit()
else:
    if not dimension.isdigit():
        print("environment variable 'VECTOR_DIMENSION' not integer")
        sys.exit()

# check that namespace is defined
if not namespace:
    astra_db = AstraDB(token=token, api_endpoint=api_endpoint)
else:
    astra_db = AstraDB(token=token, api_endpoint=api_endpoint, namespace=namespace)

# create collection if it doesn't exist
if collection_name in astra_db.get_collections()['status']['collections']:
    print(f"Collection '{collection_name}' already exists. New collection not created")
else:
    try:
        # Attempt to create the collection
        astra_db.create_collection(collection_name=collection_name, dimension=dimension)
        print(f"Collection '{collection_name}' created with dimension {dimension}.")
    except Exception as e:
        print(f"Collection Name: {collection_name}")
        print(f"Dimension: {dimension}")
        print(f"An error occurred: {e}")
