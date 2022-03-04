# Import libraries
import os
import sys

# Allow imports from src folder
module_path = os.path.abspath(os.path.join('../src'))
if module_path not in sys.path:
    sys.path.append(module_path)

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from dateutil import tz
from pandas.tseries.offsets import MonthEnd
from sklearn.preprocessing import MinMaxScaler
import itertools

import math
import numpy as np
import pandas as pd
import fasttrack as ft
import greyhoundracinguk as gh

from dotenv import load_dotenv

#def main():
load_dotenv()

#api_key = os.getenv('FAST_TRACK_API_KEY', os.environ['FAST_TRACK_API_KEY'])
#client = ft.Fasttrack(api_key)
#track_codes = client.getResults()
client = gh.Greyhoundracinguk(os.environ['x-rapidapi-key'])
#client.getResults("2022-03-01")
#client.getRacecards("2021-03-01")
client.getRaceDetails()

#conn.request("GET", "/results", headers=headers)

#res = conn.getresponse()
#data = res.read()

#print(data.decode("utf-8"))


#conn.request("GET", "/racecards", headers=headers)

#res = conn.getresponse()
#data = res.read()

#print(data.decode("utf-8"))

#conn.request("GET", "/race/53128", headers=headers)

#res = conn.getresponse()
#data = res.read()

#print(data.decode("utf-8"))

#import requests

#url = "https://greyhound-racing-uk.p.rapidapi.com/results"

#querystring = {"date":"2021-06-02"}

#response = requests.request("GET", url, headers=headers, params=querystring)

#print(response.text)
      
#import json

#print(json.dumps(response.text, indent=2
