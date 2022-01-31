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
0 	Russia
1 	China
2 	Hong Kong
3 	Macau
4 	India
5 	None
6 	Kazakhstan
7 	Saudi Arabia
8 	Iran
9 	Mongolia
10 	Indonesia
11 	Pakistan
12 	Gilgit-Baltistan
13 	Azad Kashmir
14 	Turkey
15 	Myanmar
16 	Afghanistan
17 	Yemen
18 	Thailand
19 	Turkmenistan
20 	Uzbekistan
21 	Iraq
22 	Japan
23 	Vietnam
24 	Malaysia
25 	Oman
26 	Philippines
27 	Laos
28 	Kyrgyzstan
29 	Syria
30 	Golan Heights
31 	Cambodia
32 	Bangladesh
33 	Nepal
34 	Tajikistan
35 	North Korea
36 	South Korea
37 	Jordan
38 	Azerbaijan
39 	United Arab Emirates
40 	Georgia (country)
41 	Sri Lanka
42 	Egypt
43 	Bhutan
44 	Taiwan
45 	Armenia
46 	Israel
47 	Kuwait
48 	East Timor
49 	Qatar
50 	Lebanon
51 	Cyprus
52 	Northern Cyprus
53 	State of Palestine
54 	Brunei
55 	Bahrain
56 	Singapore
57 	Maldives
