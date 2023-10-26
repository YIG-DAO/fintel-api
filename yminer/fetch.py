from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

session = Session()

def yeetPayload(url, parameters, headers):
  try:
    session.headers.update(headers)
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    payload = data['data']
    return payload
  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
    return e