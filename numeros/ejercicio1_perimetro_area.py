# ejercicio1_perimetro_area.py
# Versión final: con input() para base y altura
base = float(input("Introduce la base del rectángulo: "))
altura = float(input("Introduce la altura del rectángulo: "))

perimetro = 2 * (base + altura)
area = base * altura

print("Base =", base, "Altura =", altura)
print("Perímetro:", perimetro)
print("Área:", area)
