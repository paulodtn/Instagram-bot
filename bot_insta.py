from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
import secrets
import random

#CRIANDO LISTAS DE MENSAGENS E MARCAÇÕES E DELIMITANDO QUANTOS ELEMENTOS SERÃO SELECIONADOS
mens = ['Força', 'Você vai superar tudo isso', 'Vai dar tudo certo', 'Estamos com você', 'Tamo junto', 'Fé que tudo vai dar cero', 'A gente vai conseguir', '']
marc = ['@oellyson', '@mcelvisoficial', '@mctroiaoficial', '@mcdreadoficial', '@mcjapadorecifeoficial', '@pedrinhodorecifeoficial', '@elizamelloficial', '@recifeordinario', '@bregabregoso', '@biankacarvalho_oficial', '@fabioaraujotv', '@tvguararapesoficial', '@radiojornalpe','@tvjornalsbt', '@jc_pe', '@bregabregoso', '@portalg1']
k = 1
m = 5

rep = int(input('DEFINA QUANTAS VEZES QUER REPETIR O PROCESSO:'))
#ABRIR O NAVEGADOR NA PÁGINA DESEJADA
driver = webdriver.Firefox(executable_path=r'D:\VSCode\Pyton\BOT INSTA\geckodriver.exe')
driver.set_page_load_timeout(30)
driver.get("https://www.instagram.com")
time.sleep(5)
#PREENCHER COM OS DADOS NECESSÁRIOS PARA FAZER LOGIN
driver.find_element(By.XPATH,'/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input').send_keys("")#COLOCAR LOGIN ENTRE ''
driver.find_element(By.XPATH,'/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input').send_keys("")#COLOCAR SENHA DA CONTA ENTRE ''
time.sleep(3)
driver.find_element(By.XPATH,'/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div').click()
time.sleep(18)
#CLIQUES PARA PODER ACESSAR A BARRA DE PESQUISA
driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
time.sleep(6)
driver.get("")#LINK DO POST/PAGINA QUE ESTA PROCURANDO
time.sleep(4)
for r in range(1, rep + 1):
    print ('RODADA DE NUMERO:', r)#CONTADOR DO LAÇO DE REPETIÇÃO
    tempo = random.randint(20,300)#VARIAÇÃO DO TEMPO DE ESPERA DO LAÇO
    p1frase = (secrets.SystemRandom().sample(mens, k))
    p2frase = (secrets.SystemRandom().sample(marc, m))
    frase = p1frase + p2frase
    driver.find_element(By.XPATH,'').send_keys(' '.join(frase))#PREENCHER O CAMPO DE COMENTÁRIOS COM UMA FRASE E MARCAÇÕES ALEATÓRIAS
    driver.find_element(By.XPATH,'').click()#CLICAR NO ENTER
    time.sleep(tempo)