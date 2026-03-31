import pyautogui
from time import sleep
import time
pyautogui.click (256,174 ,duration=1)
pyautogui.press("enter")
sleep(3)
pyautogui.click(962,617, duration=2)
pyautogui.write("abel")
pyautogui.press("enter")
sleep(2)
pyautogui.press('enter')
#clicar novo produto
pyautogui.click(32,48, duration= 1)
#add produto
with open('lista.txt' , 'r') as arquivo:
    for linha in arquivo:
        id_prod = linha.split(",")[0]
        nome = linha.split(",")[1]
        qntd = linha.split(",")[2]
        preco = linha.split(",")[3]

        pyautogui.click(176,90, duration= 1)
        pyautogui.write(id_prod)
        pyautogui.click(178,151, duration= 1)
        pyautogui.write(nome)
        pyautogui.click(185,218, duration= 1)
        pyautogui.write(qntd)
        pyautogui.click(233,282, duration= 1)
        pyautogui.write(preco)
        pyautogui.click(255,331, duration= 1)
        time.sleep(1)
        pyautogui.press('enter')