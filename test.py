import  requests,pprint

response = requests.get('http://127.0.0.1/api/mgr/table')

pprint.pprint(response.json())