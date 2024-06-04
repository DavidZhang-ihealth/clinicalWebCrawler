# Medicare List Web Crawler - How to Run

## Prerequisites
Python, pip, BeautifulSoups4, requests

## On MacOS
Simply run `./run.sh` in terminal and enter the URL you would like to scrape once prompted.

## On Windows (not quite sure)
Run the following commands in order
```
pip install virtualenv
python -m venv env
env\Scripts\activate
pip install requests
pip install bs4
python web_crawler.py
```

## Deactivating environment
Simply run `deactivate` in terminal