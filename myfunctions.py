# -*- coding: utf-8 -*-
"""
Created on Mon May 11 12:53:32 2020

@author: Elite
"""


def q01_h():
    file = open('newscript.py', 'a')
    file.write("    circ.h(0)\n")
    
def q02_h():
    file = open('newscript.py', 'a')
    file.write("    circ.h(1)\n")
    
def q01_x():
    file = open('newscript.py', 'a')
    file.write("    circ.x(0)\n")
    
def q02_x():
    file = open('newscript.py', 'a')
    file.write("    circ.x(1)\n")
    
def run_circuit():
    file = open('newscript.py', 'a')
    file.write("    job = execute(circ, backend)\n")
    file.write("    result = job.result()\n")
    file.write("    outputstate = result.get_statevector(circ, decimals=3)\n")
    file.write("    return outputstate\n")
    