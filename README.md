# HungerStation Menu Scraper 🚀

This project is a **Streamlit web application** that scrapes menu items from HungerStation restaurant pages. It uses Selenium in UC (Undetectable Chrome) mode to bypass CAPTCHA challenges and BeautifulSoup for parsing the scraped data. Extracted data can be downloaded as an Excel file. 🎉

## Features 🌟

- 🚀 **Bypass CAPTCHA:** Seamlessly handle CAPTCHA challenges using Selenium UC mode.
- 📝 **Data Extraction:** Extract menu items including title, description, price, and image.
- 📊 **Streamlit Integration:** View scraped data in an interactive table.
- 📥 **Excel Export:** Download the extracted data as an Excel file.

## How to Use 📖

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/hungerstation-scraper.git
   cd hungerstation-scraper
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run hungerstation_scraper.py
   ```

4. Open the provided URL in your browser and enter a HungerStation restaurant URL to start scraping! 🌐

## Technologies Used 💻

- **SeleniumBase:** For web scraping and CAPTCHA handling.
- **BeautifulSoup:** For HTML parsing and data extraction.
- **Pandas:** To structure and export data to Excel.
- **Streamlit:** To build the interactive user interface.

## File Overview 📂

- `hungerstation_scraper.py`: Main application script.
- `requirements.txt`: Lists all required Python libraries.
- `menu_items.xlsx`: Example output file (generated after scraping).

## Example Output 🎯

| Title        | Description        | Price | Image URL |
|--------------|--------------------|-------|-----------|
| Menu Item 1  | A tasty appetizer  | $10   | [link]    |
| Menu Item 2  | A delicious entree | $20   | [link]    |

## Contributing 🤝

Contributions are welcome! If you have any improvements or suggestions, feel free to open an issue or submit a pull request. 🌟

## License 📜

This project is licensed under the MIT License. Feel free to use, modify, and distribute it! 👐

---

_Enjoy scraping menus and building cool projects! 🚀_

