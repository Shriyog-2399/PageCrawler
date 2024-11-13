URL Spider with Keyword Filte

This project is a Python-based web crawler that recursively searches for URLs starting from a specified URL. It includes keyword filtering to only capture URLs that contain a specific keyword. The spider prevents duplicate URLs from being revisited by maintaining a set of visited URLs. It uses the requests library for HTTP requests, BeautifulSoup for HTML parsing, and urljoin for creating absolute URLs.
Features

    Recursive Crawling: The script crawls pages up to a maximum depth, which you can set via the max_depth parameter.
    Keyword Filtering: Only URLs that contain the specified keyword are printed and added to the visited set.
    Duplicate Prevention: Tracks visited URLs to avoid duplicate entries.

Requirements

Install the required libraries using:

pip install requests beautifulsoup4

Usage

    Run the script:

    python spider.py

    Enter the URL and the keyword to filter URLs.

Example:

Enter the URL: http://example.com
Enter the keyword: blog

The script will crawl http://example.com for URLs that contain "blog."
Code Overview

    spider_urls function: The primary recursive function that:
        Crawls a specified URL to a maximum depth.
        Uses BeautifulSoup to find all anchor tags (<a>) and extracts the URLs.
        Filters URLs based on the keyword, then prints and stores each URL if it meets the criteria.

Notes

    Error Handling: The script handles HTTP request errors and skips invalid URLs.
    Customization: Adjust the max_depth parameter to set the recursion depth.

Example Output

Enter the URL: http://example.com
Enter the keyword: news
http://example.com/news/article1
http://example.com/news/article2

This README provides instructions on installation, usage, and code functionality, making it clear and easy to use for anyone interested in web scraping or crawling.
