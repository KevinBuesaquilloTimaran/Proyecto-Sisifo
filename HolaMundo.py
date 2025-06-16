nombre: str = "Tu nombre"
edad: int = 20
precio: float = 10000.0

def calcular_IVA(precio: float) -> float:
    return precio * 1.19  # IVA 19% Colombia

print(calcular_IVA(precio))