import re
import urllib

import bs4

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html)
spans = soup('span')
numbers = []
for span in spans:
    numbers.append(int(span.string))
print (sum(numbers))