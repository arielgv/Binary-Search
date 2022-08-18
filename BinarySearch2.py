# Binary Search :
import random

def binary(lista,startpoint,endpoint,picked):
    
    if startpoint > endpoint:
        return False

    middlepoint = (startpoint + endpoint) // 2
    print(f'Looking for the number between {lista[startpoint]} and {lista[endpoint]}')

    if lista[middlepoint] == picked:
        return True
    elif picked > lista[middlepoint]:
        startpoint = middlepoint + 1
        return binary(lista,startpoint,endpoint,picked)
    elif picked < lista[middlepoint]:
        endpoint = middlepoint -1
        return binary(lista,startpoint,endpoint,picked)
    else:
        return False

if __name__=="__main__":
    howmuch = int(input("A random list is generating, enter how many numbers shall it have: "))
    thelist=[random.randint(0,100) for i in range (howmuch)]
    thelist.sort()
    print(len(thelist))
    numberpicked = int(input('List Generated!\n Enter the number for guess if is in list:  '))
    if binary(thelist,0,len(thelist)-1,numberpicked) == True :
        print('The number is in the list.')
        print(thelist)
    else:
        print('The number is NOT in the list.')
        print(thelist)