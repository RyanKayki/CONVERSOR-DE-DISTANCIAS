import os

#FUNÇÕES
def km_to_miles(kilometers):
    miles = kilometers * 0.621371
    return miles

def miles_to_km(miles):
    kilometers = miles / 0.621371
    return kilometers

def meters_to_jards(meters):
    yards = meters * 1.09361
    return yards

def jards_to_meters(yards):
    meters = yards / 1.09361
    return meters

def cm_to_pol(centimeters):
    inches = centimeters / 2.54
    return inches

def pol_to_cm(inches):
    centimeters = inches * 2.54
    return centimeters

#PROGRAMA PRINCIPAL
while True:
    os.system('cls')
    print("----Conversor Térmico----")

#OPÇÃO E TRATANDO OS NUMEROS DE 1 A 6
    while True:
            print("\n (1) km para milhas\n (2) milhas para km\n (3) metros para jardas\n (4) jardas para metros\n (5) centimetro para polegada\n (6) polegada para centimetro")
            escolha = input("Escolha: ")
            if escolha.isnumeric():
                escolha = int(escolha)
                if escolha >= 1 and escolha <= 6:
                    break
                print("Opção invalida")

    #QUAl DISTANCIA - RESULTADO DAS CONVERSÕES    
    while True:
            
            cod = float(input("\n Por favor, insira o numero que você deseja: ")) 
            if escolha == 1:
                result = km_to_miles(cod)
                print("O resultado da Conversão é {:.2f} milhas".format(result))
                os.system('pause')
            
            elif escolha == 2:
                result = miles_to_km(cod)
                print("O resultado da Conversão é {:.2f} Km".format(result))
                os.system('pause')
            
            elif escolha == 3:
                result = meters_to_jards(cod)
                print("O resultado da Conversão é {:.2f} Jardas".format(result))
                os.system('pause')

            elif escolha == 4:
                result = jards_to_meters(cod)
                print("O resultado da Conversão é {:.2f} Metros".format(result))
                os.system('pause')

            elif escolha == 5:
                result = cm_to_pol(cod)
                print("O resultado da Conversão é {:.2f} Polegadas".format(result))
                os.system('pause')

            else:
                result = pol_to_cm(cod)
                print("O resultado da Conversão é {:.2f} Centimetros".format(result))   
                os.system('pause')