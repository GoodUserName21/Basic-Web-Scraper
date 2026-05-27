"""
Basic Web Scraper
A simple Python web scraper using requests and BeautifulSoup
"""

import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime


class WebScraper:
    """A basic web scraper class for extracting data from websites"""
    
    def __init__(self, url, headers=None):
        """
        Initialize the scraper with a URL
        
        Args:
            url (str): The URL to scrape
            headers (dict): Optional headers for the request
        """
        self.url = url
        self.headers = headers or {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        self.soup = None
        self.content = None
    
    def fetch(self):
        """Fetch the webpage content"""
        try:
            response = requests.get(self.url, headers=self.headers, timeout=10)
            response.raise_for_status()
            self.content = response.text
            self.soup = BeautifulSoup(self.content, 'html.parser')
            print(f"✓ Successfully fetched: {self.url}")
            return True
        except requests.RequestException as e:
            print(f"✗ Error fetching {self.url}: {e}")
            return False
    
    def get_title(self):
        """Extract the page title"""
        if not self.soup:
            return None
        title = self.soup.find('title')
        return title.text if title else None
    
    def get_headings(self):
        """Extract all headings from the page"""
        if not self.soup:
            return []
        headings = []
        for tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            for heading in self.soup.find_all(tag):
                headings.append({
                    'level': tag,
                    'text': heading.get_text(strip=True)
                })
        return headings
    
    def get_paragraphs(self):
        """Extract all paragraphs from the page"""
        if not self.soup:
            return []
        paragraphs = []
        for p in self.soup.find_all('p'):
            text = p.get_text(strip=True)
            if text:
                paragraphs.append(text)
        return paragraphs
    
    def get_links(self):
        """Extract all links from the page"""
        if not self.soup:
            return []
        links = []
        for link in self.soup.find_all('a', href=True):
            links.append({
                'text': link.get_text(strip=True),
                'href': link['href']
            })
        return links
    
    def get_images(self):
        """Extract all image URLs from the page"""
        if not self.soup:
            return []
        images = []
        for img in self.soup.find_all('img'):
            images.append({
                'src': img.get('src'),
                'alt': img.get('alt', '')
            })
        return images
    
    def export_to_json(self, filename='scraped_data.json'):
        """Export scraped data to a JSON file"""
        if not self.soup:
            print("No data to export. Run fetch() first.")
            return False
        
        data = {
            'url': self.url,
            'timestamp': datetime.now().isoformat(),
            'title': self.get_title(),
            'headings': self.get_headings(),
            'paragraphs': self.get_paragraphs(),
            'links': self.get_links(),
            'images': self.get_images()
        }
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"✓ Data exported to {filename}")
            return True
        except Exception as e:
            print(f"✗ Error exporting to JSON: {e}")
            return False


def main():
    """Example usage of the WebScraper"""
    # Example: Scrape a website
    url = input("Enter the URL to scrape: ")
    
    scraper = WebScraper(url)
    
    if scraper.fetch():
        print("\n--- Page Title ---")
        print(scraper.get_title())
        
        print("\n--- Headings ---")
        for heading in scraper.get_headings()[:5]:  # Show first 5
            print(f"{heading['level'].upper()}: {heading['text']}")
        
        print("\n--- Links (first 5) ---")
        for link in scraper.get_links()[:5]:
            print(f"- {link['text']}: {link['href']}")
        
        print("\n--- Images (first 5) ---")
        for image in scraper.get_images()[:5]:
            print(f"- {image['alt'] or 'No alt text'}: {image['src']}")
        
        # Export to JSON
        export = input("\nExport to JSON? (y/n): ").lower()
        if export == 'y':
            scraper.export_to_json()


if __name__ == '__main__':
    main()
