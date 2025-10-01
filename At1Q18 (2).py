numero = int(input("numero"))
d = {
    1: "domingo",
    2: "segunda-feira",
    3: "terca-feira",
    4: "quarta-feira",
    5: "quinta-feira",
    6: "sexta-feira",
    7: "sabado"}
if 1 <= numero <=7:
    print("O dia corresponde")
else:
    print("nao corresponde")