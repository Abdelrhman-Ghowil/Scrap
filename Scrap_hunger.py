import streamlit as st
from seleniumbase import Driver
from bs4 import BeautifulSoup
import pandas as pd
import tempfile

# Streamlit UI
def main():
    st.title("HungerStation Menu Scraper")

    url = st.text_input("Enter HungerStation URL", value="https://hungerstation.com/sa-en/restaurant/eataly/riyadh/al-muhammadeya/11829?utm_source")

    if st.button("Scrape Menu"):
        with st.spinner("Scraping the menu. Please wait..."):
            try:
                # Initialize driver in UC Mode
                driver = Driver(uc=True)

                # Open URL with CAPTCHA handling
                driver.uc_open_with_reconnect(url, 4)

                # Wait for CAPTCHA completion (if necessary)
                driver.uc_gui_click_captcha()

                # Get page source
                page_source = driver.page_source

                # Use BeautifulSoup to parse the HTML
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
                # Close the driver
                driver.quit()

if __name__ == "__main__":
    main()
