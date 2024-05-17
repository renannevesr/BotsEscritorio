import requests
import re
from bs4 import BeautifulSoup
import html
from APISheets import read, write

url = 'https://cp.trf5.jus.br/cp/cp.do'
url_base_prec='https://cp.trf5.jus.br'
def formatar_numero(numero):
    return f"{numero[:7]}-{numero[7:9]}.{numero[9:13]}.{numero[13:14]}.{numero[14:16]}.{numero[16:]}"


while True:
    last_prec = int(read()) + 1
    print(last_prec)
    myobj = {'tipo': 'xmlrpvprec',
            'filtroRPV_Precatorios': f'{last_prec}',
            'tipoproc': 'P',
            'ordenacao': 'D'
            } 
    response = requests.post(url, data=myobj)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=re.compile('^/processo/'))
        
        #print(links[0]['href'])
        prec_link = links[0]['href']
        url_prec=url_base_prec+prec_link
        #print(url_prec)
        response_prec_raw = requests.get(url_prec)
        response_prec=html.unescape(response_prec_raw.text)
        #print(response_prec)
        soup = BeautifulSoup(response_prec, 'html.parser')

        reqte_td_raw = soup.find_all('td')[17].get_text(strip=True)
        reqte_td = re.sub(r'^:\s*', '', reqte_td_raw)
        adv_td_raw = soup.find_all('td')[18].get_text(strip=True)
        if adv_td_raw =='REQDO':
            reqte_adv_td = 'SEM ADV CADASTRADO NO PREC'
        else: 
            reqte_adv_td_raw = soup.find_all('td')[19].get_text(strip=True)
            reqte_adv_td = re.sub(r'^:\s*', '', reqte_adv_td_raw)
        proc_origin_td_raw = soup.find_all('td')[3].get_text(strip=True)
        print(proc_origin_td_raw)
        regex_tribunal = r'- (.*)$'
        regex_numero_processo = re.findall(r'\d+', proc_origin_td_raw)
        numero_processo_match = ''.join(regex_numero_processo)
        print(numero_processo_match)
        numero_processo = formatar_numero(numero_processo_match)
        print(numero_processo)
        tribunal_match = re.search(regex_tribunal, proc_origin_td_raw)
        if tribunal_match:
            tribunal = tribunal_match.group(1)
        else:
            tribunal = None
        precatorio_td_raw = soup.find_all('td')[0].get_text(strip=True)
        regex_numeros = r'\d+'
        num = re.findall(regex_numeros, precatorio_td_raw)
        precatorio_td=[int(numero) for numero in num]
        precatorio_td= ', '.join(map(str, precatorio_td))
        autuado_td_raw = soup.find_all('td')[1].find('div', align='right').get_text(strip=True)
        autuado_td = autuado_td_raw.replace("AUTUADO EM ", "")
        info_prec = {
        "REQTE": reqte_td,
        "ADV": reqte_adv_td,
        "PROC. ORIGINÁRIO Nº": numero_processo,
        "TRIBUNAL": tribunal,
        "PRECATÓRIO": precatorio_td,
        "AUTUADO EM": autuado_td
    }
        write(info_prec)

    else:
        print("A requisição não foi bem sucedida. Código de status:", response.status_code)