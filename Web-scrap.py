
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup      #BeautifulSoup used for web scrapin, it helps you extract and manipulate data from HTML and XML files.
from urllib import *


visited_urls = set ()      #Duplicate url won't be added


def spider_urls(url, keyword, max_depth=3, current_depth=0):

    if current_depth > max_depth:
        return  # Stop recursion if max depth is reached.

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for bad responses.

    except requests.RequestException as e:
        print(f"Invalid {url}: {e}")
        return



    # Only process if the status code is 200
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")       ## Parse HTML content / source code.
        a_tag = soup.find_all('a')       #find all anchor tags
        urls = []

        for tag in a_tag:
            href = tag.get("href")
            if href is not None and href != "":
                urls.append(href)

        
        for url_link in urls:
            url_join = urljoin(url, url_link)
            # Only add if it hasn't been visited and it's a relevant link
            if url_join not in visited_urls and keyword in url_join:
                visited_urls.add(url_join)  # Add to the visited set.
                print(url_join)  # Print the found URL.
                spider_urls(url_join, keyword, max_depth, current_depth + 1)  # Recursively call the function.




url = input("Enter the url: ")
keyword = input("Enter the keyword: ")
spider_urls(url, keyword)

