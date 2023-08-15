from autoscraper import AutoScraper

url = 'https://stackoverflow.com/questions/2081586/web-scraping-with-python'

# We can add one or multiple candidates here.
# You can also put urls here to retrieve urls.
wanted_list = ["What are metaclasses in Python?"]

scraper = AutoScraper()
result = scraper.build(url, wanted_list)
print(result)

result = scraper.get_result_similar('https://stackoverflow.com/questions/2081586/web-scraping-with-python')
print(result)

url = 'https://github.com/alirezamika/autoscraper'

wanted_list = ['A Smart, Automatic, Fast and Lightweight Web Scraper for Python', '2.5k', 'https://github.com/alirezamika/autoscraper/issues']

scraper = AutoScraper()
result = scraper.build(url, wanted_list)
print(result)
