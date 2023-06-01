import os
import time

caminho_pasta = r'C:\Users\joao mendes\Desktop\projectX'
lista_anterior = [caminho_pasta]

while True:

    lista_atual = os.listdir(caminho_pasta)

    if lista_atual != lista_anterior:
        print("O diretório foi atualizado.")
        lista_anterior = lista_atual
    else:
        print("Diretório atualizado.")
    time.sleep(1)
