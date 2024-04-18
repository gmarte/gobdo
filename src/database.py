import pymongo
from config import MONGODB
import logging

class Database:
    def __init__(self):
        self.client = None
        self.db = None
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

    def connect(self):
        try:
            self.client = pymongo.MongoClient(MONGODB['url'])
            self.db = self.client[MONGODB['db']]  # specify your database name here
            self.logger.info('Successfully connected to the database')
        except Exception as e:
            self.logger.error(f"Failed to connect to the database: {e}")
            raise
    def get_all_institutions(self):
        try:
            institutions_collection = self.db['institutions']
            institutions = list(institutions_collection.find({}))  # Retrieve all documents in the 'institutions' collection
            self.logger.info(f"Retrieved {len(institutions)} institutions.")
            return institutions
        except Exception as e:
            self.logger.error(f"Failed to retrieve institutions: {e}")
            return []  # Return an empty list in case of an error
    def insert_institution(self, institution):
        try:
            institutions_collection = self.db['institutions']
            result = institutions_collection.insert_one(institution)
            self.logger.info(f"Successfully inserted institution with ID: {result.inserted_id}")
        except Exception as e:
            self.logger.error(f"Failed to insert institution: {e}")

    def insert_many_institutions(self, institutions):
        try:
            institutions_collection = self.db['institutions']
            result = institutions_collection.insert_many(institutions)
            self.logger.info(f"Successfully inserted {len(result.inserted_ids)} institutions")
        except Exception as e:
            self.logger.error(f"Failed to insert institutions: {e}")
            raise

    def close(self):
        if self.client is not None:
            self.client.close()
            self.logger.info('Database connection closed')
