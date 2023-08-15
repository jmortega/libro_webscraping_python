from scrape_linkedin import CompanyScraper

with CompanyScraper() as scraper:
    company = scraper.scrape(company='python')
print(company.to_dict())
