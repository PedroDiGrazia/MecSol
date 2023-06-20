import numpy as np
import matplotlib.pyplot as plt
import math
import sys

Qtd_nos = int(input("Quantos nós serão utilizados: "))

vetor_x = list(range(Qtd_nos))
vetor_y = list(range(Qtd_nos))
nos = []
for i in range(0, Qtd_nos):
    vetor_x[i] = int(input(f"Digite a coordenada X do nó {i}: ")) 
    vetor_y[i] = int(input(f"Digite a coordenada Y do nó {i}: "))
    nos.append([vetor_x[i],vetor_y[i]])
    
print()
for i in range(0, Qtd_nos):
    print(f"Nó {i} = {nos[i]}")
    
resposta_no = input("Deseja conectar algum nó mais de uma vez? (sim/não): ")

if resposta_no == 'sim':
    mais_conexao = int(input("Digite qual nó tera mais conexões: "))
    qtd_conexao = int(input("Quantas conexões serão feitas: "))
    valores_conexao = list(range(qtd_conexao))
    for i in range(0, qtd_conexao):
        valores_conexao[i] = int(input(f"Deseja conectar quais nós ao nó {mais_conexao}: "))

plt.scatter(vetor_x, vetor_y, color='red')
plt.plot(vetor_x, vetor_y, color='blue')
plt.plot([vetor_x[-1],vetor_x[0]],[vetor_y[-1],vetor_y[0]],color='blue')
if resposta_no == 'sim':
    for i in range(0,qtd_conexao):
        plt.plot([vetor_x[mais_conexao],vetor_x[valores_conexao[i]]],
                 [vetor_y[mais_conexao],vetor_y[valores_conexao[i]]],
                 color='blue')
    
    plt.show(block=False)
    print()  
else:
    print()
barras = list(range(Qtd_nos))
if resposta_no != 'sim':
    for i in range(0, Qtd_nos):
        barras[i] = int(input(f"Deseja conectar o nó {i} {nos[i]} a qual nó: ")) 
else:
    print()
plt.scatter(vetor_x, vetor_y, color='red')
plt.plot(vetor_x, vetor_y, color='blue')
plt.plot([vetor_x[-1],vetor_x[0]],[vetor_y[-1],vetor_y[0]],color='blue')
plt.show(block=False) 
Qtd_apoios = int(input("Digite a quantidade de apoios: "))
if Qtd_apoios != 2:
    print("Só é possível calcular quando a quantidade de apoios for 2!")
    print("REINICIE O PROGRAMA!")
    sys.exit()
apoios = list(range(Qtd_apoios))
for i in range(0, Qtd_apoios):
    apoios[i] = int(input("Digite em qual nó o apoio se encontra: "))

print(apoios)
print("!!!Tipos de apoio!!!")
print("-> FIXO = 1")
print("-> MOVEL = 2")
input("Aperte <enter> para continuar!")

tipo_apoio = list(range(Qtd_apoios))
for i in range(0,Qtd_apoios):
    tipo_apoio[i] = int(input(f"Digite o tipo do apoio {i} no Nó {apoios[i]}: "))
if tipo_apoio[0] == tipo_apoio[1]:
    print("Não é possivel calcular (tipos de apoios iguais)!")
    print("REINICIE O PROGRAMA!")
    sys.exit()

print(tipo_apoio)

dif_y = list(range(Qtd_nos))
dif_x = list(range(Qtd_nos))

for i in range(0,Qtd_apoios):
    dif_m = vetor_x[apoios[1]] - vetor_x[apoios[0]]

for i in range(0, Qtd_nos):
    dif_x[i] = vetor_x[barras[i]] - vetor_x[i]
    dif_y[i] = vetor_y[barras[i]] - vetor_y[i]
    dif_x[i] = abs(dif_x[i])
    dif_y[i] = abs(dif_y[i])

dif_x2 = list(range(Qtd_nos))
dif_y2 = list(range(Qtd_nos))
soma_2 = list(range(Qtd_nos))
tamanho_barra = list(range(Qtd_nos))

for i in range(0, Qtd_nos):
    dif_x2[i] = dif_x[i] ** 2
    dif_y2[i] = dif_y[i] ** 2

for i in range(0, Qtd_nos):
    soma_2[i] = dif_x2[i] + dif_y2[i]
    tamanho_barra[i] =  math.sqrt(soma_2[i])

print(tamanho_barra)

qtd_forcas = int(input("Digite quantas forças serão aplicadas: "))
local_forca = list(range(qtd_forcas))
tipo_forca = list(range(qtd_forcas))
intensidade_forca = list(range(qtd_forcas))
direção_forca = list(range(qtd_forcas))

for i in range(0, qtd_forcas):
    local_forca[i] = int(input(f"Digite em qual nó deseja aplicar a força {i}: "))

print("!!!TIPOS DE FORÇAS!!!")
print("-> Força Horizontal = 1")
print("-> Força Vertical = 2")
input("Aperte <enter> para continuar!")

força_horizontal = list(range(qtd_forcas))
força_vertical = list(range(qtd_forcas))

dir_força = 0
dif_fx = list(range(qtd_forcas))
dif_fy = list(range(qtd_forcas))

for i in range(0,qtd_forcas):
    tipo_forca[i] = int(input(f"Qual é o tipo da força {i}: "))
    intensidade_forca[i] = int(input(f"Qual é a intensidade da força {i}: "))
    direção_forca[i] = input(f"Qual é a direção da força {i} (+/-): ")

    if direção_forca[i] == '-':
        dir_força = 1   

    if tipo_forca[i] == 1:
        força_horizontal[i] = intensidade_forca[i]
        força_vertical[i] = 0
        dif_fy[i] = vetor_y[local_forca[i]] - vetor_y[apoios[0]]
    else:
        força_vertical[i] = intensidade_forca[i]
        força_horizontal[i] = 0
        dif_fx[i] = vetor_x[local_forca[i]] - vetor_x[apoios[0]]

print(dif_fx)
print(dif_fy)
for i in range(0,qtd_forcas):
    print(f"Força {i} do nó {local_forca[i]} = {intensidade_forca[i]} N")

plt.scatter(vetor_x, vetor_y, color='red')
plt.plot(vetor_x, vetor_y, color='blue')
plt.plot([vetor_x[-1],vetor_x[0]],[vetor_y[-1],vetor_y[0]],color='blue')
plt.arrow(vetor_x[i], vetor_y[i], força_horizontal[i]*0.2, força_vertical[i]*0.2, head_width=0.1, head_length=0.1, fc='red', ec='red')
plt.show(block=False)

apoio_fixo = list(range(Qtd_apoios))
apoio_móvel = list(range(Qtd_apoios))
apoio_engaste = list(range(Qtd_apoios))

resultante_vertical = 0
resultante_horizontal = 0
for i in range(0,Qtd_apoios):
    if tipo_apoio[i] == 1:
        v = list(range(Qtd_apoios))
        h = list(range(Qtd_apoios))
        apoio_fixo.append([v[i],h[i]])

    elif tipo_apoio[i] == 2:
        v = list(range(Qtd_apoios))
        apoio_móvel.append([v[i]])
    else:
        v = list(range(Qtd_apoios))
        h = list(range(Qtd_apoios))
        m = list(range(Qtd_apoios))
        apoio_engaste.append([v[i],h[i],m[i]])

print(apoio_fixo)
print(apoio_móvel)
print(apoio_engaste)

print(direção_forca)

força_vertical_resultante = 0
força_horizontal_resultante = 0

for i in range(qtd_forcas):
    força_vertical_resultante = força_vertical[-1]
    força_horizontal_resultante = força_horizontal[0]

print(f"Soma das forças na vertical dos apoios terão que ser iguais a: {força_vertical_resultante}")
print(f"Soma das forças na horizontal dos apoios terão que ser iguais a: {força_horizontal_resultante}")

sum_f = 0
for i in range(qtd_forcas):
    sum_f = sum_f + (força_vertical[i] * dif_fx[i]) + (força_horizontal[i] * dif_fy[i])

V1 = sum_f / dif_m
V0 = força_vertical_resultante - V1
H = força_horizontal_resultante

print(f"V0 = {V0}N")
print(f"V1 = {V1}N")
print(f"Hfixo = {H}N")
