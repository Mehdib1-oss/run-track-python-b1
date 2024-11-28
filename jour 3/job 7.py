a = float(input("Entrez la longueur du côté a : "))
b = float(input("Entrez la longueur du côté b : "))
c = float(input("Entrez la longueur du côté c : "))

if a + b > c and a + c > b and b + c > a:
    print("Ces longueurs forment un triangle.")
    
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Le triangle est rectangle.")
        
        if a == b or a == c or b == c:
            print("Le triangle rectangle est isocèle.")
    elif a == b == c:
        print("Le triangle est équilatéral.")
    elif a == b or a == c or b == c:
        print("Le triangle est isocèle.")
    else:
        print("Le triangle est quelconque.")
else:
    print("Ces longueurs ne peuvent pas former un triangle.")

