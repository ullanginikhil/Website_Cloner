# Website Cloner and Crawler

## Overview
This **Website Cloner and Crawler** is a Python-based tool that allows users to crawl a website, download all its HTML, CSS, and JavaScript files, and save them into organized folders on the local machine. The tool is designed to recursively traverse all internal links within the domain, ensuring that the entire site structure is cloned.

## Features
- **HTML Cloning**: Downloads the main HTML files from the website, including all internal pages linked from the starting page.
- **CSS & JavaScript**: Fetches and saves all external CSS stylesheets and JavaScript files linked on each page.
- **Recursive Crawling**: Follows all internal links within the domain to ensure a complete website clone.
- **Folder Structure**: Saves the HTML files in the `html` folder, CSS files in the `css` folder, and JavaScript files in the `js` folder, mimicking the site's structure.
- **Error Handling**: Handles broken links or inaccessible pages gracefully, logging issues without crashing the program.
- **Duplicate Handling**: Tracks visited URLs to prevent downloading the same page multiple times.

## Usage
1. Clone the repository and install the dependencies using the following command:
   ```bash
   pip install requests beautifulsoup4 lxml
