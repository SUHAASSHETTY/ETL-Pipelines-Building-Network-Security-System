# ETL Pipeline setup 
# Dataset(csv) -> Json -> MongoDB

import os
import sys
import json
import pandas as pd
import pymongo
import certifi
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
MONGO_DB_URL = os.getenv("MONGO_DB_URL")

if not MONGO_DB_URL:
    raise Exception("❌ MongoDB URI not found. Make sure .env file has MONGO_DB_URL set.")

# CSV → JSON converter
def csv_to_json(file_path):
    try:
        data = pd.read_csv(file_path)
        data.reset_index(drop=True, inplace=True)
        records = list(json.loads(data.T.to_json()).values())
        return records
    except Exception as e:
        print("❌ Error converting CSV to JSON:", e)
        sys.exit(1)

# Insert into MongoDB
def insert_data(records, database, collection):
    try:
        client = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=certifi.where())
        db = client[database]
        coll = db[collection]

        result = coll.insert_many(records)
        return len(result.inserted_ids)
    except Exception as e:
        print("❌ Error inserting into MongoDB:", e)
        sys.exit(1)

if __name__ == "__main__":
    FILE_PATH = "Network_Data/phisingData.csv"   # update if your file is elsewhere
    DATABASE = "SUHAASAI"                        # your DB name
    COLLECTION = "NetworkData"                   # your collection name

    print("📂 Reading CSV and converting to JSON...")
    records = csv_to_json(FILE_PATH)

    print(f"📥 Converted {len(records)} records. Inserting into MongoDB Atlas...")
    inserted_count = insert_data(records, DATABASE, COLLECTION)

    print(f"✅ Successfully inserted {inserted_count} records into {DATABASE}.{COLLECTION}")
