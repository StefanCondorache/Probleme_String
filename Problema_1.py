n=str(input("string:"))
nr_mare=0
nr_cifre=0
nr_chr=0
for x in n:
    if ord(x)>=65 and ord(x)<=90:
        nr_mare+=1
    elif ord(x)>=48 and ord(x)<=57:
        nr_cifre+=1
    elif ord(x)>=40 and ord(x)<=43 or ord(x)==45 or ord(x)==47 or ord(x)==91 or ord(x)==93 or ord(x)==123 or ord(x)==125:
        nr_chr+=1
print(nr_mare,"LITERE MARI")
print(nr_cifre,"cifre")
print(nr_chr,"caractere specializate")
