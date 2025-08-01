# main.py

import csv
from scraper import scrape_books

if __name__ == "__main__":
    url_to_scrape = "https://adelekeuniversity.edu.ng//"
    output_file = "books.csv"

    print(f"Scraping {url_to_scrape}...")
    books_data = scrape_books(url_to_scrape)

    if books_data:
        print(f"Scraping successful! Found {len(books_data)} books.")
        
        # Write data to CSV file
        try:
            with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['title', 'price', 'rating']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                for book in books_data:
                    writer.writerow(book)
            
            print(f"Data successfully saved to {output_file}")

        except IOError as e:
            print(f"Error writing to file {output_file}: {e}")

    else:
        print("Scraping failed or no books were found.")
