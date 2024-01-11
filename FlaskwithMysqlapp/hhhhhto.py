>>> from urllib.request import urlopen
>>> from pprint import pprint
>>> with urlopen("https://www.example.com") as response:
...     pprint(dir(response))
...
