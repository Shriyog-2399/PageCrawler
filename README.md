**Overview*

The URL Spider Tool is a Python-based web crawler designed to recursively collect and filter URLs from a given website based on a specified keyword. It efficiently traverses links up to a user-defined depth, ensuring duplicate URLs are avoided and only relevant links containing the keyword are considered.

This tool is ideal for penetration testers, researchers, and developers who need to gather URLs matching specific criteria for further analysis or processing.
Features

    Recursive Crawling: Automatically follows links on web pages to a specified depth.
    Keyword Filtering: Only includes URLs containing a user-defined keyword.
    Duplicate Avoidance: Ensures each URL is processed only once.
    Error Handling: Skips invalid URLs or pages that cannot be accessed.
    HTML Parsing: Uses BeautifulSoup to extract links from HTML content.

**Requirements**

Before running the tool, ensure you have the following installed:

    Python 3.6+
    Required Python libraries:
        requests
        beautifulsoup4

To install the dependencies, run:

pip install requests beautifulsoup4

Usage

    Clone or download the script to your local machine.

    Run the script:

    python spider_urls.py

    Input the target URL and keyword when prompted:
        URL: The starting point for the web crawler (e.g., https://example.com).
        Keyword: A string that the tool will use to filter relevant URLs.

    The tool will recursively crawl the website, extract URLs, and print relevant results to the console.

**Code Explanation**
Key Components:

    Recursive URL Crawling:
        The function spider_urls handles recursive crawling up to the maximum depth specified by the max_depth parameter.

    Keyword Filtering:
        The keyword is checked in each URL to ensure only relevant links are visited and printed.

    Duplicate Avoidance:
        A visited_urls set ensures URLs are not revisited during the crawling process.

    Error Handling:
        The script gracefully skips over pages that result in errors (e.g., 404, 500) or cannot be accessed.


**Example Run**

Input:

Enter the URL: https://example.com
Enter the keyword: product

Output:

https://example.com/product1
https://example.com/product2/details
https://example.com/products/latest


**Configuration**

    Maximum Depth: The default depth is set to 3. You can adjust this by modifying the max_depth parameter in the spider_urls function call.

Limitations

    This tool does not handle JavaScript-rendered content.
    It respects the default behavior of the requests library and does not modify user agents or bypass restrictions.

**Future Enhancements**

    Add support for multi-threading to increase crawling speed.
    Implement handling for JavaScript-heavy websites using tools like selenium or playwright.
    Include support for exporting results to a file.
