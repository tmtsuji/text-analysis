# -*- coding: utf-8 -*-
# Nao esquecer de verificar se esta no diretorio correto!!

# Salvando os arquivos txt em uma lista para conferência ao final 
import os

# a variavel path contem o caminho do diretorio
path = '' 
filenames = os.listdir(path)

# esse loop vai criar um arquivo contendo o código e o nome do arquivo 
#correpondente a cada código

with open("filenames.txt", "w") as p:
    for i in range(len(filenames)):
        s= "*n_{0}".format(i) + " " + "," + filenames[i] + ";"
        p.write(s)
    p.close()
  
    
# Deletando caracteres especiais e juntando os arquivos em um txt só
delete_list = ["*","#", "%","&", "*", "(",")", "-", "+","=","[", "]", "{","}",
               ";","<",">","/","–","_"]

# inserindo os termos de forma adequada ao iramuteq

    # lista de termos a serem substituidos
    
replace_list = [" "]

    # lista dos termos substitutos
       # As ordens dos termos devem ser correspondentes as da replace list
       
surrogate_list = [" "]


# Juntando textos e Escrenvendo o cabecalho requerido pelo Iramuteq

with open("teste.txt", 'w') as f: #Abre o arquivo txt para escrever
    #o nome do arquivo deve ser um novo nome inexistente na pasta
    
    for i in range(len(filenames)):  #loop para percorrer os arquivos
        
        j= "**** " + "*n_{0}".format(i) + " \n " #variável que contem o formato do cabecalho
        
        f.write(j) #escreve a variavel no arquivo aberto
        
        with open(filenames[i]) as t: #abre os arquivos que estao
            
            # Ajustando o texto dos documentos antes de inseri-los

             for line in t:   

                for c in delete_list:
                    line = line.replace(c, " ")               

                for k in range(len(replace_list)):
                    line = line.replace(replace_list[k],surrogate_list[k])

                f.write(line) # escreve o conteudo dos arquivos no arquivo aberto              
            
    f.close()



       

#Para ajustar e organizar um arquivo só 
with open("newfile.txt", 'w') as f: #Abre o arquivo txt para escrever
    #o nome do arquivo deve ser um novo nome inexistente na pasta
    
        
        with open("file.txt") as t: #abre os arquivos que estao
            
            # Ajustando o texto dos documentos antes de inseri-los

             for line in t:   

                for c in delete_list:
                    line = line.replace(c, " ")               

                for k in range(len(replace_list)):
                    line = line.replace(replace_list[k],surrogate_list[k])

                f.write(line) # escreve o conteudo dos arquivos no arquivo aberto              
            
        f.close()
       
       
       
       
       
       
       
       
       
       
       
       
       
     
