# Basic-Web-Scraper

A simple and easy-to-use Python web scraper for extracting data from websites.

## Features

- ✨ Extract page titles, headings, paragraphs, links, and images
- 📥 Support for custom headers
- 🔍 BeautifulSoup-powered HTML parsing
- 💾 Export scraped data to JSON format
- ⚡ Simple and intuitive API

## Installation

1. Clone this repository:
```bash
git clone https://github.com/GoodUserName21/Basic-Web-Scraper.git
cd Basic-Web-Scraper
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

Run the scraper interactively:
```bash
python scraper.py
```

You'll be prompted to enter a URL and choose whether to export the data to JSON.

### Using as a Module

```python
from scraper import WebScraper

# Create scraper instance
scraper = WebScraper('https://example.com')

# Fetch the page
if scraper.fetch():
    # Extract data
    title = scraper.get_title()
    headings = scraper.get_headings()
    links = scraper.get_links()
    paragraphs = scraper.get_paragraphs()
    images = scraper.get_images()
    
    # Export to JSON
    scraper.export_to_json('output.json')
```

## API Reference

### WebScraper Class

#### Methods

- `fetch()` - Fetch the webpage content
- `get_title()` - Get the page title
- `get_headings()` - Get all headings (h1-h6)
- `get_paragraphs()` - Get all paragraph text
- `get_links()` - Get all links with text and href
- `get_images()` - Get all images with src and alt text
- `export_to_json(filename)` - Export scraped data to JSON file

## Example Output

```json
{
  "url": "https://example.com",
  "timestamp": "2026-05-27T10:00:00",
  "title": "Example Domain",
  "headings": [
    {
      "level": "h1",
      "text": "Example Domain"
    }
  ],
  "links": [
    {
      "text": "More information...",
      "href": "https://www.iana.org/domains/example"
    }
  ],
  "images": []
}
```

## Requirements

- Python 3.6+
- requests
- beautifulsoup4

## License

This project is open source and available under the MIT License.

## Disclaimer

Always check a website's `robots.txt` and terms of service before scraping. Respect website policies and rate limits.
