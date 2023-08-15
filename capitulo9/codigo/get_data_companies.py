from scrape_linkedin import scrape_in_parallel, CompanyScraper

companies = ['google', 'amazon']

#Scrape all companies, output to 'companies.json' file, use 2 browser instances
scrape_in_parallel(
    scraper_type=CompanyScraper,
    items=companies,
    output_file="companies.json",
    num_instances=2
)
