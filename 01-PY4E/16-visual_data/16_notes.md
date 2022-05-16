__Course:__ Python 4 Everybody
__Instructor:__ Charles Severance
__Source:__ n/a
__Student:__ surge55
__Book:__ Python for Everybody
__Author:__ Charles Severance


# Chapter 16 Notes
## Visualizing Data



From Lecture

--------------------



## Retrieving and Visualizing Data

Multi-Step Data Analysis

Source --> Gather Data --> Crawl --> Raw Data --> Clean up the Data --> Visualize / Analyze



## Many Data Mining Technologies

- hadoop.apache.org
- spark.apache.org
- aws.amazon.com/redshift
- community.pentaho.com



## "Personal Data Mining"  

- Our goal is to make you better programmers - not to make you data mining experts



## GeoData

- Makes a Google Map from users entered data
- Uses the Google Geodata API
- Caches data in a database to avoid rate limiting and allow restarting
- Visualized in a browser using the Google Maps API



## Page Rank

- Write a simple web page crawler
- Compute a simple version of Google's Page Rank algorithm
- Visualize the resulting network



## Search Engine Architecture

- Web Crawling
- Index Building
- Searching



## Web Crawler

- Is a computer program that browses the web in a methodical, automated manner. Web crawlers are mainly used to create a copy of all the visited pages for later processing by a search engine that will index the downloaded pages to provide fast searches.
- Steps to a web crawler:
  - Retrieve a page
  - Look through the page for links
  - Add the links to a list of "to be retrieved" sites
  - Repeat...



## Web Crawling Policy

- A **selection policy** that states which pages to download
- A **re-visit policy** that states when to check for changes to the pages
- A **politeness policy** that states how to avoid overloading web sites
- A **parallelization policy** that states how to coordinate distributed web crawlers



## robots.txt

- A way for a website to communicate with web crawlers
- An informal and voluntary standard
- Sometimes folks make a "spider trap" to catch "bad" spiders



## Index Building

- Uses the page rank algorithm
- Determining the value of links and how many links
- Search Indexing
  - Search engine indexing collects, parses, and stores data to facilitate fast and accurate information retrieval. The purpose of storing an index is to optimize speed and performance in finding relevant documents for a search query. Without an index, the search engine would scan every document in the corpus, which would require considerable time and computing power.

