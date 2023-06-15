import psycopg2
from psycopg2 import sql
import logging
from config import DATABASE


class Database:
    def __init__(self):
        self.conn = None
        self.cur = None
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                dbname=DATABASE['database'],
                user=DATABASE['user'],
                password=DATABASE['password'],
                host=DATABASE['host'],
                port=DATABASE['port'],
            )
            self.cur = self.conn.cursor()
            self.logger.info('Successfully connected to the database')
        except Exception as e:
            self.logger.error(f"Failed to connect to the database: {e}")
            raise

    def insert_institution(self, name, domain):
        try:
            insert_sql = sql.SQL(
                """
                INSERT INTO institutions (name, domain) 
                VALUES (%s, %s)
                ON CONFLICT (domain) DO NOTHING;
                """
            )
            self.cur.execute(insert_sql, (name, domain))
            self.conn.commit()
            self.logger.info(
                f'Successfully inserted {domain} into the database')
        except Exception as e:
            self.logger.error(
                f"Failed to insert institution into the database: {e}")
            # Optionally, you could rollback the transaction if there's an error
            # self.conn.rollback()

    def close(self):
        if self.conn is not None and self.cur is not None:
            self.cur.close()
            self.conn.close()
            self.logger.info('Database connection closed')
