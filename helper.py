def decoreer(tekst=""):
    tekst="header"
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()

def fooi_pp(bedrag, persoon):
    bedrag_pp = bedrag/persoon
    return f"het bedrag per persoon is {bedrag_pp} euro"

def ondersteep(tekst=""):
    uit = []
    uit.append(tekst)
    uit.appens(len/(tekst) * "=")
    return uit


def som(dictionary):
    totaal = 0
    for waarde in dictionary.values():
        totaal += waarde
    return totaal
