import requests
from bs4 import BeautifulSoup
import csv

def scrape_amazon(search_term):
    url = f"https://www.amazon.com/s?k={search_term}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    items = soup.find_all("div", {"data-component-type": "s-search-result"})
    scraped_data = []
    
    for item in items[:10]:  # Limit to 10 items
        title = item.h2.text.strip() if item.h2 else "No title"
        price = item.find("span", "a-price-whole")
        price = price.text if price else "No price"
        rating = item.find("span", "a-icon-alt")
        rating = rating.text if rating else "No rating"
        scraped_data.append([title, price, rating])
    
    # Save to CSV
    with open("amazon_products.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Price", "Rating"])
        writer.writerows(scraped_data)

    print("Scraped data saved to amazon_products.csv")

scrape_amazon("laptop")