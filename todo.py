from datetime import datetime

archivo ={}
"""
ejemplo = {
            id=1,
            titulo="",
            date=datetime.now(),
            user="",
            hacer=[],
            hechas=[]
        }
"""

def nueva():
    #Rellenar logica para generar una nueva nota
    print("se ha guardado con exito")

def borrar():
    archivo.pop(input("numero de nota a eliminar:"))
    #Corregir codigo para agregar un condicional:
        #print("seguro que desea borrar esta nota:",archivo["titulo"])
    print("se ha borrado con exito")

def todas():
    for nota in archivo:
        print(nota["id"]," - ",nota["titulo"])

switcher = {
        0: nueva,
        1: borrar,
        2: todas
    }


def numbers_to_strings(argument):
    func = switcher.get(argument, "nothing")
    return func()

Input: numbers_to_strings(int(input("numero:")))
