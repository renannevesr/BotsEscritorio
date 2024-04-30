import requests
import re
from bs4 import BeautifulSoup

url = 'https://cp.trf5.jus.br/cp/cp.do'
myobj = {'tipo': 'xmlrpvprec',
        'filtroRPV_Precatorios': '245999',
         'tipoproc': 'P',
         'ordenacao': 'D'
         }
url_base_prec='https://cp.trf5.jus.br'
 
response = requests.post(url, data=myobj)


if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', href=re.compile('^/processo/'))
    #links = soup.find_all('a', href=True)
    print(links[0]['href'])
    prec_link = links[0]['href']
   # for link in links:
     #   print(link['href'])
    url_prec=url_base_prec+prec_link
    print(url_prec)
    response_prec = requests.get(url_prec)
    print(response_prec.text)
else:
    print("A requisição não foi bem sucedida. Código de status:", response.status_code)