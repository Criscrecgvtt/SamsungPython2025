s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60, 70}
print("1) s1 | s2  →", s1 | s2)             # Unió
print("2) s1 & s2 →", s1 & s2)             # Intersecció
print("3) s1 - s2 →", s1 - s2)             # Diferència
print("4) s1 ^ s2 →", s1 ^ s2)             # Diferència simètrica
print("5) s1.issubset(s2) →", s1.issubset(s2))       # És subconjunt?
print("6) s1.issuperset(s2) →", s1.issuperset(s2))   # És superconjunt?
print("7) s1.isdisjoint(s2) →", s1.isdisjoint(s2))   # Són disjunts?