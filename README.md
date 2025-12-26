# 🛒 E-Commerce Web Scraper

A powerful, modular Python-based web scraper designed to extract comprehensive product data from multiple e-commerce websites. Features both manual scraping (CLI & Streamlit Web UI) and fully automated scheduled scraping with formatted Excel exports.

## ✨ Features

- **🌐 Multi-Site Support**: Scrapes from web-scraping.dev, Flipkart, eBay, Walmart, and other e-commerce platforms
- **📊 Comprehensive Data Extraction**: Extracts 20+ product attributes including:
  - Product name, price, availability
  - Product URLs and images
  - Seller info and ratings
  - Original price, discount percentage
  - Stock quantity and status
  - Category, SKU, specs, warranty
  - And more!
- **📁 Excel & CSV Export**: Automatic date-based file naming (products_YYYYMMDD.xlsx)
- **⚙️ Flexible CSS Selectors**: Standardized selectors that work across multiple e-commerce sites
- **🤖 Automated Scheduling**: Background scheduler for periodic scraping
- **🖥️ Streamlit UI**: User-friendly web interface for manual scraping
- **⚡ Polite Scraping**: Built-in delays and headers to respect server resources
- **🛡️ Error Handling**: Robust error handling for missing selectors and network issues
- **🏗️ Modular Architecture**: Separated scraper logic, UI, and scheduler for easy maintenance

## 📋 Project Structure

```
ecommerce-web-scraper/
├── scraper.py              # Core scraping logic with CSS selectors
├── app.py                  # Streamlit web UI application
├── scheduler.py            # Automated scheduling for periodic scraping
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore file
├── scraped_data/          # Output folder for CSV and Excel files
└── README.md              # This file
```

## 🔧 System Requirements

- **Python**: 3.8 or higher
- **OS**: Windows, macOS, or Linux
- **Internet Connection**: Required for scraping

## 📦 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/The-Harsh-Goyal/ecommerce-web-scraper.git
cd ecommerce-web-scraper
```

### Step 2: Create a Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## 🚀 Usage

### Option 1: Web UI (Streamlit) - Recommended for Beginners

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501` where you can:
1. Enter the e-commerce website URL
2. Click "Scrape Now" to extract products
3. View results in a table
4. Download as CSV or Excel

### Option 2: CLI (Command Line) - Direct Scraping

```bash
python scraper.py
```

This will scrape the default URL (web-scraping.dev) and save results to `scraped_data/products_YYYYMMDD.xlsx`

### Option 3: Python Script - Advanced Usage

```python
from scraper import scrape_and_save

url = "https://www.web-scraping.dev/products"
success, message, df, count = scrape_and_save(url)

if success:
    print(f"Scraped {count} products successfully!")
    print(df.head())  # Display first 5 products
```

### Option 4: Automated Scheduling

```bash
python scheduler.py
```

Runs automatic scraping at scheduled intervals and saves data to Excel files.

## 🌍 Supported E-Commerce Sites

The scraper works with:
- ✅ **web-scraping.dev** (Primary testing site)
- ✅ **Flipkart**
- ✅ **eBay**
- ✅ **Walmart**
- ✅ **Any other e-commerce site** (with compatible HTML structure)

## 🎯 CSS Selectors Used

The scraper uses multiple fallback CSS selectors for robustness. Here are the main ones:

### Product Block/Container
```python
[".product", ".row.product", ".product-card", ".product-tile", 
 ".product-item", ".product-listing", ".plp-card",
 "div._4ddWXP",  # Flipkart
 "div[data-automation-id*='product']",  # Walmart
 "div.s-item"]  # eBay
```

### Product Title
```python
[".product-name", "h2.product-name", "h3.product-name", 
 "h2.product-title", "h3.product-title", ".product-title", "h2", "h3"]
```

### Product Price
```python
[".product-price", ".price", "span.price", ".sale-price", 
 "[class*='price']", ".current-price", ".item-price",
 "div._30jeq3",  # Flipkart
 "span._16Jk6d",  # Flipkart
 "span[data-automation-id*='price']",  # Walmart
 "span.s-item-price"]  # eBay
```

### Availability Status
```python
[".availability", ".stock-status", ".in-stock", ".stock", 
 "[class*='availability']", "[class*='stock']", 
 ".stock-info", "span.SECONDARY_INFO"]  # eBay
```

### Product Link
```python
["a.product-link", "a.product-name", ".product a", 
 "a[href*='product']", "a[href*='item']", "a"]
```

### Additional Selectors
- **Image**: `.product-image`, `img[src*='product']`, `img[alt*='product']`
- **Seller**: `.seller-name`, `.vendor-name`, `[class*='seller']`
- **Rating**: `.product-rating`, `.rating`, `.star-rating`, `[class*='rating']`
- **Discount**: `.discount-percentage`, `.discount-badge`, `[class*='discount']`
- **Stock Quantity**: `.stock-count`, `.quantity-left`, `[class*='stock-count']`
- **Category**: `.breadcrumb`, `.product-category`, `[class*='category']`
- **Condition**: `.condition`, `.product-condition`, `[class*='condition']`
- **Delivery**: `.delivery-info`, `.shipping-info`, `[class*='delivery']`
- **SKU**: `.product-sku`, `.sku`, `[data-sku]`, `[data-product-id]`
- **Specs**: `.specs`, `.highlights`, `.product-specs`, `[class*='spec']`
- **Warranty**: `.warranty`, `.guarantee`, `[class*='warranty']`

## 📊 Output Format

Scraped data is saved in the `scraped_data/` folder with automatic date-based naming:

### Filename Format
```
products_YYYYMMDD.xlsx  (Example: products_20251226.xlsx)
products_YYYYMMDD.csv   (Example: products_20251226.csv)
```

### Excel Columns (20+ attributes)
- product_name
- price
- availability
- product_url
- image_url
- seller
- rating
- units_sold
- condition
- delivery_cost
- seller_rating
- original_price
- discount_in_percentage
- stock_qty
- product_category
- seller_info
- delivery_info
- stock_status
- badge
- product_code (SKU)
- specs
- warranty
- scraped_date
- scraped_time

## ⚙️ Configuration

### Polite Scraping Settings (in scraper.py)

```python
DELAY_RANGE = (2, 5)  # Random delay between 2-5 seconds

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
    "Accept-Language": "en-US,en;q=0.9"
}
```

### Timeout Setting
- Default request timeout: 15 seconds
- Adjustable in `fetch_page()` function

## 🐛 Troubleshooting

### Issue: "No products found on the page"
**Solution:**
- Verify the URL is correct and points to a product listing page
- Check if the website has changed its HTML structure
- Inspect the page with Developer Tools (F12) to find new CSS selectors

### Issue: "Timeout Error"
**Solution:**
- Check your internet connection
- Try increasing timeout value in `fetch_page()` function
- Try a different URL or wait and try again later

### Issue: "ModuleNotFoundError"
**Solution:**
- Ensure virtual environment is activated
- Reinstall dependencies: `pip install -r requirements.txt`

### Issue: Excel file won't open or shows errors
**Solution:**
- Close any existing Excel files with the same name
- Ensure write permissions in the project directory
- Try again with a different filename if needed

## 📚 Workflow Examples

### Workflow 1: Manual Scraping via Web UI
```
1. Run: streamlit run app.py
2. Enter URL in browser
3. Click "Scrape Now"
4. View & download results
```

### Workflow 2: CLI Scraping
```
1. Run: python scraper.py
2. Check scraped_data/ folder
3. Open Excel file to view results
```

### Workflow 3: Automated Daily Scraping
```
1. Run: python scheduler.py
2. Scraper runs at scheduled times
3. New Excel file created each day
```

## ✅ Best Practices

1. **Respect Website Rules**: Always check `robots.txt` and website terms
2. **Use Appropriate Delays**: The scraper includes 2-5 second delays by default
3. **Handle Errors Gracefully**: The scraper includes error handling
4. **Check Legal Compliance**: Ensure scraping is allowed for your use case
5. **Update Selectors**: Websites change their HTML structure - update selectors as needed
6. **Use Virtual Environment**: Keeps your project dependencies isolated

## 🔄 How It Works

1. **Fetch**: Downloads HTML from the provided URL with headers and timeout
2. **Delay**: Applies random delay (2-5 seconds) to be polite
3. **Parse**: Uses BeautifulSoup to parse HTML and extract product data
4. **Extract**: Applies multiple CSS selectors with fallbacks for robustness
5. **Save**: Exports data to both Excel (formatted) and CSV (compatible)

## 🛠️ Development

### Project Dependencies
- **requests**: HTTP library for fetching pages
- **beautifulsoup4**: HTML parsing and extraction
- **pandas**: Data manipulation and CSV/Excel handling
- **openpyxl**: Excel file creation and formatting
- **streamlit**: Web UI framework

### Code Structure
- `extract_with_fallbacks()`: Tries multiple selectors until one works
- `fetch_page()`: Safely fetches webpage HTML
- `parse_products()`: Extracts product data from HTML
- `save_to_csv_and_excel()`: Exports to both formats with formatting
- `scrape_and_save()`: Main orchestration function

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Harsh Goyal**
- Data Engineer at KPMG India
- GitHub: [@The-Harsh-Goyal](https://github.com/The-Harsh-Goyal)
- LinkedIn: [harsh-goyal1025](https://www.linkedin.com/in/harsh-goyal1025/)
- Email: hgthemercury4@gmail.com

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 💡 Future Enhancements

- [ ] Support for JavaScript-heavy websites (Selenium)
- [ ] Advanced filtering and search options
- [ ] Database support (SQLite, PostgreSQL)
- [ ] API endpoint for scraping
- [ ] Docker containerization
- [ ] Cloud deployment ready

## ⚠️ Disclaimer

This tool is provided for educational and legitimate business use. Users are responsible for:
- Ensuring compliance with local laws and regulations
- Respecting website Terms of Service
- Checking `robots.txt` and respecting scraping rules
- Using the tool responsibly and ethically

The author is not responsible for misuse or legal issues arising from the tool's usage.

## 🎯 Quick Start

```bash
# 1. Clone
git clone https://github.com/The-Harsh-Goyal/ecommerce-web-scraper.git
cd ecommerce-web-scraper

# 2. Setup
python -m venv venv
source venv/bin/activate  # or: venv\Scripts\activate (Windows)
pip install -r requirements.txt

# 3. Run
streamlit run app.py

# 4. Open browser and start scraping!
```

---

**Last Updated**: 2025-12-26  
**Version**: 1.0.0  
**Status**: ✅ Active Development
