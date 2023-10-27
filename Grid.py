from random import shuffle, randrange
import entry
import tkinter as tk
import random


def make_maze(w, h):
    """ Cria uma matriz com valores aleatorios de acordo com os parametros w e h.
        Parâmetros:
            w - o número de colunas do labirinto (padrão: 16)
            h - o número de linhas do labirinto (padrão: 8)
    """

    matrizConvertida=[[random.randint(1,9) for _ in range((w*2)+1)] for i in range((h*2)+2)]

    return matrizConvertida

def draw_grid(container, height, width):
    """
    Cria uma celula para cada medida H e W
    """
    for x in range(width):
        row = []
        for y in range(height):
            cell = tk.Entry(container, width=6)
            cell.grid(row=x, column=y)
            row.append(cell)


def paint_outline(matriz, container):
    #Preenche verticalmente
    for h in range((len(matriz)-1)):
        # Define o cabecalho com as cordenadas
        entry.change_entry_text(container, h+1, 0, h)
        # Pinta toda a primeira linha de preto
       # entry.change_entry_color(container, h+1, 1, "black")
        # Pinta toda a ultima linha de preto
        #entry.change_entry_color(container, h+1, len(matriz)-1, "black")

    #Preenche horizontalmente
    for w in range(len(matriz[0])):
        # Define o cabecalho com as cordenadas
        entry.change_entry_text(container, 0, w+1, w)
        # Pinta toda a primeira linha de preto
        #entry.change_entry_color(container, 1, w+1, "black")
        # Pinta toda a ultima linha de preto
       # entry.change_entry_color(container, len(matriz)-1, w+1, "black")

def paint_maze(matriz, container):
    rowCount=0
    idCont=0
    for row in matriz:
        colCount = 0
        for char in row:
            entry.change_entry_text(container, rowCount+1, colCount+1, str(idCont)+" - "+str(char))
            idCont=idCont+1
            colCount=colCount+1
        rowCount=rowCount+1

def paint_path(visitadoArray,container,matriz):


    for cell in visitadoArray[0]:
        x, y = encontrar_posicao(cell,matriz)
        entry.change_entry_color(container, x+1, y+1, "yellow")

    # for row in matriz:
    #     colCount = 0
    #     for char in row:
    #         if(char==2):
    #             entry.change_entry_color(container, rowCount+1, colCount+1, "blue")
    #         colCount=colCount+1
    #     rowCount=rowCount+1

def encontrar_id(y,x,matriz):
    # Subtrai 1 de X e Y para ajustar para índices baseados em 0
    id = x * len(matriz[0]) + y
    return int(id)

def encontrar_posicao(id,matriz):
    x = (id) % len(matriz[0]) 
    y = (id) // len(matriz) 
    return x, y


