"""
Example script showing different ways to use the web scraper
"""

from scraper import WebScraper


def example_1_basic():
    """Basic example: scrape a website and print results"""
    print("=" * 50)
    print("Example 1: Basic Usage")
    print("=" * 50)
    
    url = "https://example.com"
    scraper = WebScraper(url)
    
    if scraper.fetch():
        print(f"\nTitle: {scraper.get_title()}")
        print(f"\nFound {len(scraper.get_links())} links")
        print(f"Found {len(scraper.get_paragraphs())} paragraphs")


def example_2_with_custom_headers():
    """Example: use custom headers for the request"""
    print("\n" + "=" * 50)
    print("Example 2: Custom Headers")
    print("=" * 50)
    
    custom_headers = {
        'User-Agent': 'My Custom Bot/1.0',
        'Accept-Language': 'en-US'
    }
    
    url = "https://example.com"
    scraper = WebScraper(url, headers=custom_headers)
    
    if scraper.fetch():
        print(f"Successfully fetched with custom headers")


def example_3_extract_links():
    """Example: extract and display links"""
    print("\n" + "=" * 50)
    print("Example 3: Extract Links")
    print("=" * 50)
    
    url = "https://example.com"
    scraper = WebScraper(url)
    
    if scraper.fetch():
        links = scraper.get_links()
        print(f"\nFound {len(links)} links:")
        for i, link in enumerate(links[:5], 1):
            print(f"{i}. {link['text']}")
            print(f"   URL: {link['href']}")


def example_4_export_to_json():
    """Example: export scraped data to JSON"""
    print("\n" + "=" * 50)
    print("Example 4: Export to JSON")
    print("=" * 50)
    
    url = "https://example.com"
    scraper = WebScraper(url)
    
    if scraper.fetch():
        scraper.export_to_json('example_data.json')
        print("Data exported to example_data.json")


if __name__ == '__main__':
    # Run examples (uncomment to test)
    example_1_basic()
    # example_2_with_custom_headers()
    # example_3_extract_links()
    # example_4_export_to_json()
