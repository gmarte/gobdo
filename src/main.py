# main.py
from googlesearch import search
from database import Database
from urllib.parse import urlparse


def main():
    # Create an instance of our Database class
    db = Database()

    # Connect to the database
    db.connect()

    # Query the websites
    query = "*.gob.do"

    for url in search(query, num_results=100):
        # Parse the URL to get the institution name
        # Parse the URL and get the network location part
        netloc = urlparse(url).netloc

        # Now split by '.' and the first element will be just 'datos' if the URL does not start with 'www.'
        # If the URL starts with 'www.', remove 'www.' before splitting
        name = netloc.replace('www.', '').split('.')[0]
        # Insert into the table
        db.insert_institution(name, url)

    # Close the database connection
    db.close()


if __name__ == "__main__":
    main()
