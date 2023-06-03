# This script uses the requests library to make a GET request to the specified URL and retrieve the HTML content of the web page. Then, the 
# beautifulsoup4 library is used to parse the HTML and extract the desired information. The scrape_web_page function takes a URL as input, retrieves 
# the HTML content, and uses BeautifulSoup to extract the desired information from the parsed HTML. In the example, product details (title and price) 
# from an e-commerce website are being scraped. 

import requests
from bs4 import BeautifulSoup
import csv
import json

# Function to make a GET request to a URL and retrieve the HTML content
def get_html_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving HTML content: {str(e)}")

# Function to scrape web page and extract desired information
def scrape_web_page(url):
    # Retrieve HTML content of the web page
    html_content = get_html_content(url)
    if not html_content:
        return
    
    # Create BeautifulSoup object to parse HTML
    soup = BeautifulSoup(html_content, "html.parser")

    # Extract desired information from the parsed HTML
    # Example: Scraping product details from an e-commerce website
    product_title = soup.find("h1", class_="product-title").text.strip()
    product_price = soup.find("span", class_="product-price").text.strip()

    # Perform further analysis or processing on the extracted data
    # Example: Print the product details
    print("Product Title:", product_title)
    print("Product Price:", product_price)
    print("")

    # Store the extracted data in a structured format (e.g., CSV or JSON)
    # Example: Write the data to a CSV file
    with open("product_details.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Title", "Price"])
        writer.writerow([product_title, product_price])

    # Example: Write the data to a JSON file
    data = {
        "title": product_title,
        "price": product_price
    }
    with open("product_details.json", "w") as jsonfile:
        json.dump(data, jsonfile, indent=4)

# Example usage
url = "https://example.com/product-page"
scrape_web_page(url)
