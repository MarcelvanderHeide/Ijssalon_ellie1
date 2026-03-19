def mijn_functie_1(a):
    return a ** 2
    
print(mijn_functie_1(2))
print(mijn_functie_1(4))
print(mijn_functie_1(10))
print(mijn_functie_1(12))

def mijn_functie_2(a, b):
    if b== 0:
        raise ValueError("Deling door nul is niet toegestaan.")
    
    op = a + b
    af = a - b
    maal = a * b
    delen = a / b
    if isinstance(delen, float) and delen.is_integer():
        delen = int(delen)
   
    return [op, af, maal, delen]

print(mijn_functie_2(12, 3))
print(mijn_functie_2(12, 2))
print(mijn_functie_2(10, 5))
print(mijn_functie_2(100, 20))