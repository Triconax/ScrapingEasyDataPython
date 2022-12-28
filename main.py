import requests
from bs4 import BeautifulSoup
import pandas as pd
url = 'http://quotes.toscrape.com/page/1/'
response = requests.get(url)
page_contents = response.text
doc = BeautifulSoup(page_contents,'html.parser')
print(response.status_code)
span_tags = doc.find_all('span',{'class':'text'})
##print(len(span_tags))
##A loop which seperates the quotes which we want and puts it in a list
quotes = []
for tag in span_tags:
    quotes.append(tag.text)
    
##print(quotes)

small_tags = doc.find_all('small')

##A loop which seperates the author names which we want and puts it in a list
author_names = []
for tag in small_tags:
    author_names.append(tag.text)
##print(author_names)

##Create a dict and put in the list names which we created
dict = {'QUOTES_LIST' : quotes,
        'AUTHORS_LIST': author_names}

##Creates the data frame
table_df = pd.DataFrame(dict)

print(table_df)
##Converts to a csv file
table_df.to_csv('table_df.csv', index=None)



