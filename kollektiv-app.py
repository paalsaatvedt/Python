
def billettapp():
    if alder<5:
        pris=0
    elif alder==5 or alder>=20:
        pris=20
    elif alder==21 or alder>=25:
        pris=50
    elif alder==26 or alder>=60:
        pris=80
    elif 60<alder:
        pris=0
    if sykkel=="j":
        pris+=50
    print("prisen blir", pris)

alder=int(input("skriv inn alderen din: "))
sykkel=input("har du sykkel? j/n: ")

billettapp()