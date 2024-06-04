import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = input ("Enter url to scrape: ")
response = requests.get(url)

def fetch_html(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.content

def get_links(soup, base_url):
    links = []
    for strong_tag in soup.find_all('strong'):
        parent = strong_tag.find_parent()
        if parent:
            for a_tag in parent.find_all('a', href = True):
                href = a_tag['href']
                if "Home" in a_tag.get_text() or "Disclaimer" in a_tag.get_text() or "Privacy Policy" in a_tag.get_text() or href.startswith('tel:'):
                    continue
                full_url = urljoin(base_url, href)
                links.append(full_url)

    page_number = soup.find_all
    return links

def crawl(url):
    print(f"Scraping URL: {url}")
    html_content = fetch_html(url)
    soup = BeautifulSoup(html_content, 'html.parser')
    file = open("result.txt", "a")

    entries = soup.find_all('td')

    # print("Name: " + entries[8].get_text()) # name
    # print("Specialty: " + entries[9].get_text()) # specialty
    # print("Address: " + entries[10].get_text()) # address
    # print("Accepts Medicare: " + entries[13].get_text()) # medicare?
    # print("NPI: " + entries[16].get_text()) # NPI number

    # write to text file
    if "primary-clinics" not in url:
        file.write("Name: " + entries[8].get_text() + '\n') # name
        file.write("Specialty: " + entries[9].get_text() + '\n') # specialty
        file.write("Address: " + entries[10].get_text() + '\n') # address
        file.write("Accepts Medicare: " + entries[13].get_text() + '\n') # medicare?
        file.write("NPI: " + entries[16].get_text() + '\n') # NPI number

    links = get_links(soup, url)
    return links

def main():
    start_url = url
    to_crawl = [start_url]
    crawled = set()
    file = open("result.txt", "w") 

    while to_crawl:
        print(f"Links to scrape: {to_crawl}")
        current_url = to_crawl.pop(0)
        if current_url in crawled:
            continue

        crawled.add(current_url)
        links = crawl(current_url)

        for link in links:
            if link not in crawled and link not in to_crawl:
                to_crawl.append(link)

if __name__ == "__main__":
    main()



