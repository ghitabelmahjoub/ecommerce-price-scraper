# E-commerce Price Web Scraper

Python web scraper that collects product prices from e-commerce websites and analyzes price trends over time. This project scrapes book titles and prices from a website and saves the data to CSV files. It also includes a script to preview and analyze the scraped data.

## How to Run

1. Make sure you have Python installed (version 3.6 or above).

2. Install the required Python packages by running this command in your terminal:  
pip install requests beautifulsoup4 pandas

css
Copier
Modifier

3. Run the scraper script to collect data:  
python scraper.py

css
Copier
Modifier

4. Run the data preview script to see a summary of the scraped data:  
python preview_data.py

markdown
Copier
Modifier

## Files

- `scraper.py` - The main web scraper that collects book data.  
- `preview_data.py` - Script to load the CSV and print a preview and stats.  
- `books_prices_multi.csv` - CSV file containing scraped data (optional, if included).

## Dependencies

- requests  
- beautifulsoup4  
- pandas

## License

This project is open source and free to use.
