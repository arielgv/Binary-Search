import random

def buscador(lista,principio,final,objetivo):

    if principio > final : 
        return False

    medio = (principio + final ) // 2

    if lista[medio] == objetivo :
        return True
    elif lista[medio] > objetivo:

        final = medio - 1 
        return buscador(lista,principio,final,objetivo)
    
    else:
        principio = medio + 1 
        return buscador(lista,principio,final,objetivo)





if __name__=="__main__":
    howlong = int(input( "cuantos numeros ? "))
    guess = int(input('q numero queres buscar ? '))
    listarr = [random.randint(0,100) for i in range (howlong)]
    listarr.sort()
    print(listarr)
    if buscador(listarr,0,len(listarr),guess) == True:
        print("si esta..")
    else:
        print("no esta ")