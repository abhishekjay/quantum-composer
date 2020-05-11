# -*- coding: utf-8 -*-
import tkinter
from tkinter import *
from myfunctions import q01_h, q01_x, q02_h, q02_x, run_circuit
parent = Tk(screenName=None,  baseName=None,  className='Quantum Composer',  useTk=1)  

def initialisation_2():
    file = open('newscript.py', 'a')
    file.write("import numpy as np\n")
    file.write("from qiskit import *\n")
    file.write("def circuit():\n")
    
    file.write("    circ = QuantumCircuit(2)\n")
    file.write("    backend = Aer.get_backend('statevector_simulator')\n")

def initialisation_1():
    file = open('newscript.py', 'a')
    file.write("import numpy as np\n")
    file.write("from qiskit import *\n")
    file.write("def circuit():\n")
    
    file.write("    circ = QuantumCircuit(1)\n")
    file.write("    backend = Aer.get_backend('statevector_simulator')\n")
    
def runcircuit():
    run_circuit()
    from newscript import circuit
    result = circuit()
    message_result = Message(parent, text = result)
    message_result.place(relx = 0, rely = 0.45)
    open('newscript.py', 'w').close()
    
def addgate_h_q01():
    q01_h()
    
def addgate_h_q02():
    q02_h()

def addgate_x_q01():
    q01_x()
    
def addgate_x_q02():
    q02_x()
    
    
init_1 = Button(parent, text = "Single Qubit", fg = "green", command = initialisation_1)
init_1.place(relx = 0.05, rely = 0.05)

init_2 = Button(parent, text = "Two Qubit", fg = "green", command = initialisation_2)
init_2.place(relx = 0.15, rely = 0.05)

h_q01 = Button(parent, text = "H", fg = "red", command = addgate_h_q01)
h_q01.place(relx = 0.1, rely = 0.1)

x_q01 = Button(parent, text = "X", fg = "black", command = addgate_x_q01)
x_q01.place(relx = 0.15, rely = 0.1) 

h_q02 = Button(parent, text = "H", fg = "red", command = addgate_h_q02)
h_q02.place(relx = 0.1, rely = 0.2)   

x_q02 = Button(parent, text = "X", fg = "black", command = addgate_x_q02)
x_q02.place(relx = 0.15, rely = 0.2)

run_button = Button(parent, text = "RUN", fg = "black", command = runcircuit)
run_button.place(relx = 0.125, rely = 0.3)

clear_button = Button(parent, text = "CLEAR", fg = "black", command = lambda: message_result.destroy())
clear_button.place(relx = 0.3, rely = 0.3)

label_q01 = Label(parent, text='q_01')
label_q01.place(relx = 0, rely = 0.1)
label_q02 = Label(parent, text='q_02')
label_q02.place(relx = 0, rely = 0.2) 


parent.mainloop()  