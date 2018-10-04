from googlesearch import search
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

query = ["Karol Bagh Delhi Crime Rate","Paschim Vihar Delhi Crime Rate","CP Delhi Crime Rate"]
cd = []
for q in query: 
	i = 0 
	x= []
	
	for j in search(q, tld="co.in", num=6, stop=1, pause=2): 
		print (j)
		if 'youtube' in j:
			continue
		r = requests.get(j)
		soup = BeautifulSoup(r.content)
		x.append(soup)
		i+=1

	l=[]
	l=str(x).split()
	wordfreq=[l.count(p) for p in l]
	d = dict(zip(l,wordfreq))
	if 'rape' not in d:
		d['rape'] = 0
	if 'violence' not in d:
		d['violence'] = 0
	if 'molestation' not in d:
		d['molestation'] = 0
	if 'abuse' not in d:
		d['abuse'] = 0
	if 'murder' not in d:
		d['murder'] = 0
	if 'rape' in d or 'violence'in d or 'molestation' in d or 'abuse' in d or 'murder' in d:
		temp = d['rape'] + d['violence'] + d['molestation'] + d['abuse'] + d['murder']
		print (d['rape'])
	else:
		temp = 0
		print '0'
	cd.append(temp)

print cd


q = ['karol bagh','Paschim Vihar','CP']  
# plotting the points  
plt.plot(q,cd) 
  
# naming the x axis 
plt.xlabel('places') 
# naming the y axis 
plt.ylabel('crime density') 
plt.show()
