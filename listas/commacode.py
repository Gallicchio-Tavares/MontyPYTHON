'''
spam = ['apples', 'bananas', 'tofu', 'cats']
            0          1        2       3

Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. 
For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value 
passed to it. Be sure to test the case where an empty list [] is passed to your function.
'''

def separar(lista): #aceita uma lista de qualquer tamanho
  tamanho = len(lista)  

  if tamanho == 0: # lista vazia
    return
  elif tamanho == 1: # apenas um elemento na lista
    return lista[0]

  frase = ""  

  for i in range(tamanho): # demais casos
    if i < tamanho - 2:
      frase += lista[i] + ", "
    elif i == tamanho - 2: #penultima palavra
      frase += lista[i]
    elif i == tamanho - 1: #ultima palavra
      frase += " and " + lista[i]
  
  return frase

spam = ['apples', 'bananas', 'tofu', 'cats', 'dogs']
print(separar(spam))