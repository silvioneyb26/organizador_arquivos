import os

arq_ext= ['.py','.txt']

def pegar_extensao(nome):
    index = nome.rfind('.')
    return nome[index:]                        

def criar_pasta(diretorio, nome_pasta):
    pasta =  os.path.join(diretorio, "{}".format(nome_pasta))  
    if not os.path.isdir(pasta):
        os.mkdir(pasta)  

    nomes_arquivos = os.listdir(diretorio)
    nova_pasta = ''
    for arquivo in nomes_arquivos:
        if os.path.isfile(os.path.join(diretorio, arquivo)):
            # extensão do arquivo com letras minúsculas
            extensao = str.lower(pegar_extensao(arquivo))
            if extensao in arq_ext:
                nova_pasta = pasta
                velho = os.path.join(diretorio, arquivo)
                novo = os.path.join(nova_pasta, arquivo)
                os.rename(velho, novo) 
                     
def git_add(nome):
    os.system('git add {}'.format(nome))
    commit = str(input('Deixe um comentário: '))
    os.system('git commit -m {}'.format(commit))
    os.system('git push') 
                
               



nome_pasta = input("""Bem vindo!
Por favor, informe o nome da pasta a ser salva: """)
caminho = os.getcwd()
criar_pasta(caminho, nome_pasta)
mn = 0
while mn == 0:     
     
    print('\n Vamos salvar a pasta no github? 1.sim ou 2.nao:')   
    op = input("Qual é a opcão desejada? ")
    os.system("clear") 

    #selecionar opções
    if (op == "1"):       
      print(git_add(nome_pasta))
      mn += 1
    elif (op == "1"):
        print("Tudo bem! A pasta {} foi está salva em seud diretório".format(nome_pasta)) 
   
    
    
    
