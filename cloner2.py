import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# Create directories to save files
def create_dirs(base_dir):
    if not os.path.exists(base_dir):
        os.mkdir(base_dir)
    folders = ["html", "css", "js"]
    for folder in folders:
        path = os.path.join(base_dir, folder)
        if not os.path.exists(path):
            os.mkdir(path)

# Save files to the appropriate folders
def save_file(content, file_path):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    with open(file_path, 'wb') as f:
        f.write(content)

# Download and save HTML, CSS, and JS files
def download_site(url, base_dir, visited):
    # Avoid re-downloading the same page
    if url in visited:
        return
    visited.add(url)
    
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch {url}: {e}")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')

    # Save HTML
    parsed_url = urlparse(url)
    path = parsed_url.path.strip('/')
    if not path:
        path = "index"
    html_file_path = os.path.join(base_dir, 'html', f'{path}.html')
    save_file(response.content, html_file_path)
    print(f"Saved HTML file: {html_file_path}")

    # Save CSS
    for css in soup.find_all('link', rel='stylesheet'):
        css_url = urljoin(url, css['href'])
        css_response = requests.get(css_url)
        css_file_name = os.path.basename(urlparse(css_url).path)
        css_file_path = os.path.join(base_dir, 'css', css_file_name)
        save_file(css_response.content, css_file_path)
        print(f"Saved CSS file: {css_file_path}")

    # Save JS
    for script in soup.find_all('script'):
        if script.get('src'):
            js_url = urljoin(url, script['src'])
            js_response = requests.get(js_url)
            js_file_name = os.path.basename(urlparse(js_url).path)
            js_file_path = os.path.join(base_dir, 'js', js_file_name)
            save_file(js_response.content, js_file_path)
            print(f"Saved JS file: {js_file_path}")

    # Recursively follow all internal links
    for link in soup.find_all('a', href=True):
        link_url = urljoin(url, link['href'])
        link_parsed = urlparse(link_url)

        # Only follow links within the same domain
        if link_parsed.netloc == parsed_url.netloc:
            download_site(link_url, base_dir, visited)

# Main function
def clone_website(url):
    base_dir = 'cloned_website'
    create_dirs(base_dir)
    visited = set()
    download_site(url, base_dir, visited)

if __name__ == "__main__":
    website_url = input("Enter the website URL: ")
    clone_website(website_url)
