import os
import requests
from googlesearch import search
import shutil
from datetime import datetime

def download_file(url, save_path):
    """ Download file from a given URL and save it to the specified path. """
    try:
        response = requests.get(url, stream=True, timeout=10)  # Added timeout for safety
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                response.raw.decode_content = True
                shutil.copyfileobj(response.raw, f)
            return True
    except requests.RequestException as e:
        print(f"Error downloading file: {e}")
    return False

def perform_search(query):
    """ Perform a Google search and return the URL of the first result. """
    results = search(query, num_results=1)
    return results

def find_and_download_files(year, month, institution_url, base_dir):
    file_types = ['xlsx', 'pdf']
    for file_type in file_types:
        query = f'"nomina" OR "recursos humanos" and "{month}" AND "{year}" site:{institution_url} filetype:{file_type}'
        url = perform_search(query)
        if url:
            directory = os.path.join(base_dir, str(year), month)
            os.makedirs(directory, exist_ok=True)
            filename = f"{year}-{month}.{file_type}"
            save_path = os.path.join(directory, filename)
            if download_file(url, save_path):
                print(f"Downloaded: {save_path}")
                return  # Stop after successful download
        else:
            print(f"No files found for {month} {year} with filetype {file_type}.")

if __name__ == "__main__":
    year = input("Enter the year: ")
    month = input("Enter the month (e.g., Enero, Febrero, etc.): ")
    institution_url = input("Enter the institution website URL: ")
    base_directory = input("Enter the base directory to save files (e.g., C:/Documents/Payrolls): ")
    find_and_download_files(year, month, institution_url, base_directory)
