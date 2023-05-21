from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests
 
class handler(BaseHTTPRequestHandler):
  # result = None 
  """
        Handles a GET HTTP request with the 'country' or 'capital' query parameter
        and responds with a string indicating the capital of a country or the country of a capital.
  """
  def do_GET(self):
    s = self.path
    url_components = parse.urlsplit(s)
    query_strings_list = parse.parse_qsl(url_components.query)
    dic = dict(query_strings_list)
    country = dic.get("country")
    capital = dic.get("capital")
    
    if capital:
      url ="https://restcountries.com/v3.1/capital/"
      res = requests.get(url+capital)
      data = res.json()
      res = data[0]["name"]["common"]
      res2 = f"{capital} is the capital of {res}.."
    elif country:
      url ="https://restcountries.com/v3.1/name/"
      res = requests.get(url+country)
      data = res.json()
      res = data[0]["capital"][0]
      res2 = f"The capital of {country} is {res}"

    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(res2.encode('utf-8'))
    return