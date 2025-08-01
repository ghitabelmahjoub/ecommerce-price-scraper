import requests
from bs4 import BeautifulSoup
import pandas as pd

books = []

for page in range(1, 4):  # Scrape pages 1 to 3
    url = f'http://books.toscrape.com/catalogue/page-{page}.html'
    print(f"Scraping page {page}...")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for book in soup.select('article.product_pod'):
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        books.append({'title': title, 'price': price})

print(f"Scraped {len(books)} books across 3 pages!")

# Save to CSV
df = pd.DataFrame(books)
df.to_csv('books_prices_multi.csv', index=False)
print("Scraping done! Data saved to books_prices_multi.csv")
