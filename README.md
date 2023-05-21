## SCRAP-GLASSDOOR_WEBSITE
Scrap data from [Glassdoor](https://www.glassdoor.co.in/) Website by the help of Beautiful Soup.

## WEB SCRAPING :
Web scraping is the process of gathering information from the Internet.However, the words “web scraping” usually refer to a process that involves automation.
Some websites don’t like it when automatic scrapers gather their data, while others don’t mind.
If you’re scraping a page respectfully for educational purposes, then you’re unlikely to have any problems.
Still, it’s a good idea to do some research on your own and make sure that you’re not violating any Terms of Service before you start a large-scale project.

## SCRAP HTML CONTENT FROM A PAGE :
First, you’ll want to get the site’s HTML code into your Python script so that you can interact with it.
For this task, you’ll use Python’s `requests` library.
```
pip install requests
```
### Retrive HTML code :
``` python
import requests

headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
url='https://www.glassdoor.co.in/Explore/browse-companies.html?'
webpage=requests.get(url,headers=headers).text
```
### if response code is 403 :
- headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
- requests.get('url',headers=headers).text

## PARSE HTML CODE WITH BEAUTIFUL SOUP :
Beautiful Soup is a Python library for parsing structured data.
It allows you to interact with HTML in a similar way to how you interact with a web page using developer tools. 
Install Beautiful Soup ->
```
 pip install beautifulsoup4

```
###  import the library in your Python script and create a Beautiful Soup object :
```python
soup=BeautifulSoup(webpage, 'lxml')
```
### Find the dataset in `csv` format [here](https://github.com/RinaProg/SCRAP-GLASSDOOR_WEBSITE/tree/master/list_of_company_dataset)

## STEPS FOR SCRAPING ANY WEBSITE :
- Step 1: Step through a web scraping pipeline from start to finish.
- Step 2: Inspect the HTML structure of your target site with your browser’s developer tools.
- Step 3: Decipher the data encoded in URLs.
- Step 4: Get the HTML content using Python’s requests library.
- Step 5: Parse the HTML with Beautiful Soup to extract relevant information
- Step 6: Build a script that fetches all data from the Web and displays relevant information in your console.

## COMMENT :
In this Project,how to scrape data from the Web using Python, requests, and Beautiful Soup.Built a script that fetches data from the Internet and went through the complete web scraping process from start to finish.
Hope you all like this documentation and you can suggest me if there would be any sutiable modification required.
Thank you 😊
