import csv

def read_and_display_books(filename='book_data.csv'):
    """Reads book data from a CSV file and displays it in a formatted way."""
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            print(f"Reading data from {filename}:\n")
            for row in reader:
                print(f"  Title: {row['Title']}")
                print(f"  Author: {row['Author']}")
                print(f"  Publication Year: {row['Publication Year']}")
                print(f"  ISBN: {row['ISBN']}")
                print(f"  Genre: {row['Genre']}")
                print("-" * 20)
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    read_and_display_books()
