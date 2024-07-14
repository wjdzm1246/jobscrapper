import requests
from bs4 import BeautifulSoup




class job_scrapper:
    def __init__(self):
        #self.keywords = keywords

        #for keyword in keywords:
        #jobs_db = self.job_scrapper(keyword)
        #self.save_data_inFile(keyword, jobs_db)
        self.all_jobs = []

    def set_job(self, jobs):
      for job in jobs:
        title = job.find("h2").text.strip()
        company = job.find("h3").text.strip()
        region = job.find("div", class_="location").text
        url = job.find("a")["href"]

        print(title)
        print(company)
        job_data = {
          "title": title,
          "company": company,
          "region": region,
          "link": f"https://remoteok.com{url}"
        }
        self.all_jobs.append(job_data) 

    def scrapping(self, keyword):
        
        print(f"Scrapping {keyword}...")
        url = f"https://remoteok.com/remote-{keyword}-jobs"
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"})
        soup = BeautifulSoup(response.text, "html.parser")

        jobs = soup.find_all("td", class_="company position company_and_position")[1:]

        self.set_job(jobs)
        return self.all_jobs
