import time
import openpyxl
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def calcular_data_nascimento(entrada):
    # Dividir a entrada e extrair anos, meses e dias
    partes = entrada.split()
    anos = int(partes[0].replace('.a', ''))
    meses = int(partes[1].replace('.m', ''))
    dias = int(partes[2].replace('.d', ''))
    
    # Data atual
    data_atual = datetime.now()
    
    # Calcular a data de nascimento
    data_nascimento = data_atual - relativedelta(years=anos, months=meses) - timedelta(days=dias)
    
    # Retornar a data de nascimento formatada
    return data_nascimento.strftime("%d/%m/%Y")


url = 'https://armoney.panoramaemprestimos.com.br'

login = 'rego&quintino01'
senha = '20304050'
list_b = 'lista_auditor.xlsx'
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
cel1 = '//*[@id="idFormCliente"]/div[2]/table/tbody/tr/td[1]/div[1]/div[1]/table/tbody/tr[1]/td[3]/mascara/input'
cel2 = '//*[@id="idFormCliente"]/div[2]/table/tbody/tr/td[1]/div[1]/div[1]/table/tbody/tr[2]/td[3]/mascara/input'
rua1 ='/html/body/div[1]/div[8]/div/form/div[2]/table/tbody/tr/td[1]/div[1]/div[3]/div[3]/div/table[1]/tbody/tr/td[2]/table/tbody/tr[3]/td[1]'
complement1 ='/html/body/div[1]/div[8]/div/form/div[2]/table/tbody/tr/td[1]/div[1]/div[3]/div[3]/div/table[1]/tbody/tr/td[2]/table/tbody/tr[3]/td[2]'
cidade1= '/html/body/div[1]/div[8]/div/form/div[2]/table/tbody/tr/td[1]/div[1]/div[3]/div[3]/div/table[1]/tbody/tr/td[2]/table/tbody/tr[4]/td[1]'
bairro1='/html/body/div[1]/div[8]/div/form/div[2]/table/tbody/tr/td[1]/div[1]/div[3]/div[3]/div/table[1]/tbody/tr/td[2]/table/tbody/tr[4]/td[2]'
cep1= '/html/body/div[1]/div[8]/div/form/div[2]/table/tbody/tr/td[1]/div[1]/div[3]/div[3]/div/table[1]/tbody/tr/td[2]/table/tbody/tr[4]/td[3]'
rua2 ='/html/body/div[1]/div[8]/div/form/div[2]/table/tbody/tr/td[1]/div[1]/div[3]/div[3]/div/table[1]/tbody/tr/td[2]/table/tbody/tr[5]/td[1]'
complement2 ='/html/body/div[1]/div[8]/div/form/div[2]/table/tbody/tr/td[1]/div[1]/div[3]/div[3]/div/table[1]/tbody/tr/td[2]/table/tbody/tr[5]/td[2]'
cidade2 = '/html/body/div[1]/div[8]/div/form/div[2]/table/tbody/tr/td[1]/div[1]/div[3]/div[3]/div/table[1]/tbody/tr/td[2]/table/tbody/tr[6]/td[1]'
bairro2 ='/html/body/div[1]/div[8]/div/form/div[2]/table/tbody/tr/td[1]/div[1]/div[3]/div[3]/div/table[1]/tbody/tr/td[2]/table/tbody/tr[6]/td[2]'
cep2 = '/html/body/div[1]/div[8]/div/form/div[2]/table/tbody/tr/td[1]/div[1]/div[3]/div[3]/div/table[1]/tbody/tr/td[2]/table/tbody/tr[6]/td[3]'
rua3=   '/html/body/div[1]/div[8]/div/form/div[2]/table/tbody/tr/td[1]/div[1]/div[3]/div[3]/div/table[1]/tbody/tr/td[2]/table/tbody/tr[7]/td[1]'
complement3=   '/html/body/div[1]/div[8]/div/form/div[2]/table/tbody/tr/td[1]/div[1]/div[3]/div[3]/div/table[1]/tbody/tr/td[2]/table/tbody/tr[7]/td[2]'
cidade3=   '/html/body/div[1]/div[8]/div/form/div[2]/table/tbody/tr/td[1]/div[1]/div[3]/div[3]/div/table[1]/tbody/tr/td[2]/table/tbody/tr[8]/td[1]'
bairro3 =   '/html/body/div[1]/div[8]/div/form/div[2]/table/tbody/tr/td[1]/div[1]/div[3]/div[3]/div/table[1]/tbody/tr/td[2]/table/tbody/tr[8]/td[2]'
cep3=  '/html/body/div[1]/div[8]/div/form/div[2]/table/tbody/tr/td[1]/div[1]/div[3]/div[3]/div/table[1]/tbody/tr/td[2]/table/tbody/tr[8]/td[3]'

# Assuming df_b and driver are already defined and initialized

for i in range(rows):
    try:
        len_pesquisa = 0
        ausencia = 0
        quantidade = 0
        dados = 0
        lista.clear()
        nome = df_b.loc[i, 'nome']
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
                cpf = driver.find_element("xpath", '/html/body/div[1]/div[8]/div/table[1]/tbody/tr[2]/td[5]').text
                try:
                    df_b.loc[i, 'CPF'] = cpf
                except:
                    df_b.loc[i, 'CPF'] = "vazio"
                dados[0].click()
                time.sleep(1)
                driver.find_element("xpath", '//*[@id="ctlIntegracoes"]/integracoes/grupo[2]/integracao').click()
                time.sleep(4)
                endereco = driver.find_elements(By.CLASS_NAME, 'txt2')
                endereco_cidade = driver.find_elements(By.CLASS_NAME, 'txt12')
                endereco_1 = driver.find_elements(By.CLASS_NAME, 'txt100')
                endereco_2 = driver.find_elements(By.CLASS_NAME, 'txt4_5')
                endereco_3 = driver.find_elements(By.CLASS_NAME, 'txt4')
                tel = driver.find_elements(By.CLASS_NAME, 'clTel')
                beneficio = driver.find_elements(By.CLASS_NAME, 'txt6')
                data_nasc = driver.find_elements(By.CLASS_NAME, 'cal_jq masc val_data verificavel hasDatepicker')
                print(data_nasc)
                idade = driver.find_element(By.XPATH, "//*[@id='id_idade']")

                nomes_variaveis = ['cel1', 'cel2', 'rua1', 'complement1', 'cidade1', 'bairro1', 'cep1', 'rua2', 'complement2', 'cidade2', 'bairro2', 'cep2', 'rua3', 'complement3', 'cidade3', 'bairro3', 'cep3']
                for variavel in nomes_variaveis:
                    try:
                        if variavel in ('cel1', 'cel2'):
                            dados = driver.find_element(By.XPATH, f'{eval(variavel)}').get_attribute('value')
                            print(dados)
                            df_b.loc[i, variavel] = dados
                        else:
                            dados = driver.find_element(By.XPATH, f'{eval(variavel)}')
                            print("dados")
                            print(dados.text)
                            df_b.loc[i, variavel] = dados.text
                    except:
                        dados = "sem dados"
                        df_b.loc[i, variavel] = 'sem dados'

                for idx_city in endereco_cidade:
                    city = idx_city.get_attribute('value')
                for indice in endereco:
                    ia = indice.get_attribute('value')

                try:
                    tel1 = str(tel[0].text)
                    df_b.loc[i, 'Tel.1'] = tel1
                except:
                    tel1 = None

                try:
                    tel2 = str(tel[1].text)
                    df_b.loc[i, 'Tel.2'] = tel2
                except:
                    tel2 = None

                try:
                    tel3 = str(tel[2].text)
                    df_b.loc[i, 'Tel.3'] = tel3
                except:
                    tel3 = None

                try:
                    rua = str(endereco_1[1].get_attribute('value'))
                    df_b.loc[i, 'Rua'] = rua
                except:
                    rua = None
                try:
                    numero = str(endereco_3[1].get_attribute('value'))
                    df_b.loc[i, 'Numero'] = numero
                except:
                    numero = None
                try:
                    bairro = str(endereco_1[3].get_attribute('value'))
                    df_b.loc[i, 'Bairro'] = bairro
                except:
                    bairro = None

                try:
                    cep = str(endereco_2[1].get_attribute('value'))
                    df_b.loc[i, 'Cep'] = cep
                except:
                    cep = None
                try:
                    cidade = str(endereco_cidade[1].get_attribute('value'))
                    df_b.loc[i, 'Cidade'] = cidade
                    print("cidade =", cidade)
                except:
                    cidade = "não tem"

                try:
                    UF = str(endereco[1].get_attribute('value'))
                    df_b.loc[i, 'UF'] = UF
                    print("UF=", UF)
                except:
                    UF = "não tem"

                try:
                    Bene = str(beneficio[0].get_attribute('value'))
                    df_b.loc[i, 'Beneficio'] = Bene
                    print("Bene=", Bene)
                except:
                    Bene = "não tem"

                try:
                    Bene1 = str(beneficio[1].get_attribute('value'))
                    df_b.loc[i, 'Especie'] = Bene1
                    print("Bene=", Bene1)
                except:
                    Bene1 = "não tem"

                try:
                    nasc = idade.text
                    df_b.loc[i, 'Idade'] = nasc
                    print("idade=", nasc)
                except:
                    nasc = "não tem"
                try:
                    data_nascimento = calcular_data_nascimento(nasc)
                    df_b.loc[i, 'data_nasc'] = data_nascimento
                    print("data_nasc=", data_nascimento)
                except:
                    nasc = "não tem"

                print(df_b)
            if tam_dados >= 4:
                print("entrou 2 if")
                homonimos = tam_dados / 2
                df_b.loc[i, 'CPF'] = "numero de homonimos na coluna da dib"
                df_b.loc[i, 'DIB'] = homonimos
        except:
            print("saiu no 1 try")
            pass
        driver.switch_to.default_content()
    except:
        df_b.to_csv("ms_incompleta.csv")
df_b.drop(["nome_ini"], axis=1, inplace=True)
df_b.to_csv("ms.csv")