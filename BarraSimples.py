print()
QtdApoios = int(input("Quantos apoios serão utilizados: "))
print()
print("!!!Considere os Apoios como:!!!")
print("-> Fixo = 1")
print("-> Movel = 2")
print("-> Engaste = 3")
print()
input("Aperte <Enter> para continuar!")

i = 0
n = 0
m = 0
Fixo = 'Fixo'
Movel = 'Movel'
Engaste = 'Engaste'

vetor = list(range(QtdApoios))
for i in range(QtdApoios):
    vetor[m]=10
    m=m+1
Apoio = list(range(QtdApoios))
print()
j=0
p=100
m=0
i=0
for i in range(0, QtdApoios):
    n = n + 1
    vetor[m] = int(input(f"Digite o numero do Apoio no ponto {n} (1,2,3): "))
    if vetor[m] <1 or vetor[m] >3: 
        p=p+1
        for j in range(0,p):
            print()
            print("NUMERO INVALIDO! DIGITE NOVAMENTE")
            vetor[m] = int(input(f"Digite o numero do Apoio no ponto {n} (1,2,3): "))
            if vetor[m] >=1 and vetor[m]<=3:
                m=m+1
                break
            else:
                print()
    else:
        m=m+1
print()
n = 0
o = 0
m = 0       
i = 0
for i in range(0, QtdApoios):
    if vetor[m] == 1:
        Apoio[o]=Fixo   
    elif vetor[m] == 2:
        Apoio[o] = Movel
    else:
        Apoio[o]=Engaste
    o = o+1
    m = m+1

o=0
m=0
for i in range(0, QtdApoios):
    n = n + 1
    print(f"O tipo do apoio no ponto {n} é: {Apoio[o]}")
    o = o + 1
print()
n = 0
m = 0
i = 0
j = 0
vetor2 = list(range(QtdApoios))
print("Origem = 0m")
for i in range(0, QtdApoios):
    n = n+1
    vetor2[j] = float(input(f"Qual é a distância em relação à origem do apoio {n}: "))
    j = j+1
print()

TamanhoBarra =  vetor2[-1] - vetor2[0]

print(f"O tamanho da barra é de: {TamanhoBarra}m")

QtdForcas= int(input("Quantas forças serão aplicadas: "))

print()
print("!!!Considere as Forças como:!!!")
print("-> Distribuida = 1")
print("-> Concentrada = 2")
print()
input("Aperte <Enter> para continuar!")

Forca = list(range(QtdForcas))
c=0
i=0
for i in range(0,QtdForcas): 
    TipoForca = int(input("Qual tipo de força sera aplicada: "))
    if TipoForca == 1:
        print("Força distribuida!")
        Forca[c]= 'Distribuida' 
    else:
        print("Força concentrada")
        Forca[c]= 'Concentrada' 
    c=c+1
i=0
c=0
j=0
p=100
for i in range(0,QtdForcas):
    if Forca[c] == 'Concentrada':
        print()
        PosForcaC = float(input(f"Onde deseja aplicar a força? Tamanho da barra = {TamanhoBarra}m: ")) 
        if PosForcaC >TamanhoBarra or PosForcaC <0:
            p=p+1
            for j in range (0,p):
                print()
                print("NUMERO INVALIDO, DIGITE NOVAMENTE!")
                PosForcaC = float(input(f"Onde deseja aplicar a força? Tamanho da barra = {TamanhoBarra}m: ")) 
                if PosForcaC <=TamanhoBarra and PosForcaC >=0:
                    print()
                    print(f"Força aplicada em {PosForcaC}m")
                    p=0
                    break
                else:
                    print()
            else:
                print()
        
    else:
        print()
        print("Utilize um dos apoios como origem!")
        PosForcaD = float(input(f"Digite o intervalo da força em relação a origem até {TamanhoBarra}m: "))
        if PosForcaD > TamanhoBarra:
           PosForcaD = float(input("Digite Novamente: "))
    c=c+1

print()
IntensidadeF = float(input("Qual é a intensidade da força (N): "))
o=0
i=0
V1=0
V2=0
V3=0
H1=0
H3=0
M3=0
ForcasT = list(range(3))
ForcasA1 = [V1,H1]
ForcasA2 = [V2]
ForcasA3 = [V3,H3,M3]

for i in range(0,QtdApoios): 
    if Apoio[o] == Fixo:
        ForcasT[o] = Fixo
        o=o+1
    elif Apoio[o] == Movel:
        ForcasT[o] = Movel
        o=o+1
    else:
        ForcasT[o] = Engaste
        o=o+1

print()  
o=0
SomatoriaX = 0
SomatoriaY = list(range(3))
for i in range(0,3):
    if ForcasT[o] == Fixo:
        SomatoriaX = ForcasA1[1]
        SomatoriaY[o] = ForcasA1[0]
        o=o+1
    elif ForcasT[o] == Movel:
        SomatoriaY[o] = ForcasA2[0]
        o=o+1
    else:
        SomatoriaX = ForcasA3[0]
        SomatoriaY[o] = ForcasA3[2]
i=0
o=0

H1 = SomatoriaX
H2 = SomatoriaX
V2 = (PosForcaC*IntensidadeF)/TamanhoBarra
V1 = IntensidadeF - V2

print()
print("RESULTADOS:")
print()
print(f"Ha: {H1} N")
print(f"Va: {V1} N")
print(f"Hb: {H2} N")
print(f"Vb: {V2} N")
