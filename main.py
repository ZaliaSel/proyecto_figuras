from lib import cuadrado, rectangulo
print("Proyecto Figuras")
print(cuadrado.get_identificador())
lado=4
print(f"El area de un {cuadrado.get_indentificador()} de lado {lado} es: {cuadrado.get_area(lado)} y el perimetro es {cuadrado.get_perimetro(lado)}")

base=4
altura=2
print(triangulo.get_identificador())
print(f"El area de un {triangulo.get_identificador()} de base {base} y altura {altura} y el perimetro es {triangulo(base,base,base)}")