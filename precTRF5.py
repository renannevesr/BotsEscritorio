import requests
import re
from bs4 import BeautifulSoup
import html

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
    response_prec_raw = requests.get(url_prec)
    response_prec=html.unescape(response_prec_raw.text)
    print(response_prec)
    soup = BeautifulSoup(response_prec, 'html.parser')

    reqte_td = soup.find_all('td')[17].get_text(strip=True)
    proc_origin_td = soup.find_all('td')[3].get_text(strip=True)
    precatorio_td = soup.find_all('td')[0].get_text(strip=True)
    autuado_td = soup.find_all('td')[1].find('div', align='right').get_text(strip=True)

    # Imprimindo as informações
    print("REQTE:", reqte_td)
    print("PROC. ORIGINÁRIO Nº:", proc_origin_td)
    print("PRECATÓRIO:", precatorio_td)
    print("AUTUADO EM:", autuado_td)
else:
    print("A requisição não foi bem sucedida. Código de status:", response.status_code)