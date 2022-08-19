import requests
import json


def rest():
  
  """
  this will test the restAPI using the python request module.
  
  it will be testing three data endpoint, The apiview, modelviewset and the absolute url generated for individual item.
  
  this is all through the GET request method
  """
  
  
  # modelviewset
  particles = requests.get("http://127.0.0.1:8000/rest/particle")
  
  
  # absolute url
  tenthElement = requests.get("http://127.0.0.1:8000/rest/element/10")
  
  
  # apiview
  calcium = requests.get("http://127.0.0.1:8000/element/Calcium")
  
  
  print("particles: \n", json.dumps(particles.json(), indent=2), "\n")
  print("tenthElement: \n", json.dumps(tenthElement.json(), indent=2), "\n")
  print("calcium: \n", json.dumps(calcium.json(), indent=2), "\n")
  
 


def graphql():
  
  """
  this will test the graphene data endpoint.
  """
  
  query = '''
      {
          element(name: "Neon") {
            atomicNo
            symbol
            atomicMass
            period
            group
            kind,
            discoverer
            year
          }
      
      }
      '''


  
  neon = requests.get("http://127.0.0.1:8000/graphql", params={"query": query})
  
  print("neon: \n", json.dumps(neon.json(), indent=2), "\n")
 
 
  
rest() 
graphql()
  
  