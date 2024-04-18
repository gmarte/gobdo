# main.py
from googlesearch import search
from database import Database
from urllib.parse import urlparse
import sys



def main():
    # Create an instance of our Database class
    db = Database()

    # Connect to the database
    db.connect()

    # Print options and get user input
    print("Choose an action by entering the corresponding number:")
    print("1 - Scrape data")
    print("2 - Insert all scraped data")
    print("3 - Update existing data")
    action = input("Enter your choice (1, 2, or 3): ")
    
    if action == '1':
        # 1. List to store all institution data
        # 2. Scrape the websites and store the data in the institutions list
        # 3. For each website in the list of government websites search for payroll files
        # 4. For each payroll file found, extract the data and store it in the institutions list with the employee data
        # 5. Employees should be stored in a list within the institution data
        # 6. Example structure of the institutions list: [{"name": "institution_name", "domain": "institution_domain", "employees": [{"name": "employee_name", cedula;"employee_cedula", position: "employee_position" "salary": "employee_salary"}]}]
        institutions = db.get_all_institutions()
        # print(institutions)
        #for institution in institutions:
            # Scrape the website
            # Search for payroll files
            # Extract employee data
            # Store the employee data in the institution data
            #pass
    elif action == '2':
        # List to store all institution data
        institutions = []

        # Query the websites
        query = "*.gob.do"

        for url in search(query, num_results=100):        
            netloc = urlparse(url).netloc

            name = netloc.replace('www.', '').split('.')[0]        
            institutions.append({"name": name, "domain": url})

        # Close the database connection
        if institutions:
            db.insert_many_institutions(institutions)
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        db.close()
        sys.exit(1)
    db.close()


if __name__ == "__main__":
    main()
