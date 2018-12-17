from tkinter import *


"""
#Janela com 2 frames e 4 botoes

#Cria Janela
window = Tk()


#Cria Frame 1
topFrame = Frame(window)
#Poe frame 1 no topo da janela
topFrame.pack(side=TOP)

#Cria botao 1
button1 = Button(topFrame, text="Button 1", fg="red")
#Poe botao 1 no lado esquerdo do frame 1
button1.pack(side=LEFT)
#Cria botao 2
button2 = Button(topFrame, text="Button 2", fg="blue")
#Poe botao 2 no lado esquerdo do frame 1
button2.pack(side=LEFT)
#Cria botao 3
button3 = Button(topFrame, text="Button 3", fg="green")
#Poe botao 3 no lado esquerdo do frame 1
button3.pack(side=LEFT)

#Cria Frame 2
bottomFrame = Frame(window)
#Poe frame 2 na parte de baixo da janela
bottomFrame.pack(side=BOTTOM)

#Cria botao 4
button4 = Button(bottomFrame, text="Button 4", fg="purple")
#Poe botao 4 na parte de baixo do frame 2
button4.pack(side=BOTTOM)


#Cria loop pra janela ficar aberta
window.mainloop()
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

"""
#Janela que tem 3 labels de tamanho dinamico

#Cria Janela
window = Tk()


#Cria label 1
label1 = Label(window, text="One", bg="red", fg="white")
#Poe label 1 na window
label1.pack()
#Cria label 2
label2 = Label(window, text="Two", bg="green", fg="black")
#Poe label 2 na window e faz ela sempre preencher a window horizontalmente
label2.pack(fill=X)
#Cria label 3
label3 = Label(window, text="Three", bg="blue", fg="white")
#Poe label 3 na window e faz ela sempre preencher a window verticalmente
label3.pack(side=LEFT, fill=Y)


#Cria loop pra janela ficar aberta
window.mainloop()
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

"""
#Janela com Grid Layout tendo 2 labels, 2 entrys e 1 checkbox

#Cria Janela
window = Tk()


#Cria label 1
label1 = Label(window, text="Name")
#Posiciona label 1 na grid layout, primeira linha primeira coluna, e gruda o texto na direita (east)
label1.grid(row=0, column=0, sticky=E)
#Cria label 2
label2 = Label(window, text="Password")
#Posiciona label 2 na grid layout, segunda linha primeira coluna, e gruda o texto na direita (east)
label2.grid(row=1, column=0, sticky=E)

#Cria entry 1
entry1 = Entry(window)
#Posiciona entry 1 na grid layout, primeira linha segunda coluna
entry1.grid(row=0, column=1)
#Cria entry 2
entry2 = Entry(window)
#Posiciona entry 2 na grid layout, segunda linha segunda coluna
entry2.grid(row=1, column=1)

#Cria checkbox
checkbox = Checkbutton(window, text="Keep me Logged in")
#Posiciona checkbox e faz ele ocupar duas colunas
checkbox.grid(columnspan=2)



#Cria loop pra janela ficar aberta
window.mainloop()
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

"""
#Janela com botao que ao clicar chama funcao

#Cria Janela
window = Tk()


#Modo 1
#Cria funcao
#def printName():
    #print("nhom nhom nhom!")

#Cria botao e associa a funcao
#button1 = Button(window, text="Print nhom nhom nhom", command=printName)
#Poe botao na janela
#button1.pack()

#ou

#Modo 2
#Cria funcao e associa evento
def printName(event):
    print("nhom nhom nhom!")

#Cria botao
button1 = Button(window, text="Print nhom nhom nhom")
#Associa botao a funcao
button1.bind("<Button-1>", printName)
#Poe botao na janela
button1.pack()


#Cria loop pra janela ficar aberta
window.mainloop()

"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

"""
#Janela com frame que chama uma funcao pra cada click diferente (botao esquerdo do mouse, direito, e do meio)

#Cria Janela
window = Tk()


#Evento caso clique com botao esquerdo do mouse
def leftClick(event):
    print("Left")

#Evento caso clique com botao do meio do mouse
def middleClick(event):
    print("Middle")

#Evento caso clique com botao direito do mouse
def rightClick(event):
    print("Right")


#Cria frame com tamanho fixo
frame = Frame(window, width=300, height=250)

#Caso o usuario clique com o botao esquerdo do mouse (Button-1), chama funcao leftClick
frame.bind("<Button-1>", leftClick)
#Caso o usuario clique com o botao do meio do mouse (Button-2), chama funcao middleClick
frame.bind("<Button-2>", middleClick)
#Caso o usuario clique com o botao direito do mouse (Button-3), chama funcao rightClick
frame.bind("<Button-3>", rightClick)

#Coloca frame na janela
frame.pack()


#Cria loop pra janela ficar aberta
window.mainloop()
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import time


# [ Funcao chamada ao apertar o botao ]
def func_example(event):
    
    lbStatus.config(text="Status: executando.")
    lbStatus.update()
    
    for i in range(11):
        lbProgresso.config(text="Progresso: loop " + str(i) + " de 10.")
        lbProgresso.update()
        time.sleep(1)
        
        if i >= 10:
            lbStatus.config(text="Status: loop finalizado.")
            lbStatus.update()
        

    
# [ Cria Window ]
window = Tk()

#Define titulo da window
window.title('Exemplo')
#Define tamanho da window
window.geometry("500x300")
#Define se o tamanho da window é dinamico
window.resizable(0, 0)



#Cria lbDica
lbDica = Label(window, text="Aperte o botao 'Iniciar' para mudar os labels 'Status' e 'Progresso'.", fg="red")
#Posiciona lbDica na window
lbDica.pack(fill=X, padx=10, pady=35)



#Cria btIniciar
btIniciar = Button(window, text="Iniciar")
#Associa btIniciar a funcao bltgm
btIniciar.bind("<Button-1>", func_example)
#Posiciona btIniciar na window
btIniciar.pack(fill=X, padx=35, pady=5, ipady=10)



#Cria lbProgresso
lbProgresso = Label(window, text="Progresso: o botão ainda não foi apertado.")

#Posiciona lbProgresso na window
lbProgresso.pack(fill=X, padx=10, pady=20)



#Cria lbStatus
lbStatus = Label(window, text="Status: aguardando click.")

#Posiciona lbStatus na window
lbStatus.pack(fill=X, padx=10, pady=5)



#Cria loop pra janela ficar aberta
window.mainloop()