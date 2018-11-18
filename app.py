from flask import Flask
import json

app = Flask(__name__)

import json, requests
url = 'https://api.foursquare.com/v2/venues/explore'

@app.route('/')
def hello():
  params = dict(
    client_id='F22SZ5OH34NV0ETPBQCJ33UIJGFMDWNMTI0MVUABYPJECIBW',
    client_secret='GTWA3CFSP1Y5PMUNJTWKFOS3QJELCNHRMBOASKL4UDGKYJAK',
    v='20181118',
    suggestedRadius='6000',
    ll='40.7243,-74.0018',
    query='thai',
    limit=100
  )

  resp = requests.get(url=url, params=params)
  data = json.loads(resp.text)

  # print(data)
  return json.dumps(data)


if __name__ == '__main__':
    app.run()
