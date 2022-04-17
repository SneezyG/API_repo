from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import json
import os
from dotenv import load_dotenv
# import sentry_sdk
import functools

load_dotenv()

@functools.lru_cache
def load_data():
  # read the csv file and return the data
  data = pd.read_csv(os.getenv('file'))
  data.index = list(data.element)
  return data
  



# home view
def index(request):
  return render(request, 'elements/index.html')
  
# guild view
def guide(request):
  return render(request, 'elements/guild.html')

# API view with logging.
def data(request, element):
  data = load_data()
  try:
    data = data.loc[element, :]
  except:
    return HttpResponse("not found", status=404)
  
 
  # convert data to json format
  data = data.to_json(orient='index')
  parsed_data = json.loads(data)
  data = json.dumps(parsed_data, indent = 4)
  
  return HttpResponse(data, content_type='application/json')


"""
#setup error reporting service
sentry_sdk.init(
  
    "https://295b206a88da4811906270f529e0b5dd@o1188216.ingest.sentry.io/6308170",
    
    traces_sample_rate=1.0
)
"""