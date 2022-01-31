# Import packages
import requests
from bs4 import BeautifulSoup
import lxml
import pandas as pd

# Assign the URL of interest
url = 'https://en.wikipedia.org/wiki/List_of_Asian_countries_by_area'

# Package the request, send the request and catch the response
r = requests.get(url)

# Extract the response as a html
html_doc = r.text

# Create a BeautifulSoup object from the html
soup = BeautifulSoup(html_doc, 'lxml')

# Print the title of the webpage
print(soup.title)

<title>List of Asian countries by area - Wikipedia</title>

# Prettify the BeautifulSoup object
soup_prettify = soup.prettify()

# Create a table variable to get information from the table of the list of Asian Countries
table = soup.find('table', {'class':'wikitable sortable'})

# Extract the title (country names) from the table information
countries_name = []
for links in table.findAll('a'):
    countries_name.append(links.get('title'))
    print(countries_name)
 
# Create a DataFrame storing a list of Asian countries and print the result
df = pd.DataFrame()
df['Country'] = countries_name
print(df)

           Country
0            Russia
1   European Russia
2              None
3             China
4            Taiwan
..              ...
71       Gaza Strip
72           Brunei
73          Bahrain
74        Singapore
75         Maldives
