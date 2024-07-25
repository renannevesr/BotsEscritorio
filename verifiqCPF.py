import time
import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def calcular_data_nascimento(entrada):
    partes = entrada.split()
    anos = int(partes[0].replace('.a', ''))
    meses = int(partes[1].replace('.m', ''))
    dias = int(partes[2].replace('.d', ''))

    data_atual = datetime.now()

    data_nascimento = data_atual - relativedelta(years=anos, months=meses) - timedelta(days=dias)
    
    return data_nascimento.strftime("%d/%m/%Y")

def extrair_miolo(cpf):
    numeros = re.sub(r'\D', '', cpf)
    print(numeros)

    return numeros[3:9] if len(numeros) >= 9 else numeros

url = 'https://armoney.panoramaemprestimos.com.br'

login = 'rego&quintino02'
senha = '203040'
list_b = 'lista.csv'
lista = []
df_b = pd.read_csv(list_b)

print(df_b.head())
rows = df_b.shape[0]

driver = webdriver.Chrome()

driver.get(url)
time.sleep(1)
driver.find_element("xpath", '//*[@id="usuario_id_campo"]').send_keys(login)
driver.find_element("xpath", '//*[@id="senha_id_campo"]').send_keys(senha)
time.sleep(2)
driver.find_element("xpath", '/html/body/div[1]/form/div/div[4]/a').click()
driver.find_element("xpath", '//*[@id="ui-id-1"]').click()
time.sleep(1)

for i in range(rows):
    try:
        len_pesquisa = 0
        ausencia = 0
        quantidade = 0
        dados = 0
        lista.clear()
        nome = df_b.loc[i, 'nome']
        cpf1 = df_b.loc[i, 'cpf']
        miolo_cpf1 = extrair_miolo(cpf1)
        time.sleep(1)
        driver.find_element("xpath", '//*[@id="ui-id-2"]/a[1]').click()
        # Store iframe web element
        iframe = driver.find_element(By.XPATH, '//*[@id="id_execucao"]')
        # Switch to selected iframe
        driver.switch_to.frame(iframe)
        if i == 0:
            driver.find_element("xpath", '//*[@id="lk_nomeCpf_cons"]').click()
        try:
            driver.find_element("xpath", '//*[@id="pnl_nomeCpf_cons"]/table/tbody/tr/td[2]/obrigatorio/input').send_keys(nome)
            driver.find_element("xpath", '//*[@id="id_listar"]').click()
            time.sleep(1)
            try:
                ausencia = driver.find_elements(By.CLASS_NAME, 'msg_aviso')
            except:
                print("entrou no try de msg_aviso")
                pass
            if ausencia != 0:
                df_b.loc[i, 'CPF'] = "nao_CPF"
            try:
                quantidade = driver.find_elements(By.CLASS_NAME, 'msg_aviso')
            except:
                pass
            try:
                dados = driver.find_elements(By.CLASS_NAME, 'lit')
                tam_dados = len(dados)
                idx_dados = 0
                for e in dados:
                    idx_dados += 1
            except:
                print("entrou try dados")
                pass
            if 1 < tam_dados < 3:
                time.sleep(2)
                cpf_site= driver.find_element("xpath", '/html/body/div[1]/div[8]/div/table[1]/tbody/tr[2]/td[5]').text
                miolo_cpf2 = extrair_miolo(cpf_site)
                try:
                    df_b.loc[i, 'CPF'] = cpf_site
                except:
                    df_b.loc[i, 'CPF'] = "vazio"
                    
            if tam_dados >= 4:
                print("entrou if tam")
                registro_raw = driver.find_element("xpath", '//*[@id="barra_paginacao"]/tbody/tr/td[2]').text
                print("resgistro 1")
                registro = int(re.search(r'\d+', registro_raw).group())
                print("entrou 2 if")
                print(registro)
                for tr in range (2,22): 
                    cpf_site =driver.find_element("xpath", f'/html/body/div[1]/div[8]/div/table[1]/tbody/tr[{tr}]/td[5]').text
                    miolo_cpf2 = extrair_miolo(cpf_site)
                    if miolo_cpf1 == miolo_cpf2:
                        try:
                            df_b.loc[i, 'CPF'] = cpf_site
                            break
                        except:
                            df_b.loc[i, 'CPF'] = "vazio"  
                num_iterations = registro  // 20 + 1
                for _ in range(num_iterations):
                    try:
                        driver.find_element("xpath",'//*[@id="barra_paginacao"]/tbody/tr/td[2]/a[1]').click()
                        for tr in range(2, 22): 
                            cpf_site = driver.find_element("xpath", f'/html/body/div[1]/div[8]/div/table[1]/tbody/tr[{tr}]/td[5]').text
                            miolo_cpf2 = extrair_miolo(cpf_site)
                            print(miolo_cpf1 + miolo_cpf2)
                            if miolo_cpf1 == miolo_cpf2:
                                try:
                                    df_b.loc[i, 'CPF'] = cpf_site
                                    break
                                except:
                                    df_b.loc[i, 'CPF'] = "vazio" 
                    except: 
                        pass   
        except:
            print("saiu no 1 try")
            pass
        driver.switch_to.default_content()
    except:
        df_b.to_csv("nome_incompleta.csv")
df_b.to_csv("nome.csv")