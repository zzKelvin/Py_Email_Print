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

while(True):
    i=i+1
    if keyboard.is_pressed('x') == True:
        print("Script cancelado")
        break

    pyg.click(46,104) #1   ESCREVER/CRIAR EMAIL
    time.sleep(5)

    pyg.click(369,164) #2   DESTINATARIO 
    pyg.write("email@email.com.br")
    time.sleep(1)

    pyg.click(991,215) #3   ASSUNTO
    pyg.write("EMAIL N: {}".format(i))
    time.sleep(1)

    pyg.click(363,370) #4   MENSAGEM
    pyg.write("Email para teste Nº({})".format(i))
    time.sleep(1)

    pyg.click(161,788) #5   ENVIAR
    time.sleep(5)

    image = pyscreenshot.grab(bbox=(400, 120, 1000, 1080))
    image.save(r'C:\Users\LSE\Desktop\Py_Gmail_Print\cut.png')
    image.save(r'C:\Users\LSE\Desktop\Py_Gmail_Print\Email_Print\Email_N({0}).png'.format(x))

    img1 = Image.open("cut.png")
    area = (40, 30, 200, 65)
    corte = img1.crop(area)
    img2 = corte.resize((400,100))
    resultado = (pytesseract.image_to_string(img2))
    os.remove('cut.png')

    print(resultado)
    
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
        Recebe_Banco = Emails.get(Emails.N_Email == result)
        Recebe_Banco.Possui_Banco = 'True'
        Recebe_Banco.save()
        print("Email N({}) adicionado ao Banco de Dados".format(i))
    else:
        print("Erro")
        break
    time.sleep(2)
