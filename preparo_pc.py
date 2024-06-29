import pyautogui as py
py.PAUSE = 3
import time 
from time import sleep

login = "CARLOS.NETO"
senha = "*******"

py.click(x=979, y=1069) # abertura do whatsapp web
py.click(x=844, y=1071) # abertura do Thunderbird 
py.click(x=797, y=1062) # abertura do Slack
py.click(x=937, y=1056) # abertura do Chrome 

# Processo de abertura do sistema Protheus

#abrir e logar no protheus e ja preparar o layout que eu gosto pra trabalhar
py.press("win") #vai abrir o protheus la na barra de pesquisa do windows
py.write("Protheus") #escreve protheus 
py.press("backspace")
py.press("enter") #clica para abrir 
time.sleep(4)
py.click(x=983, y=665) #confirma o primeiro alerta
time.sleep(4)
py.click(x=839, y=488) #clica no campo de login 
py.write(login) #escreve o login 
py.press("tab") #pula para o campo de senha 
py.write(senha) #escreve a senha 
py.click(x=902, y=616) #confirma o login 
py.click(x=1028, y=827) #confirma o segundo aviso   
time.sleep(7) 
#protheus aberto!
py.click(x=64, y=460) #atualizações
py.click(x=103, y=686) #especificos vasconcelos
py.click(x=1070, y=687) #ok
time.sleep(6)
py.click(x=25, y=33) #menu
py.click(x=90, y=642) #atualizaões 
py.click(x=95, y=685) #pré nota
py.click(x=1070, y=687) #ok
time.sleep(6)
py.click(x=25, y=33) #menu
py.click(x=92, y=698) #doc. entrada
py.click(x=1070, y=687) #ok
#layout pronto para trabalho!
