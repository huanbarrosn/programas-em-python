import os

assunto = 'frutas'
arquivo = 'frutas'
path_file = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path_raiz = os.path.join(path_file, 'database', f'{assunto}.txt')
print(path_raiz)

'''print()

with open(file=f'{path}', 
          mode='r', 
          encoding='utf-8') as arquivo:
    
    lista_palavras = arquivo.readlines()
    print(lista_palavras)'''