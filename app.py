import csv
from flask import Flask, render_template

app = Flask(__name__)

def get_books():
    books = []
    try:
        with open('book_data.csv', mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                books.append(row)
    except FileNotFoundError:
        print("Error: The file book_data.csv was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return books

@app.route('/')
def index():
    books = get_books()
    return render_template('index.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
