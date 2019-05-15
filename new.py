import urllib.request
import csv
import sys
import io
import pandas as pd
from functools import reduce

url = "https://data.cityofnewyork.us/Public-Safety/FDNY-Line-Of-Duty-Deaths/32y8-s55cs/data.csv" \
    "?accessType=DOWNLOAD"

try:
    fileFromUrl = urllib.request.urlopen(url)
except urllib.error.URLError as error:
    print("urllib.error.URLError", error)
    sys.exit(1)

sequenceOfBytes = fileFromUrl.read() #Read whole file into one big sequenceOfBytes.
fileFromUrl.close()

try:
    s = sequenceOfBytes.decode("utf-8")    #s is a string
except UnicodeError as unicodeError:
    print(unicodeError)
    sys.exit(1)


fileFromString = io.StringIO(s)
df = pd.read_csv(fileFromString, dtype = {'str'})  #reads in fileFromString as DataFrame
fileFromString.close()

deaths=[
    "Rank",
    "Name",
    "Unit",
    "Date"
    ]

deaths.drop(columns=deaths, inplace=True)

print("FDNY NY DEATHS")
print()
print("Rank")
print()
print("Name")
print()
print("Unit")
print()
print("Date")


sys.exit(0)
