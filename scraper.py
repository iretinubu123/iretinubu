# scraper.py

import requests
from bs4 import BeautifulSoup

def scrape_books(url):
    """
    Scrapes the books from the given URL and extracts their title, price, and rating.

    Args:
        url (str): The URL of the website to scrape.

    Returns:
        list: A list of dictionaries, where each dictionary represents a book.
              Returns an empty list if scraping fails.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes

        soup = BeautifulSoup(response.content, 'lxml')
        books = []
        
        for item in soup.select('article.product_pod'):
            title = item.h3.a['title']
            price = item.select_one('p.price_color').get_text(strip=True)
            rating = item.p['class'][1]  # The rating is the second class, e.g., 'Three'
            
            books.append({
                'title': title,
                'price': price,
                'rating': rating
            })
        
        return books

    except requests.exceptions.RequestException as e:
        print(f"Error during requests to {url}: {e}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
