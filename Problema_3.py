n1=str(input(":"))
n2=str(input(":"))
n3=str(input(":"))
n4=str(input(":"))
cuvant=""
if len(n1)>3 and len(n2)>3 and len(n3)>3 and len(n4)>3:
    cuvant+=n1[0:2]+n2[0]+n3[0:3]+n4[0:len(n4)//2]
print(cuvant)
