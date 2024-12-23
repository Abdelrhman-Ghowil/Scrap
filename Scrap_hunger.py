import streamlit as st
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import tempfile
import os

# Streamlit UI
def main():
    st.title("HungerStation Menu Scraper")

    url = st.text_input("Enter HungerStation URL", value="https://hungerstation.com/sa-en/restaurant/eataly/riyadh/al-muhammadeya/11829?utm_source")

    if st.button("Scrape Menu"):
        with st.spinner("Scraping the menu. Please wait..."):
            driver = None  # Initialize driver to None
            try:
                # Set up Chrome options
                chrome_options = Options()
                chrome_options.add_argument("--headless")  # Run in headless mode
                chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
                chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

                # Set ChromeDriver path
                chrome_driver_path = "/usr/bin/chromedriver"  # Update this path as per your environment

                # Initialize WebDriver
                driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

                # Open the URL
                driver.get(url)

                # Wait for the page to load (modify if CAPTCHA exists)
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "card"))
                )

                # Get page source
                page_source = driver.page_source

                # Parse the HTML with BeautifulSoup
                soup = BeautifulSoup(page_source, 'html.parser')

                # Extract menu items
                menu_items = []
                menu_elements = soup.find_all('button', class_='card p-6 menu-item')

                for item in menu_elements:
                    title = item.find('h2', class_='menu-item-title').text.strip() if item.find('h2', class_='menu-item-title') else None
                    description = item.find('p', class_='menu-item-description').text.strip() if item.find('p', class_='menu-item-description') else None
                    price = item.find('p', class_='text-greenBadge text-base mx-2').text.strip() if item.find('p', class_='text-greenBadge text-base mx-2') else None
                    img = item.find('img')['src'] if item.find('img') else None

                    menu_items.append({
                        'name': title,
                        'Description': description,
                        'Price': price,
                        'links': img
                    })

                # Save extracted data to an Excel file
                df = pd.DataFrame(menu_items)
                temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx")
                df.to_excel(temp_file.name, index=False)

                st.success("Scraping completed!")

                # Display the data
                st.dataframe(df)

                # Provide download link for the Excel file
                with open(temp_file.name, "rb") as f:
                    st.download_button("Download Excel File", data=f, file_name="menu_items.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

            except Exception as e:
                st.error(f"An error occurred: {e}")

            finally:
                # Close the driver if it was initialized
                if driver:
                    driver.quit()

if __name__ == "__main__":
    main()
