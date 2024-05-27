import requests
from bs4 import BeautifulSoup

# Function to get HTML content of the page
def get_html_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

# Function to parse HTML and extract data
def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'lxml')
    
    data = {
        'headings': [],
        'paragraphs': []
    }
    
    # Extract headings
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    for heading in headings:
        data['headings'].append(heading.get_text().strip())
    
    # Extract paragraphs
    paragraphs = soup.find_all('p')
    for paragraph in paragraphs:
        data['paragraphs'].append(paragraph.get_text().strip())
    
    return data

# Function to save data to a text file
def save_to_file(data, filename):
    try:
        with open(filename, 'w') as file:
            file.write("Headings:\n")
            for heading in data['headings']:
                file.write(heading + "\n")
            
            file.write("\nParagraphs:\n")
            for paragraph in data['paragraphs']:
                file.write(paragraph + "\n")
        
        print(f"Data saved to {filename}")
    except IOError as e:
        print(f"Error writing to {filename}: {e}")

# Main function
def main(url, output_file):
    html_content = get_html_content(url)
    if html_content:
        data = parse_html(html_content)
        save_to_file(data, output_file)

if __name__ == "__main__":
    url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'  # URL of the Wikipedia page
    output_file = 'scraped_data.txt'  # Output file name
    main(url, output_file)
