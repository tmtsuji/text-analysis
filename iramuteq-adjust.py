# -*- coding: utf-8 -*-
# Nao esquecer de verificar se esta no diretorio correto!!

# Salvando os arquivos txt em uma lista para conferência ao final 
import os

# a variavel path contem o caminho do diretorio
path = '/home/thays/Documents/Doutorado/udm2022/planos_argentina_eua/frança/teste' 
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
    
replace_list = ["bassin de rétention", "bassins de rétention", "puit d'infiltration",
                "puits d'infiltration","tranchée d'infiltration","tranchées d'infiltration", 
                "tranchée dreinante", "tranchées drainantes", "pavés poreux",  
                "toitures végétalisées", "toitures végétalisées", "toiture végétalisée",
                "toit végétal", "toiture végétale","bassin d'infiltration", 
                "bassins d'infiltration", "noue végétalisée", "noues végétalisées",
                "fossé végétalisée", "fossés végétalisées", "tranchée de rétention",
                "tranchées de rétention", "tranchée d’infiltration","tranchées d’infiltration",
                "eaux pluviales", "eau pluviale", "solution compensatoire",
                "solutions compensatories", "changement climatique", "îlots de chaleur",
                "îlot de chaleur","massif infiltrant", "tranchée infiltrant",
                "bassin de détention", "bassins de détention",]

    # lista dos termos substitutos
       # As ordens dos termos devem ser correspondentes as da replace list
       
surrogate_list = ["bassin_de_rétention","bassins_de_rétention","puit_d'infiltration",
                  "puits_d'infiltration","tranchée_d'infiltration","tranchées_d'infiltration",
                  "tranchée_dreinante","tranchées_drainantes","pavés_poreux",
                  "toitures_végétalisées","toitures_végétalisées","toiture_végétalisée",
                  "toit_végétal","toiture_végétale","bassin_d'infiltration",
                  "bassins_d'infiltration","noue_végétalisée", "noues_végétalisées",
                  "fossé_végétalisée","fossés_végétalisées","tranchée_de_rétention",
                  "tranchées_de_rétention","tranchée_d’infiltration","tranchées_d’infiltration",
                  "eaux_pluviales","eau_pluviale","solution_compensatoire",
                  "solutions_compensatories","changement_climatique","îlots_de_chaleur",
                  "îlot_de_chaleur","massif_infiltrant","tranchée_infiltrant"]


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
with open("aesn_fr.txt", 'w') as f: #Abre o arquivo txt para escrever
    #o nome do arquivo deve ser um novo nome inexistente na pasta
    
        
        with open("AESN_SDAGE2016seine.txt") as t: #abre os arquivos que estao
            
            # Ajustando o texto dos documentos antes de inseri-los

             for line in t:   

                for c in delete_list:
                    line = line.replace(c, " ")               

                for k in range(len(replace_list)):
                    line = line.replace(replace_list[k],surrogate_list[k])

                f.write(line) # escreve o conteudo dos arquivos no arquivo aberto              
            
        f.close()
       
       
       
       
       
       
       
       
       
       
       
       
       
     
