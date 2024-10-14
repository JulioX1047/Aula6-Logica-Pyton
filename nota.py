cont=0
soma=0
while cont<4 :
 nota=float(input("Qual sua nota"))
 cont+=1
 soma+=nota
 med=soma/cont

if med>=6 :
 print("Vc foi aprovado")
else :
 print("Vc foi reprovado")
 
print(f"{med} é a media ")
