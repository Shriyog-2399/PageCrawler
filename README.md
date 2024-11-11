# Recursive URL Spider

This Python script performs recursive web scraping to discover and collect unique URLs from a given starting URL, filtering them based on a specified keyword. The script leverages Python's `requests` library to make HTTP requests and `BeautifulSoup` to parse HTML content. It explores pages recursively up to a set depth, collecting URLs that match the provided keyword while preventing duplicates.

## Features

- **Recursive URL Discovery**: Scrapes URLs from the starting point and its linked pages up to a specified depth.
- **Keyword Filtering**: Filters URLs containing a specific keyword.
- **Duplicate Prevention**: Ensures URLs are collected only once, preventing redundant entries.
- **Error Handling**: Catches and reports HTTP errors gracefully, skipping invalid URLs.

## Installation

To use this script, ensure you have the following Python libraries installed:

1. `requests` for handling HTTP requests.
2. `beautifulsoup4` for parsing HTML content.

You can install them via `pip`:

```bash
pip install requests beautifulsoup4
