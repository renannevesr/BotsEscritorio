import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

def saida():
    driver.find_element(By.XPATH, '//*[@id="sidebar-shortcuts-large"]/button[3]').click()
    modal_saida_1 = driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div[2]')
    time.sleep(5)
    btn_out = driver.find_elements(By.CLASS_NAME, 'btn')
    len_btn = len(btn_out)
    for i in range(len_btn):
        bot_txt = btn_out[i].text
        #print(bot_txt)
        if bot_txt == 'Sim':
            btn_out[i].click()
            break
        
nome = '//*[@id="tab_dados"]/div[1]/div[1]/div/ul/li[1]/div/div[1]/input'
cpf = '//*[@id="tab_dados"]/div[1]/div[1]/div/ul/li[1]/div/div[2]/input'
nascimento = '//*[@id="tab_dados"]/div[1]/div[1]/div/ul/li[2]/div/div[1]/input'
beneficio = '//*[@id="tab_dados"]/div[1]/div[1]/div/ul/li[2]/div/div[2]/input'
especie = '//*[@id="tab_dados"]/div[1]/div[1]/div/ul/li[2]/div/div[3]/input'
endereco = '//*[@id="tab_dados"]/div[1]/div[2]/div/ul/li[1]/div/div[1]/input'
bairro = '//*[@id="tab_dados"]/div[1]/div[2]/div/ul/li[2]/div/div[2]/input'
cidade ='//*[@id="tab_dados"]/div[1]/div[2]/div/ul/li[1]/div/div[2]/input'
uf = '//*[@id="tab_dados"]/div[1]/div[2]/div/ul/li[1]/div/div[3]/input'
cep ='//*[@id="tab_dados"]/div[1]/div[2]/div/ul/li[2]/div/div[1]/input'
dib = '//*[@id="tab_dados"]/div[2]/div/div/ul/li/div/div[2]/input'
ddb ='//*[@id="tab_dados"]/div[2]/div/div/ul/li/div/div[3]/input'
valor ='//*[@id="tab_financeiro"]/div[2]/div[1]/div/ul/li[1]/div/div[1]/input'
situacao ='//*[@id="f_simulacao_"]/div[1]/div/div[2]/div[6]'
url = 'https://promobank.online/'
codigo = '29028'
login = 'regoequintino'
senha = 'C10203040*'

list = 'lista.xlsx'
idx = 0
lista = []
df = pd.read_excel(list)
print(df.head())
rows = df.shape[0]
driver = webdriver.Chrome()
driver.get(url)
time.sleep(1)
try:
    driver.find_element(By.XPATH, '//*[@id="aceitarCookies"]').click()
    time.sleep(1)
except:
    pass
driver.find_element(By.XPATH, '//*[@id="inputEmpresa"]').send_keys(codigo)
driver.find_element(By.XPATH, '//*[@id="inputUsuario"]').send_keys(login)
driver.find_element(By.XPATH, '//*[@id="passField"]').send_keys(senha)
time.sleep(1)
original_window = driver.current_window_handle
driver.find_element(By.XPATH, '//*[@id="submitButton"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="topMenu"]/span[3]/div[1]').click() #atendimento antigo

time.sleep(1)
try:
   # driver.find_element(By.XPATH, '// *[ @ id = "topMenu"] / span[2]').click()
    time.sleep(1)
    # Store iframe web element
    #iframe = driver.find_element(By.XPATH, '//*[@id="bodyLayout"]/iframe[3]')
    #driver.switch_to.frame(iframe)
    driver.switch_to.new_window('tab')
    while idx < rows:
        print("idx do for=", idx)
        beneficio = df.loc[idx, 'NB']
        url2 =f'https://promobank.online/sistema/consulta/processador.php?tipo=2&value={beneficio}&getMatriculas=false&competencia=&modoConsulta=folha_atual&tipoCampanha=&_=1700576191771'
        driver.get(url2)
        time.sleep(5)
        nomes_variaveis = ['nome','cpf','nascimento','beneficio','especie','endereco','bairro','cidade','uf','cep','dib','ddb','valor', 'situacao']
        for variavel in nomes_variaveis:
            try:
                if variavel == 'situacao':
                    print("entrou")
                    dados = driver.find_element(By.XPATH, f'{eval(variavel)}').text
                    print("dados")
                    print(dados)
                    df.loc[idx, variavel] = dados
                    print(df)
                else:
                    dados = driver.find_element(By.XPATH, f'{eval(variavel)}').get_attribute('value')
                    print(dados)
                    df.loc[idx, variavel] = dados
                    print(df)
            except:
                    dados = "sem dados"
                    df.loc[idx, f'{variavel}'] = valor
        idx+=1
except:
    driver.switch_to.window(original_window)
    print("saida 2.1")
    saida()
    time.sleep(1)
    try:
        df['situacao'] = df['situacao'].str.split('\n').str[1]
    except:
        pass
    try: 
        df[['Data_Nascimento', 'Idade']] = df['nascimento'].str.extract(r'(\d{2}/\d{2}/\d{4})\s+(\d+)\s+Anos')
    except:
        pass
    df.to_csv("Nova.csv")
driver.switch_to.window(original_window)
driver.find_element(By.XPATH, '//*[@id="sidebar-shortcuts-large"]/button[3]').click()
modal_saida_1 = driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div[2]')
time.sleep(2)
btn_out = driver.find_elements(By.CLASS_NAME, 'btn')
len_btn = len(btn_out)
for i in range(len_btn):
    bot_txt = btn_out[i].text
    if bot_txt == 'Sim':
        btn_out[i].click()
        break
try:
    df['situacao'] = df['situacao'].str.split('\n').str[1]
except:
    pass
try: 
    df[['Data_Nascimento', 'Idade']] = df['nascimento'].str.extract(r'(\d{2}/\d{2}/\d{4})\s+(\d+)\s+Anos')
except:
    pass
df = df.drop(columns=['beneficio','nascimento'])
df.to_csv("Nova.csv")
