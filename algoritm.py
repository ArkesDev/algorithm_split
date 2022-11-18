
frase=input("Dimmi una frase: ")
print(frase.split())
print(len(frase.split()))
conta_parole=0
ex_lettera="S"
for lettera in frase:
    if conta_parole==0:
        conta_parole=+1
        if lettera == " "and lettera !=ex_lettera :
                conta_parole= conta_parole+1
        ex_lettera=lettera
print("Questa frase contine", conta_parole, "parole")
