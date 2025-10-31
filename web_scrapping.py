from bs4 import BeautifulSoup
import requests

def fetch_page(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.text


def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup 

def extract_data(soup, tag, class_name=None):
    if class_name:
        elements = soup.find_all(tag, class_=class_name)
    else:
        elements = soup.find_all(tag)
    data = [element.get_text() for element in elements] if elements else []
    return data

# Example usage
if __name__ == "__main__":
    url = "https://umesh-personalid.github.io/Umesh-Portfolio/"
    html_content = fetch_page(url)
    soup = parse_html(html_content)
    
    # Extract all paragraph texts
    paragraphs = extract_data(soup, 'p')
    for para in paragraphs:
        print(para)
    
    # Extract all headings with a specific class
    headings = extract_data(soup, 'p', class_name='heading-class')
    for heading in headings:
        print(heading)