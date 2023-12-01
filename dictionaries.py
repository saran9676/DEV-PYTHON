import requests as re
res=re.get('https://api.github.com/repos/kubernetes/kubernetes/pulls')
x=res.json()
for i in range(len(x)):
   print(x[i]['user']['login'])
