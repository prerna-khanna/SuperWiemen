from googlesearch import search
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from textblob import TextBlob
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')
query = ["Karol Bagh Delhi Recent Crime Report","Paschim Vihar Delhi Recent Crime Report","CP Delhi Recent Crime Report", "Hauz Khas Delhi Recent Crime Report", "Dwarka Delhi Recent Crime Report", "Okhla Delhi Recent Crime Report"]
cd = []
for q in query: 
	i = 0 
	x= ""
	for j in search(q, tld="co.in", num=6, stop=1, pause=2): 
		print (j)
		if 'youtube' in j:
			continue
		r = requests.get(j)
		soup = BeautifulSoup(r.content)
		x = x + str(soup) 
		i+=1

	


	print (type(x))
    	#x = x.encode('ascii', 'ignore')
    	tb_msg = TextBlob(x)
    	
    	score = tb_msg.sentiment.polarity
	cd.append(score+0.01)
	print (score)

print cd


q = ['karol bagh','Paschim Vihar','CP','Hauz Khas','Dwarka','Okhla']  
# plotting the points  
width = 1/1.5
plt.bar(q, cd, width, color="blue")
#plt.plot(q,cd) 
  
# naming the x axis 
plt.xlabel('places') 
# naming the y axis 
plt.ylabel('crime density') 
plt.show()
