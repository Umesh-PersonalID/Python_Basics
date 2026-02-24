from bs4 import BeautifulSoup
import requests


#what is beautiful soup?

#Beautiful Soup is a Python library used for web scraping purposes to pull the data out of HTML and XML files. It creates a parse tree for parsed pages that can be used to extract data from HTML, which is useful for web scraping. Beautiful Soup provides simple methods and Pythonic idioms for navigating, searching, and modifying the parse tree, making it easy to extract the information you need from web pages.
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
        
#ambigous meaning if there is 2 or more possible interpretation of same sentence then it is called ambigous meaning.q