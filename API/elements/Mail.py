from mailjet_rest import Client
import os
from jinja2 import Template
from dotenv import load_dotenv
import requests 

load_dotenv()

def send(user, password, mail):
  api_key =  os.getenv('api_key')
  api_secret = os.getenv('api_secret')
  mailjet = Client(auth=(api_key, api_secret), version='v3.1')
  
  
  template = Template("""<html>
            <body>
            <p style="font-size:30px;">{{ user }}</p></br></br>
            <h3>A forget password request have been received on your CHEM_API account</h3>
            <br/>
            your password have been reset to:
            <h3><i>{{ newPass }}</i></h3>
            don't forget to change password after login and 
            if you did not initiate this request, please contact us immediately at <a href="/">support.chemAPI.com</a>
            <br/><br/><br/><br/>
            Thank you
            </body>
          </html>""")
          
  data = {
    'Messages': [
      {
        "From": {
          "Email": "noreply.chem.api@gmail.com ",
          "Name": "noreply@chemAPI"
        },
        "To": [
          {
            "Email": mail,
            "Name": ""
          }
        ],
        "Subject": "FORGET PASSWORD",
        "TextPart": "",
        "HTMLPart": template.render(user=user, newPass=password),
        "CustomID": "reset password"
      }
    ]
  }
  request = mailjet.send.create(data=data)
  return request
  

  
  
def validate(mail):
    url = "https://api.apilayer.com/email_verification/{mail}".format(mail=mail)

    payload = {}
    headers= {
      "apikey": os.getenv('key3')
      }

    request = requests.request("GET", url, headers=headers, data = payload)

    return request

  

  
  
  
