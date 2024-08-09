#!/usr/bin/env python3
import sys

tabuada_valor = 0
tabuada_tabela = []
count = 0

if(len(sys.argv) > 1):
    print("none")
else:
    while tabuada_valor <= 10:
        count = 0

        while count <= 10:                 
            multiplicacao_tabuada = tabuada_valor * count 
            tabuada_tabela.append(multiplicacao_tabuada)
            count += 1
        
        tabuada_string = ' '.join(str(v) for v in tabuada_tabela) #Como o array é de numberos precisei fazer esse for para mudar para string
        print(f"Table de {tabuada_valor}: {tabuada_string}")
        tabuada_tabela = []
        tabuada_valor += 1



