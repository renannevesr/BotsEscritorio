import time
import openpyxl
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://armoney.panoramaemprestimos.com.br'

login = 'rego&quintino01'
senha = 'rego1234'
list_b = 'lista.xlsx'
#list_b = 'LISTA_b.xlsx'
lista = []
df_b = pd.read_excel(list_b)

colunas = ['nome_ini']
df_b.columns = colunas
df_b["nome"] = df_b["nome_ini"]

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
    len_pesquisa = 0
    idx = 0
    ausencia = 0
    quantidade = 0
    dados = 0
    lista.clear()
    nome = df_b.loc[i, 'nome']
    time.sleep(1)
    driver.find_element("xpath", '// *[ @ id = "ui-id-2"] / a[1]').click()
    # Store iframe web element
    iframe = driver.find_element(By.XPATH, '//*[@id="id_execucao"]')
    # switch to selected iframe
    driver.switch_to.frame(iframe)
    if i ==0:
        driver.find_element("xpath", '//*[@id="lk_nomeCpf_cons"]').click()
    try:
        driver.find_element("xpath", '//*[@id="pnl_nomeCpf_cons"]/table/tbody/tr/td[2]/obrigatorio/input').send_keys(nome)
        driver.find_element("xpath", '//*[@id="id_listar"]').click()
        time.sleep(1)
        try :
            ausencia = driver.find_elements(By.CLASS_NAME, 'msg_aviso')
         
        except:
            print("entrou no try de msg_aviso")
            pass
        if ausencia !=0:
            df_b.loc[i, 'CPF'] = "nao_CPF"
        try:
            quantidade = driver.find_elements(By.CLASS_NAME, 'msg_aviso')
        except:
            pass
        try:
            dados = driver.find_elements(By.CLASS_NAME, 'lit')
            tam_dados = len(dados)
    
            for e in dados:
                idx +=1
         
        except:
            print( "entrou try dados")
            pass
        if tam_dados <3 and tam_dados> 1:
            time.sleep(2)
            cpf = driver.find_element("xpath", '/ html / body / div[1] / div[8] / div / table[1] / tbody / tr[2] / td[5]').text
            try:
                df_b.loc[i, 'CPF'] = cpf
            except:
                df_b.loc[i, 'CPF'] = "vazio"
            dados[0].click()
            time.sleep(2)
            endereco =driver.find_elements(By.CLASS_NAME, 'txt2')
            endereco_cidade = driver.find_elements(By.CLASS_NAME, 'txt12')
            endereco_1 = driver.find_elements(By.CLASS_NAME, 'txt100')
            endereco_2 = driver.find_elements(By.CLASS_NAME, 'txt4_5')
            endereco_3 = driver.find_elements(By.CLASS_NAME, 'txt4')
            tel =driver.find_elements(By.CLASS_NAME, 'clTel')

            for idx_city in endereco_cidade:
                city = idx_city.get_attribute('value')
            for indice in endereco:
                ia = indice.get_attribute('value')
            
            try:
                    tel1 = str(tel[0].text)
                    df_b.loc[i, 'Tel.1'] = tel1
            except:
                tel1=None   
        
            try:
                    tel2 = str(tel[1].text)
                    df_b.loc[i, 'Tel.2'] = tel2
            except:
                tel2=None   
        
            try:
                    tel3 = str(tel[2].text)
                    df_b.loc[i, 'Tel.3'] = tel3
            except:
                tel3=None   

            try:
                    rua = str(endereco_1[1].get_attribute('value'))
                    df_b.loc[i, 'Rua'] = rua
            except:
                rua=None        
            try:
                numero = str(endereco_3[1].get_attribute('value'))
                df_b.loc[i, 'Numero'] = numero  
            except:
                numero=None 
            try:
                    bairro = str(endereco_1[3].get_attribute('value'))
                    df_b.loc[i, 'Bairro'] = bairro
     
            except:
                bairro=None
                
            try:
                    cep = str(endereco_2[1].get_attribute('value'))
                    df_b.loc[i, 'Cep'] = cep
     
            except:
                cep=None
            try:
                cidade = str(endereco_cidade[1].get_attribute('value'))
                df_b.loc[i, 'Cidade'] = cidade
                print("cidade =",cidade)
            except:
                cidade =" não tem"
                
            try:
                UF = str(endereco[1].get_attribute('value'))
                df_b.loc[i, 'UF'] = UF
                print("UF=", UF)
            except:
                UF =" não tem"
            #margem
    
            driver.find_element("xpath",
                                '// *[ @ id = "ctlIntegracoes"] / integracoes / grupo[1] / integracao / acao / nome').click()
            driver.find_element("xpath", ' // *[ @ id = "id_infooperacional"]').click()
            time.sleep(5)
            try :
                dib = driver.find_elements(By.CLASS_NAME, 'editavel')
                diba =dib[1].text
                len_dib = len(diba)
                if len_dib == 10:
                    df_b.loc[i, 'DIB'] = diba
                    print("diba=", diba)
            except:
                pass
            try :
                dib = driver.find_elements(By.CLASS_NAME, 'editavel')
                diba =dib[1].text
                len_dib = len(diba)
                if len_dib == 10:
                    df_b.loc[i, 'DIB'] = diba
                    print("diba=", diba)
            except:
                pass
        if tam_dados >= 4:
            print("entrou 2 if")
            homonimos = tam_dados/2
            df_b.loc[i, 'CPF'] = "numero de homonimos na coluna da dib"
            df_b.loc[i, 'DIB'] = homonimos
    except:
        print("saiu no 1 try")
        pass
    driver.switch_to.default_content()
  

    print(df_b.head())
df_b.drop(["nome_ini"], axis=1, inplace=True)
df_b.to_csv("listaRJFinal.csv")