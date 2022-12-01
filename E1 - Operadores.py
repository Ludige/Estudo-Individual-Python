num = 2
num += 1 # Não aceita ++ e -- como operadores
print(num)

num = 25
print(num//2) # divide e arredonda pra baixo

string = "ABCDEFG"
# Consegue recuperar posição
print(string[2])
print(string[2:5])
print(string[-3]) #inverso

print(len(string)) #Tamanho da array

#
if len(string) > 2:
    print("Maior que 2")
    
for letra in string:
    print(letra)
    
while num > 20:
    print(num)
    num -= 1    