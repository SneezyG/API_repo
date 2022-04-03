from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import json
import os
from dotenv import load_dotenv

load_dotenv()

# home view
def index(request):
  return render(request, 'elements/index.html')
  
# guild view
def guide(request):
  return render(request, 'elements/guild.html')

# API view with logging.
def data(request, element):
  
  # read the csv file
  data = pd.read_csv(os.getenv('file'))
  
  # create an index using the element column
  data.index = list(data.Element)
  data = data.loc[element, :]
  
  # convert data to json format
  data = data.to_json(orient='index')
  parsed_data = json.loads(data)
  data = json.dumps(parsed_data, indent = 4)
  
  return HttpResponse(data)

