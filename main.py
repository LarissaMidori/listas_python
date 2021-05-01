# Testando listas e métodos de listas

frutas = ['morango','melão']
salada = ['cenoura','palmito']

mistura = salada + frutas #junta as 2 listas
print(mistura)

print(mistura[-1]) # procura o item no index -3 (conta de trá pra frente)
print(mistura[2])

mistura.append(['milho']) #adciona um elemento na última posição da lista
print(mistura)

mistura2 = mistura.copy() # faz uma cópia da lista mistura
print(mistura2)
print(id(mistura), id(mistura2)) # mostra que os valores das 2 listas são iguais, mas não os ids

numeros = [3,1,2,7,2,4,2]
print(numeros.count(2)) #mostra o número de vezes que um valor aparece na lista

mistura.extend(['alface','kiwi','palmito']) # adiciona ao final da lista
print(mistura)

print(mistura.index('palmito')) #obtém o índice da 1ª ocorrência de um valor na lista

mistura.insert(2,'rúcula') #adiciona rúcula na posição [2]
print(mistura)

mistura.pop(5) #removeu o item da posição[5]. Se não passar parâmetro remove o último item
print(mistura)

mistura.remove('palmito')
print(mistura) #remove o 1º item como parâmetro da lista

mistura.reverse() #inverte a ordem de uma lista
print(mistura)

mistura.sort(key = len) #ordena pelo comprimento das palavras
print(mistura)