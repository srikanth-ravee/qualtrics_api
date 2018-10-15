import urllib.request #default module for Python 3.X

url = 'https://imentor.ca1.qualtrics.com/API/v3/:collection'
header = {'X-API-TOKEN': 'PF9V9IOkJUMJyHVXp26q0AwoJ5BAUZOIYo2if9eU'}

req = urllib.request.Request(url,None,header) #generating the request object

handler = urllib.request.urlopen(req) #running the request object

print(handler.status) #print status code
print(handler.reason)
