# Sigan Viendo

"Sigan Viendo" is a web scraping application designed to gather and analyze information from Dominican Republic government websites.

## Overview

This application is designed to:

- Search for all `*.gob.do` domains which represent Dominican Republic government institutions.
- Collect specific data from these websites, specifically the ID (cédula), position, and salary of public employees.
- Identify employees who work in multiple government institutions.

## Installation

1. Clone this repository: `git clone https://github.com/gmarte/gobdo.git`
2. Change into the directory: `cd gobdo`
3. Install the required Python packages: `pip install -r requirements.txt`
4. Set up the PostgreSQL database by following the instructions in `config.py`.
5. Run the application: `python src/main.py`

## Usage

To start the web scraping process, run the `main.py` script located in the `src` directory:


This will start the web scraping process and the collected data will be stored in the PostgreSQL database configured in `config.py`.

## File Structure

The application is structured as follows:

- `src/`: Contains the Python scripts for the application.
  - `main.py`: Entry point for the application.
  - `web_scraper.py`: Contains the logic for web scraping.
  - `database.py`: Contains the logic for interacting with the database.
- `config.py`: Contains the configuration for the database.
- `requirements.txt`: Contains the Python packages required for this application.

## Contributing

If you want to contribute to this project, please fork the repository, make your changes, and open a Pull Request.

## License

This project is licensed under the MIT License. See `LICENSE` for more details.


