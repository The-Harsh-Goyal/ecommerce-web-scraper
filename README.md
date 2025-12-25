# E-Commerce Web Scraper

A powerful and modular Python-based web scraper designed to extract product data from e-commerce websites. This tool uses BeautifulSoup for web scraping and Streamlit for a user-friendly graphical interface.

## Features

- **Multi-Site Support**: Scrape data from multiple e-commerce websites using standardized CSS selectors
- **Structured Data Extraction**: Extracts product title, price, availability, and other key information
- **CSV Export**: Automatically saves scraped data to CSV files with date-based naming (e.g., `products_20250101.csv`)
- **Error Handling**: Robust error handling for missing selectors, network issues, and parsing errors
- **Polite Scraping**: Includes headers, delays, and user-agent rotation to respect server resources
- **Streamlit UI**: Modern, intuitive web-based interface for non-technical users
- **Modular Architecture**: Separated scraper logic from UI for easy maintenance and testing

## Project Structure

```
ecommerce-web-scraper/
├── scraper.py          # Core scraping logic
├── app.py              # Streamlit UI application
├── requirements.txt    # Python dependencies
├── .gitignore          # Git ignore file
└── README.md           # This file
```

## Requirements

### System Requirements
- **Python**: Version 3.8 or higher
- **OS**: Windows, macOS, or Linux
- **Internet Connection**: Required for scraping

### Python Packages
The following packages are required (automatically installed via requirements.txt):

- **requests** (2.31.0+): HTTP library for making requests
- **beautifulsoup4** (4.12.0+): HTML/XML parsing library
- **streamlit** (1.28.0+): Web application framework
- **pandas** (2.1.0+): Data manipulation and CSV export
- **lxml** (4.9.0+): XML and HTML parsing (optional, enhances BeautifulSoup)

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/Harsh4DS/ecommerce-web-scraper.git
cd ecommerce-web-scraper
```

### Step 2: Create a Virtual Environment (Recommended)

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

If you don't have pip, download it from [python.org](https://www.python.org/downloads/).

## Usage

### Running the Streamlit Application

1. Activate your virtual environment (if not already active)
2. Run the Streamlit app:

```bash
streamlit run app.py
```

3. The application will open in your default web browser at `http://localhost:8501`

### Using the Application

1. **Enter Website URL**: Paste the e-commerce website URL in the input field
2. **Configure Settings** (optional):
   - Request timeout
   - Delay between requests
3. **Start Scraping**: Click the "Scrape Now" button
4. **View Results**: The scraped data displays in a table format
5. **Download CSV**: Click "Download CSV" to save the data locally

### Running the Scraper Directly (Python)

For advanced users, you can import and use the scraper module directly:

```python
from scraper import EcommerceScraper

scraper = EcommerceScraper()
url = "https://www.example-ecommerce.com/products"
products = scraper.scrape(url)

# Data is automatically saved to CSV with timestamp
```

## CSV File Format

Scraped data is automatically saved with the following naming convention:

```
products_YYYYMMDD.csv
```

Example: `products_20250115.csv`

### CSV Columns
- `product_title`: Product name/title
- `product_price`: Product price
- `product_availability`: Product availability status
- `product_url`: Direct link to product
- `scrape_date`: Date when the data was scraped

Null values indicate the selector was unavailable on that website.

## Supported Selectors

The scraper uses standardized CSS selectors that work across multiple e-commerce platforms:

```python
CSS_SELECTORS = {
    'product_container': 'div.product, div.product-item, li.product',
    'product_title': 'h1, h2.product-name, a.product-title, span.product-title',
    'product_price': 'span.price, span.product-price, div.price, p.price',
    'product_availability': 'span.availability, span.stock-status, p.availability',
    'product_url': 'a.product-link, a[href*="product"]'
}
```

## Adding New E-Commerce Sites

The scraper is designed to handle multiple e-commerce sites. If selectors fail:

1. Open the website in your browser
2. Inspect the HTML using Developer Tools (F12)
3. Identify the CSS selectors for relevant data
4. The scraper will attempt multiple selector patterns
5. If a selector is unavailable, "NULL" is assigned

## Troubleshooting

### Issue: "No products found on the page"
**Solution:**
- Verify the URL is correct and points to a product listing page
- Check if the website structure changed
- Ensure the website allows scraping (check robots.txt)

### Issue: "Timeout Error"
**Solution:**
- Check your internet connection
- Increase the timeout value in settings
- Try a different URL

### Issue: "ModuleNotFoundError"
**Solution:**
- Ensure virtual environment is activated
- Reinstall dependencies: `pip install -r requirements.txt`

### Issue: "Permission Denied" on CSV export
**Solution:**
- Close any open CSV files
- Ensure write permissions in the project directory

## Best Practices

1. **Respect Websites**: Always follow the website's `robots.txt` and Terms of Service
2. **Add Delays**: Use appropriate delays between requests (default: 2 seconds)
3. **Check Legality**: Verify scraping is allowed before scraping commercial data
4. **Handle Errors**: The scraper includes error handling, but monitor logs for issues
5. **Update Selectors**: Regularly check if websites have updated their structure

## Performance Tips

- **Batch Processing**: Scrape during off-peak hours to minimize server load
- **Pagination**: Use multiple URLs for sites with pagination
- **Caching**: Implement caching to avoid redundant requests
- **Connection Pooling**: The requests library handles this automatically

## File Organization

### scraper.py
Contains the `EcommerceScraper` class with methods for:
- URL validation
- HTML parsing
- CSS selector application
- Data extraction and cleaning
- CSV export with timestamps

### app.py
Streamlit application featuring:
- URL input interface
- Settings configuration
- Real-time scraping progress
- Data visualization
- CSV download functionality

## Dependencies Explanation

| Package | Purpose | Version |
|---------|---------|----------|
| requests | HTTP requests to fetch web pages | 2.31.0+ |
| beautifulsoup4 | HTML parsing and extraction | 4.12.0+ |
| streamlit | Web application framework | 1.28.0+ |
| pandas | Data manipulation and CSV handling | 2.1.0+ |
| lxml | Enhanced HTML parsing | 4.9.0+ |

## Running Tests

You can test the scraper with sample e-commerce websites:

```bash
python scraper.py
```

This will run the scraper on a test URL and display results.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

**Harsh Goyal** - Data Engineer at KPMG India
- GitHub: [@Harsh4DS](https://github.com/Harsh4DS)
- Email: hgthemercury4@gmail.com

## Disclaimer

This tool is provided for educational purposes. Users are responsible for:
- Ensuring compliance with local laws and regulations
- Respecting website Terms of Service
- Checking `robots.txt` and respecting scraping rules
- Using the tool responsibly and ethically

The author and repository are not responsible for misuse or legal issues arising from the tool's usage.

## Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing issues for solutions
- Include error messages and URL details when reporting bugs

## Changelog

### Version 1.0.0 (Initial Release)
- Core scraper functionality
- Multi-site CSS selector support
- Streamlit UI
- CSV export with timestamps
- Error handling and logging

---

**Last Updated**: January 2025
**Status**: Active Development
