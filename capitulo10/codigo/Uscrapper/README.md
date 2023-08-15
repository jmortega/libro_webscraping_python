<h1 align="center" id="title">Uscrapper 2.0</h1><br>

<p align="center"><img src="https://socialify.git.ci/z0m31en7/Uscrapper/image?font=Source%20Code%20Pro&amp;name=1&amp;owner=1&amp;pattern=Plus&amp;theme=Dark" alt="project-image"></p><br>

<p id="description" align="justify">Introducing Uscrapper 2.0,  A powerfull OSINT webscrapper that allows users to extract various personal information from a website. It leverages web scraping techniques and regular expressions to extract email addresses, social media links, author names, geolocations, phone numbers, and usernames from both hyperlinked and non-hyperlinked sources on the webpage, supports multithreading to make this process faster, Uscrapper 2.0 is equipped with advanced Anti-webscrapping bypassing modules and supports webcrawling to scrape from various sublinks within the same domain. The tool also provides an option to generate a report containing the extracted details. </p><br><br>

<p align="center"><img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&amp;logo=linux&amp;logoColor=black" alt="shields"><img src="https://img.shields.io/badge/tmux-1BB91F?style=for-the-badge&amp;logo=tmux&amp;logoColor=white" alt="shields"><img src="https://img.shields.io/badge/windows%20terminal-4D4D4D?style=for-the-badge&amp;logo=windows%20terminal&amp;logoColor=white" alt="shields"><img src="https://img.shields.io/badge/iTerm2-000000?style=for-the-badge&amp;logo=iterm2&amp;logoColor=white" alt="shields"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&amp;logo=python&amp;logoColor=white" alt="shields"></p><br><br>

<p align="center"><img src="https://lh3.googleusercontent.com/drive-viewer/AITFw-yL2zYKX1yEZPYLPK5brCOz_jSMLH1ilEPi7jeSAv0XUIbkf4ardW0pflUV7ltxpqppYrmdOt5NWf24PjpgqxkE1zBl=s1600" alt="project-logo"></p><br>
  
<h2>💡 Extracted Details:</h2><br>

Uscrapper extracts the following details from the provided website:

*   Email Addresses: Displays email addresses found on the website.
*   Social Media Links: Displays links to various social media platforms found on the website.
*   Author Names: Displays the names of authors associated with the website.
*   Geolocations: Displays geolocation information associated with the website.
*   Non-Hyperlinked Details: Displays non-hyperlinked details found on the website including email addresses phone numbers and usernames.

<br><h2>📽 Preview:</h2><br>

<p align="center"><img src="https://lh3.googleusercontent.com/drive-viewer/AITFw-y-7PS48iC0sU2HPSjlBanpM4RPKJn3GGmmnFYmqZ5PqLyLvO4aefDzqITpO52fPwY5FH8y4stik_yYVW_RzsnlipDUxg=s2560" alt="project-ss"></p><br>
<p align="center"><img src="https://lh3.googleusercontent.com/drive-viewer/AITFw-x6V0zw3mgqnBcvKlWRLYvNQvjusTk-nvLeXCp3GmECsYLeibxnSCFJtqYt50OG1YVwPU22T1Q6FXRGdTBRe2mh4ne8Kw=s1600" alt="project-ss2"></p>

<h2>🤩 Whats New?:</h2>

Uscrapper 2.0:

*   Introduced multiple modules to bypass anti-webscrapping techniques.
*   Introducing Crawl and scrape: an advanced crawl and scrape module to scrape the websites from within.
*   Implemented Multithreading to make these processes faster. 

<h2>🛠️ Installation Steps:</h2><br>

```
git clone https://github.com/z0m31en7/Uscrapper.git
```
```
cd Uscrapper/install/ 
chmod +x ./install.sh && ./install.sh      #For Unix/Linux systems
```

<br><h2>🔮 Usage:</h2>

<p>To run Uscrapper, use the following command-line syntax:</p>

```
python Uscrapper.py [-h] [-u URL] [-c (INT)] [-t THREADS] [-O] [-ns]
```
<br><b>Arguments:</b>

* -h, --help: Show the help message and exit.
* -u URL, --url URL: Specify the URL of the website to extract details from.
* -c INT, --crawl INT: Specify the number of links to crawl
* -t INT, --threads INT: Specify the number of threads to use while crawling and scraping.
* -O, --generate-report: Generate a report file containing the extracted details.
* -ns, --nonstrict: Display non-strict usernames during extraction.

<br><h2>📜 Note:</h2>
* Uscrapper relies on web scraping techniques to extract information from websites. Make sure to use it responsibly and in compliance with the website's terms of service and applicable laws.

* The accuracy and completeness of the extracted details depend on the structure and content of the website being analyzed.

* To bypass some Anti-Webscrapping methods we have used selenium which can make the overall process slower.

<br><h2>💌 Contribution:</h2><br>
<b>Want a new feature to be added?</b><br>
* Make a pull request with all the necessary details and it will be merged after a review.
* You can contribute by making the regular expressions more efficient and accurate, or by suggesting some more features that can be added.

<h2>🛡️ License:</h2><br>
This project is licensed under the <a href="https://github.com/z0m31en7/Uscrapper/blob/main/LICENSE">MIT-LICENSE</a><br><br>
