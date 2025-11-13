y = int(input().strip())

def numeros_diferentes(year): # year para evitar la letra nh del espanhol
    digitos = [d for d in str(year)] # Ciclo for compacto para listas
    return len(digitos) == len(set(digitos))

contador = y + 1
while not numeros_diferentes(contador):
    contador += 1

print(contador)

