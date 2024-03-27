import time
import openpyxl
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://portaldatransparencia.gov.br/servidores/consulta?ordenarPor=nome&direcao=asc'

list_b = 'lista2.xlsx'
lista = []
df_b = pd.read_excel(list_b)
print(df_b.head())
rows = df_b.shape[0]
driver = webdriver.Chrome()
driver.get(url)
time.sleep(1)


for i in range(rows):
    indice = 0
    idx = 0
    quantidade = 0
    dados = 1
    lista.clear()
    cpf = df_b.loc[i, 'cpf']
    driver.get(url)
    time.sleep(1)
    driver.find_element("xpath", '//*[@id="id-box-filtro"]/div/div/ul/li[2]/div/button').click()
    driver.find_element("xpath", '//*[@id="cpf"]').send_keys(cpf)
    driver.find_element("xpath", '//*[@id="id-box-filtro"]/div/div/ul/li[2]/div/div/div/div[2]/input').click()
    driver.find_element("xpath", '//*[@id="box-filtros-aplicados-com-botao"]/p/button[1]').click()
    time.sleep(2)
    print("lista=",i)
    try: 
        vinculos = driver.find_elements(By.XPATH, '//*[@id="lista"]/tbody/tr/td')
        #print("entrou vinculos =", len(vinculos))
        quantidade = int(len(vinculos)/10)
    except:
        print("saiu")
    if quantidade> 0:
        for idx in range (quantidade):
            
            print(df_b)
            #print("quantidade=", quantidade)
            #print("idx=",idx)
            indice+=1
            time.sleep(5)
            try:                                     
                tipo =driver.find_elements(By.XPATH, f'/html/body/main/div[2]/div/div[2]/div[2]/div/div[2]/div/div[{dados}]/table/tbody/tr[{indice}]/td[2]/span')
                textos = [elemento.text for elemento in tipo]
                df_b.loc[i, 'Tipo'] = textos[0] 
            except:
                dados+=1
            if dados ==2:
                tipo =driver.find_elements(By.XPATH, f'/html/body/main/div[2]/div/div[2]/div[2]/div/div[2]/div/div[{dados}]/table/tbody/tr[{indice}]/td[2]/span')
                textos = [elemento.text for elemento in tipo]
                df_b.loc[i, 'Tipo'] = textos[0] 
            CPF_miolo= driver.find_elements(By.XPATH, f'/html/body/main/div[2]/div/div[2]/div[2]/div/div[2]/div/div[{dados}]/table/tbody/tr[{indice}]/td[3]/span')
            textos = [elemento.text for elemento in CPF_miolo]
            df_b.loc[i, 'CPF_M'] = textos[0]
            nome= driver.find_elements(By.XPATH, f'/html/body/main/div[2]/div/div[2]/div[2]/div/div[2]/div/div[{dados}]/table/tbody/tr[{indice}]/td[4]/span')
            textos = [elemento.text for elemento in nome]
            df_b.loc[i, 'Nome'] = textos[0]
            orgao = driver.find_elements(By.XPATH, f'/html/body/main/div[2]/div/div[2]/div[2]/div/div[2]/div/div[{dados}]/table/tbody/tr[{indice}]/td[5]/span')
            textos = [elemento.text for elemento in orgao]
            df_b.loc[i, 'Orgao'] = textos[0]
            matricula= driver.find_elements(By.XPATH, f'/html/body/main/div[2]/div/div[2]/div[2]/div/div[2]/div/div[{dados}]/table/tbody/tr[{indice}]/td[6]/span')
            textos = [elemento.text for elemento in matricula]
            df_b.loc[i, 'Matricula'] = textos[0]
            situacao =driver.find_elements(By.XPATH, f'/html/body/main/div[2]/div/div[2]/div[2]/div/div[2]/div/div[{dados}]/table/tbody/tr[{indice}]/td[7]/span')
            textos = [elemento.text for elemento in situacao]
            df_b.loc[i, 'Situacao'] = textos[0]
            funcao =driver.find_elements(By.XPATH, f'/html/body/main/div[2]/div/div[2]/div[2]/div/div[2]/div/div[{dados}]/table/tbody/tr[{indice}]/td[8]/span')
            textos = [elemento.text for elemento in funcao]
            df_b.loc[i, 'Funcao'] = textos[0]
            cargo =driver.find_elements(By.XPATH, f'/html/body/main/div[2]/div/div[2]/div[2]/div/div[2]/div/div[{dados}]/table/tbody/tr[{indice}]/td[9]/span')
            textos = [elemento.text for elemento in cargo]
            df_b.loc[i, 'Cargo'] = textos[0]
            qtd =driver.find_elements(By.XPATH, f'/html/body/main/div[2]/div/div[2]/div[2]/div/div[2]/div/div[{dados}]/table/tbody/tr[{indice}]/td[10]/span')
            textos = [elemento.text for elemento in qtd]
            df_b.loc[i, 'Quantidade'] = textos[0]
            if quantidade > 1:
                new_row = df_b.loc[i].copy()
                df_b = pd.concat([df_b, pd.DataFrame([new_row])], ignore_index=True)
df_b =df_b.drop_duplicates()
df_b = df_b.sort_values(by='cpf').reset_index(drop=True)
df_b.to_csv("listaTransparencia.csv")