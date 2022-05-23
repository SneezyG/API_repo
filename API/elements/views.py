from django.shortcuts import render
from django.http import HttpResponse
from dotenv import load_dotenv
# import sentry_sdk

load_dotenv()


# home view
def index(request):
  return render(request, 'elements/index.html')
  
# guild view
def guide(request):
  return render(request, 'elements/guild.html')

# API view with logging.
def data(request, element):
  pass
  


"""
#setup error reporting service
sentry_sdk.init(
  
    "https://295b206a88da4811906270f529e0b5dd@o1188216.ingest.sentry.io/6308170",
    
    traces_sample_rate=1.0
)
"""