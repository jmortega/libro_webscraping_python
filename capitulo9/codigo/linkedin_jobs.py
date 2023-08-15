import requests
from bs4 import BeautifulSoup
import math
import pandas as pd

jobslist=[]


headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}

target_url='https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Python%20%28Programming%20Language%29&currentJobId=3415227738&start={}'

for i in range(0,math.ceil(117/25)):

    response = requests.get(target_url.format(i))
    soup=BeautifulSoup(response.text,'html.parser')
    alljobs_on_this_page=soup.find_all("li")
    for x in range(0,len(alljobs_on_this_page)):
        jobid = alljobs_on_this_page[x].find("div",{"class":"base-card"}).get('data-entity-urn').split(":")[3]
        jobslist.append(jobid)

target_url='https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{}'

jobs=[]

for j in range(0,len(jobslist)):

    response = requests.get(target_url.format(jobslist[j]))
    soup=BeautifulSoup(response.text,'html.parser')
    job={}

    try:
        job["company"]=soup.find("div",{"class":"top-card-layout__card"}).find("a").find("img").get('alt')
    except:
        job["company"]=None

    try:
        job["job-title"]=soup.find("div",{"class":"top-card-layout__entity-info"}).find("a").text.strip()
    except:
        job["job-title"]=None

    try:
        job["level"]=soup.find("ul",{"class":"description__job-criteria-list"}).find("li").text.replace("Seniority level","").strip()
    except:
        job["level"]=None

    jobs.append(job)
    
print(jobs)

