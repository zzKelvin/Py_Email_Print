#O objetivo desse script é testar o envio e recebimento de emmails de uma plataforma.
#Enviando e recebendo no proprio endereço, a cada email que chega, é adicionado ao banco de Dados para "True"
#Checando se ao enviar 1000 emails, chegará os 1000 emails.

from PIL import Image
from DataBase import *
import pyautogui as pyg
import keyboard, pyscreenshot, time, os, pytesseract
pytesseract.pytesseract.tesseract_cmd = "C:\Tesseract-OCR\Tesseract.exe"
x=0
i=0
time.sleep(5)
while(True):
    i=i+1
    if keyboard.is_pressed('x') == True:
        print("Script cancelado")
        break
    #comando move o mouse e clica, X,Y sao coordenadas para onde o mouse vai, dependendo do botao do email
    pyg.click(46,104) #1   BOTAO ESCREVER/CRIAR EMAIL
    time.sleep(5)

    pyg.click(369,164) #2   BOTAO DESTINATARIO 
    pyg.write("email@email.com.br")
    time.sleep(1)

    pyg.click(991,215) #3   BOTAO ASSUNTO
    pyg.write("EMAIL N: {}".format(i))
    time.sleep(1)

    pyg.click(363,370) #4   BOTAO MENSAGEM
    pyg.write("Email para teste Nº({})".format(i))
    time.sleep(1)

    pyg.click(161,788) #5   BOTAO ENVIAR
    time.sleep(5)

    image = pyscreenshot.grab(bbox=(400, 120, 1000, 1080)) #TAMANHO DO PRINT
    image.save(r'C:\Users\LSE\Desktop\Py_Gmail\cut.png') #será salvo e logo apagado, é para o processamento da imagem
    if (i % 13) == 0: # Tamanho da caixa de entrada, mostrado na tela inicial, a cada vez que receber 13 novos emails, tira um print e salva.
        x=x+1
        image.save(r'C:\Users\LSE\Desktop\Py_Gmail\Email_Print\Caixa_Entrada({0}).png'.format(x))

    img1 = Image.open("cut.png")
    area = (40, 30, 200, 65) #area de corte para pegar a area com o nome do email(do print) ex:"EMAIL N: 551" e transformar em texto. foi 
    corte = img1.crop(area) #CORTA
    img2 = corte.resize((400,100)) #Aumenta o tamanho para facilitar pro pytesseract
    resultado = (pytesseract.image_to_string(img2)) #transforma a imagem cortada em texto 
    os.remove('cut.png')
    print(resultado)
    #abaixo, separa o nome "EMAIL N:" do numero inteiro, concatenando somente a numeração do email lido para salvar
    #no banco de dados, atraves do result
    if len(resultado) == 11:
        result = resultado[9]
    elif len(resultado) == 12:
        result = resultado[9] + resultado[10]
    elif len(resultado) == 13:
        result = resultado[9] + resultado[10] + resultado[11]
    elif len(resultado) == 14:
        result = resultado[9] + resultado[10] + resultado[11] + resultado[12]
    elif len(resultado) == 15:
        result = resultado[9] + resultado[10] + resultado[11] + resultado[12] + resultado[13]
    elif len(resultado) == 16:
        result = resultado[9] + resultado[10] + resultado[11] + resultado[12] + resultado[13] + resultado[14]
    if (int(result)) >= 0 and (int(result)) < 100000:
        Recebe_Banco = Emails.get(Emails.N_Email == result) #modifica no banco de dados para true o valor do ID do email
        Recebe_Banco.Possui_Banco = 'True'
        Recebe_Banco.save()
        print("Email N({}) adicionado ao Banco de Dados".format(i))
    else:
        print("Erro")
        break
    time.sleep(2)
