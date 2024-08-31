import requests
from bs4 import BeautifulSoup

# URL of the webpage you want to scrape
url = 'https://webscraper.io/test-sites/e-commerce/allinone' # Replace with the actual URL

# Send a GET request to the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Print raw HTML content for debugging
    # Uncomment the line below to print HTML content if needed
    # print(response.text[:1000])  # Print first 1000 characters to check content
    
    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all article elements with the specific class names
    titles = soup.find_all('a', class_='title')
    prices = soup.find_all('h4', class_='price float-end card-title pull-right')
    
    # Check if titles and prices were found
    if not titles or not prices:
        print('No titles or prices found. Check the HTML structure.')
    
    # Iterate over the titles and prices
    for title, price in zip(titles, prices):
        # Extract the text from the elements
        article_title = title.text.strip()
        article_price = price.text.strip()
        
        print(f'Title: {article_title}')
        print(f'Price: {article_price}')
        print('-' * 40)
else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')

