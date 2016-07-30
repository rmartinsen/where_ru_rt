import requests
import re

url = 'http://m.sacrt.com/bdetails.aspx?stpid=1788&route=38'
pattern = r'Vehicle [0-9]+ arriving in ([0-9]+) minutes'

html = requests.get(url).text

matches = re.search(pattern, html)

print(matches.group(0))



