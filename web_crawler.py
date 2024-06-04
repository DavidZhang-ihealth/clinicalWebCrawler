import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = 'https://www.medicarelist.com/primary-clinics/ca/'
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
                if "Home" in a_tag.get_text() or "Disclaimer" in a_tag.get_text() or "Privacy Policy" in a_tag.get_text():
                    continue
                href = a_tag['href']
                full_url = urljoin(base_url, href)
                links.append(full_url)
    print(links)
    return links

def crawl(url):
    print(f"Scraping URL: {url}")
    html_content = fetch_html(url)
    soup = BeautifulSoup(html_content, 'html.parser')

    entries = soup.find_all('td')
    for (e, entry) in enumerate(entries):
        print(e, entry.get_text())

    
    links = get_links(soup, url)
    return links

def main():
    start_url = url
    to_crawl = [start_url]
    crawled = set()

    while to_crawl:
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



