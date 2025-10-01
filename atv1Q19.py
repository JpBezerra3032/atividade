a = float(input("digite seu peso"))
b = float(input("digite sua altura"))
c = a/(b**2)
if(c<18.5):
    print("abaixo do peso")
elif c<=24.9:
    print("peso normal")
elif c<=29.9:
    print("sobrepeso")
else:
    print("obesidade")
    