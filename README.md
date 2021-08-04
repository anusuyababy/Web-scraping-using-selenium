# Web-scraping-using-selenium
scraping walmart reviews


Assignment:
Write a scraper to scrape product reviews from a Walmart product link. You will need to use Python and Selenium for this task.

Steps to follow:
- Install selenium
- Download chromedriver
- Write scraper code in python, just have a single python file, name it to scraper.py

Link to scrape: 
https://www.walmart.com/ip/Clorox-Disinfecting-Wipes-225-Count-Value-Pack-Crisp-Lemon-and-Fresh-Scent-3-Pack-75-Count-Each/14898365

What should your scraper do?
- open the above url in Google chrome
- scroll down to the review section
- click See All Reviews
- sort reviews by most recent first
- get all review blocks and then certain information (as mentioned below) from each review block
- click the next page and do the same till you see reviews from December 2020
- close the browser and save the file
- everything above should happen programmatically

What information to save in the output file output.csv
- Review date
- Reviewer name
- Review title
- Review body or description
- Rating given by the user

What to submit?
- scraper.py
- output.csv
- readme
