from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs * (1 - korting)
    return (
        f"Vandaag in de aanbieding: (1 liter) in de smaak {smaak}, "
        f"van {prijs} euro voor {nieuwe_prijs:.2f} euro"
        )

print(aanbieding_1("aardbei", 4, 0.1))

def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw
    return (
        f"Het totaal van alle inkomsten deze week is {totaal:.2f} euro, "
        f"waarover {btw_bedrag:.2f} euro btw betaald dient te worden."
        )

week_inkomsten = [220, 430, 125, 160, 205, 90, 345]
print (inkomsten_totaal(week_inkomsten, 0.09))

def laag_en_hoog(mijn_lijst):
    return [max(mijn_lijst), min(mijn_lijst)]

inkomsten = [220, 430, 125, 160, 205, 90, 345]
print (laag_en_hoog(inkomsten))

def gemiddeld(mijn_lijst):
    gemiddelde = sum(mijn_lijst) / len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde:.2f} euro."

inkomsten = [220, 430, 125, 160, 205, 90, 345]
print(gemiddeld(inkomsten))

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

print(meervoudig([10,5,3,2,1,2,9]))

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    return mijn_functie_2(korte_lijst[0], korte_lijst[1])

invoer_lijst_2 = [10,5,3,2,1,2,9]
print(combinatie(invoer_lijst_2))
