import streamlit as st
from bs4 import BeautifulSoup
import undetected_chromedriver as uc

# Streamlit App
st.title("Menu Scraper with Selenium")

# Input for URL
url = st.text_input("Enter the URL to scrape:", "")

# Input for Debug Mode
debug_mode = st.checkbox("Disable headless mode for debugging", value=False)

if st.button("Scrape Menu"):
    if url:
        try:
            # Set up undetected Chrome driver
            options = uc.ChromeOptions()
            if not debug_mode:
                options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            driver = uc.Chrome(options=options)

            # Fetch the page source
            driver.get(url)
            page_source = driver.page_source

            # Parse the page source
            soup = BeautifulSoup(page_source, 'html.parser')

            # Extract menu items
            menu_items = []
            menu_elements = soup.find_all('button', class_='card p-6 menu-item')

            for item in menu_elements:
                title = item.find('h2', class_='menu-item-title').text.strip() if item.find('h2', class_='menu-item-title') else None
                description = item.find('p', class_='menu-item-description').text.strip() if item.find('p', class_='menu-item-description') else None
                price = item.find('span', class_='text-greenBadge text-base mx-2').text.strip() if item.find('span', class_='text-greenBadge text-base mx-2') else None
                img = item.find('img')['src'] if item.find('img') else None

                menu_items.append({
                    'Name': title,
                    'Description': description,
                    'Price': price,
                    'Image Link': img
                })

            # Close the driver
            driver.quit()

            # Display results
            if menu_items:
                st.success("Menu items scraped successfully!")
                for menu_item in menu_items:
                    st.subheader(menu_item['Name'])
                    st.write(f"**Description:** {menu_item['Description']}")
                    st.write(f"**Price:** {menu_item['Price']}")
                    if menu_item['Image Link']:
                        st.image(menu_item['Image Link'], width=200)
            else:
                st.warning("No menu items found.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter a valid URL.")
