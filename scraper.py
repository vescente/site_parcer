import requests
from bs4 import BeautifulSoup
import json

def fetch_quotes(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = []

    for quote in soup.select('div.quote'):
        text = quote.select_one('span.text').get_text()
        author = quote.select_one('small.author').get_text()
        quotes.append({'text': text, 'author': author})

    return quotes

def save_quotes(quotes, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(quotes, f, ensure_ascii=False, indent=4)

def main():
    url = 'https://quotes.toscrape.com/'
    quotes = fetch_quotes(url)
    save_quotes(quotes, 'quotes.json')
    print(f'Saved {len(quotes)} quotes to quotes.json')

if __name__ == '__main__':
    main()