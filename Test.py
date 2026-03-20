# 1. Imprimir texto (print)
print("¡Hola, friend!")
print("Mi nombre es", "VS Code")

# 2. Variables
nombre = "Claudia"
edad = 25
print(f"{nombre} tiene {edad} años")

# 3. Entrada del usuario (input)
nombre = input("¿Cómo te llamas? ")
print(f"¡Hola {nombre}!")

# 4. Operaciones matemáticas
a = 10
b = 3
print(a + b)  # 13
print(a - b)  # 7
print(a * b)  # 30
print(a / b)  # 3.333...
print(a // b) # 3 (división entera)
print(a % b)  # 1 (resto)
print(a ** b) # 1000 (potencia)

# 5. Condicionales (if)
numero = 3
if numero >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# 6. Listas
frutas = ["manzana", "banana", "naranja"]
print(frutas[1])  # manzana
frutas.append("uva")
print(frutas)     # ['manzana', 'banana', 'naranja', 'uva']

# 7. Bucles (for)
for fruta in frutas:
    print(f"Me gusta la {fruta}")
