n=str(input("minim 3 caractere:"))
cuvant=""
lista=[]
for x in n:
    if x==' ' :
        lista.append(cuvant)
        cuvant=""
    else:
        cuvant+=x
        print(cuvant)
print(lista)
