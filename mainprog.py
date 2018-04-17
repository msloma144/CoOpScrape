from bs4 import BeautifulSoup
import requests
import grabber
import threading, time
from Queue import Queue

websites = Queue()


def get_websites():
    page_url = "http://www.eng.utoledo.edu/coop/career_expo/companies.html"
    response = requests.get(page_url)

    soup = BeautifulSoup(response.content, "lxml")

    total_jobs = 0

    for node in soup.find_all('div'):
        for job_listing in node.find_all('table', class_='fill border company_listing'):
            if "CSE" or "EE" in job_listing.text:
                total_jobs += 1
                for header in job_listing.find_all('table', class_='fill border_bottom company_listing_header'):
                    name = header.find('th').text.lstrip().rstrip()
                    website = header.find('td').text.lstrip().rstrip()

                    if name:
                        print(name)

                    if website:
                        print(website)
                        websites.put(website)
                        #grabber.getScreenShot(website)

                for body in job_listing.find_all('table', class_='fill company_listing_body'):
                    body_location = body.find('td').text.lstrip().rstrip()

                    if body_location and not(body_location == ","):
                        print(body_location)

                print()


def work_queue():
    while not websites.empty():
        grabber.getScreenShot(websites.get())


get_websites()
threads = []
MAX_THREADS = 10
count = 0
for i in range(0, MAX_THREADS):
    t = threading.Thread(target=work_queue)
    t.start()

