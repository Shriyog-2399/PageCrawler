This Python-based web crawler tool recursively scrapes URLs from a specified website and extracts links containing a given keyword. It uses BeautifulSoup for HTML parsing and requests for making HTTP requests, ensuring efficiency in navigating and capturing data from web pages.
Features

    Recursively crawls web pages to a specified depth.
    Collects and prints URLs that match a specified keyword.
    Avoids visiting duplicate URLs for faster performance.
    Error handling to skip invalid URLs.

Prerequisites

    Python 3.x
    Required Libraries:
        requests - For making HTTP requests.
        BeautifulSoup - For parsing and navigating HTML.

Installation

    Clone this repository:

git clone https://github.com/yourusername/web-crawler-tool.git
cd web-crawler-tool

Install the required Python libraries:

    pip install requests beautifulsoup4

Usage

To run the crawler, use:

python web_crawler.py

Example

When prompted, enter the URL to start crawling and a keyword for filtering URLs:

Enter the url: https://example.com
Enter the keyword: blog

The tool will print all URLs containing "blog" found within the specified domain, up to the maximum depth limit.
Code Explanation

    Function spider_urls:
        Parameters: url (start URL), keyword (filter keyword), max_depth (recursion limit), current_depth (tracking depth).
        Makes an HTTP request to each page, parsing links and checking for relevance to the keyword.
        Recursively follows links up to max_depth, avoiding duplicate URLs.

Notes

    The maximum depth for recursion can be adjusted by modifying the max_depth argument.
    URLs are filtered based on the keyword, ensuring only relevant links are processed.

