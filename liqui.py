po=float(input("Qual preço original  "))
desconto=float(input("Qual o desconto vc quer aplicar em percentual "))
porc=desconto*(1/100)
pf=po- (po*porc)
print(f"{pf} É o preço final ")