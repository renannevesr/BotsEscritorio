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
telefone = '//*[@id="telefone"]'
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

nome ='//*[@id="f_buscaMais"]/div[1]/table/tbody/tr[1]/td[2]'
nasc ='//*[@id="f_buscaMais"]/div[1]/table/tbody/tr[4]/td[2]'
idad ='//*[@id="f_buscaMais"]/div[1]/table/tbody/tr[4]/td[4]'
tel1 = '//*[@id="f_buscaMais"]/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/a'
tel2 = '//*[@id="f_buscaMais"]/div[2]/div[1]/table/tbody/tr[2]/td[1]/div/a'
tel3 = '//*[@id="f_buscaMais"]/div[2]/div[1]/table/tbody/tr[3]/td[1]/div/a'
tel4 = '//*[@id="f_buscaMais"]/div[2]/div[1]/table/tbody/tr[4]/td[1]/div/a'
end1= '//*[@id="f_buscaMais"]/div[3]/table/tbody/tr[1]/td[1]'
numen1=  '//*[@id="f_buscaMais"]/div[3]/table/tbody/tr[1]/td[2]'
bairro1 ='//*[@id="f_buscaMais"]/div[3]/table/tbody/tr[1]/td[3]'
cidade1= '//*[@id="f_buscaMais"]/div[3]/table/tbody/tr[1]/td[4]'
cep1= '//*[@id="f_buscaMais"]/div[3]/table/tbody/tr[1]/td[6]'
complementoend1 ='//*[@id="f_buscaMais"]/div[3]/table/tbody/tr[1]/td[7]'
end2= '//*[@id="f_buscaMais"]/div[3]/table/tbody/tr[2]/td[1]'
numen2=  '//*[@id="f_buscaMais"]/div[3]/table/tbody/tr[2]/td[2]'
bairro2 ='//*[@id="f_buscaMais"]/div[3]/table/tbody/tr[2]/td[3]'
cidade2= '//*[@id="f_buscaMais"]/div[3]/table/tbody/tr[2]/td[4]'
cep2= '//*[@id="f_buscaMais"]/div[3]/table/tbody/tr[2]/td[6]'
complementoend2 ='//*[@id="f_buscaMais"]/div[3]/table/tbody/tr[2]/td[7]'
end3= '//*[@id="f_buscaMais"]/div[3]/table/tbody/tr[3]/td[1]'
numen3=  '//*[@id="f_buscaMais"]/div[3]/table/tbody/tr[3]/td[2]'
bairro3 ='//*[@id="f_buscaMais"]/div[3]/table/tbody/tr[3]/td[3]'
cidade3= '//*[@id="f_buscaMais"]/div[3]/table/tbody/tr[3]/td[4]'
cep3= '//*[@id="f_buscaMais"]/div[3]/table/tbody/tr[3]/td[6]'
complementoend3 ='//*[@id="f_buscaMais"]/div[3]/table/tbody/tr[3]/td[7]'


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
time.sleep(2)
original_window = driver.current_window_handle
driver.find_element(By.XPATH, '//*[@id="submitButton"]').click()
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="topMenu"]/span[3]/div[1]').click() #atendimento antigo

time.sleep(1)
try:
    time.sleep(1)
    driver.switch_to.new_window('tab')
    while idx < rows:
        print("idx do for=", idx)
        beneficio = df.loc[idx, 'CPF']
        # url2 =f'https://promobank.online/sistema/consulta/processador.php?tipo=6&value={beneficio}&getMatriculas=true&tipoCampanha=&isJson=false&_=1720481550725'
        # driver.get(url2)
        # time.sleep(5)
        
        # nomes_variaveis = ['nome','cpf','nascimento','beneficio','telefone','endereco','bairro','cidade','uf','cep','dib','ddb','valor', 'situacao']
        # for variavel in nomes_variaveis:
        #     try:
        #         if variavel == 'telefone':
        #             print("entrou")
        #             dados = driver.find_element(By.XPATH, f'{eval(variavel)}').text
        #             print("dados")
        #             print(dados)
        #             df.loc[idx, variavel] = dados

        #         else:
        #             dados = driver.find_element(By.XPATH, f'{eval(variavel)}').get_attribute('value')
        #             print(dados)
        #             df.loc[idx, variavel] = dados
        #     except:
        #             dados = "sem dados"
        #             df.loc[idx, f'{variavel}'] = valor
        url3=f'https://promobank.online/sistema/consulta/processador.php?tipo=15&maisContatos=maisContatos&modo_fone=buscamais&value={beneficio}'
        driver.get(url3)
        time.sleep(4)
        nomes_variaveis2 =['nome', 'nasc','idad','tel1','tel2','tel3','tel4','end1','numen1','bairro1','cidade1','cep1','complementoend1','end2','numen2','bairro2','cidade2','cep2','complementoend2','end3','numen3','bairro3','cidade3','cep3','complementoend3']
        for variavel2 in nomes_variaveis2:
            try:
                    dados = driver.find_element(By.XPATH, f'{eval(variavel2)}').text
                    print("dados:",dados)
                    df.loc[idx, variavel2] = dados
            except:
                    dados = "sem dados"
                    df.loc[idx, f'{variavel2}'] = valor
        idx+=1
        print(idx)
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
    df.to_csv("Nova_fa.csv")
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
df.to_csv("Nova_fa.csv")
