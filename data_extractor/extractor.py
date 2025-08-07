import requests
from bs4 import BeautifulSoup

def fetch_html(url: str) -> str:
    """Download the HTML content from a URL."""
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def extract_first_paragraph(html: str) -> str:
    """Return the text of the first <p> tag found."""
    soup = BeautifulSoup(html, "html.parser")
    p = soup.find("p")
    return p.get_text() if p else ""
