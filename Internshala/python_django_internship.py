from bs4 import BeautifulSoup
import pandas as pd
import requests
from openpyxl.workbook import Workbook

r = requests.get("https://books.toscrape.com")

    # Create a BeautifulSoup object and specify the parser
soup = BeautifulSoup(r.text, 'html.parser')
  # Find all the books on the page
books = soup.find_all('article', class_='product_pod')

    # Initialize empty list for storing book details
book_details = []

    # Iterate through each book and get details

       

job_title = []
company_name=[]
location=[]
start_date=[]
duration=[]
stipends=[]
posted_on=[]
apply_by=[]


df = pd.DataFrame({'Job title':job_title,'Company name':company_name,'loaction':location,'start date':start_date,'Duration':duration,'stipends':stipends,'posted on':posted_on,'apply by':apply_by}) 
df.to_excel('keyword_internship.xlsx', index=False, encoding='utf-8')
