import requests
url = 'http://jsonplaceholder.typicode.com/photos/100'
response = requests.get(url)
print(response.json())
#print(response.json())
jsonPayload = {'albumId':1,'title':'test','url':'nothing.com','thumbnailUrl':'nothing.com'}
response = requests.put(url,json=jsonPayload)
print(response.json())
