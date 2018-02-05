from bs4 import BeautifulSoup
import requests
import grabber


page_url = "http://www.eng.utoledo.edu/coop/career_expo/companies.html"
response = requests.get(page_url)

soup = BeautifulSoup(response.content, "lxml")

total_jobs = 0
for node in soup.find_all('div'):
    for job_listing in node.find_all('table', class_='fill border company_listing'):
        if "CSE" or "EE" in job_listing.text:
            total_jobs += 1
            for header in job_listing.find_all('table', class_='fill border_bottom company_listing_header'):
                header_text_h = header.find('th').text.lstrip().rstrip()
                header_text_d = header.find('td').text.lstrip().rstrip()

                if header_text_h:
                    print(header_text_h)

                if header_text_d:
                    print(header_text_d)
                    grabber.getScreenShot(header_text_d)

            for body in job_listing.find_all('table', class_='fill company_listing_body'):
                body_location = body.find('td').text.lstrip().rstrip()

                if body_location and not(body_location == ","):
                    print(body_location)

            print()

print(total_jobs)
