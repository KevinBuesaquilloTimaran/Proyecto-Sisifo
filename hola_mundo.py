nombre: str = "Kevin"
edad: int = 20
precio_producto: float = 25000.0

def calcular_IVA(precio: float) -> float:
    return precio * 0.19  # IVA 19% Colombia

print(f"IVA a pagar: ${calcular_IVA(precio_producto):.2f}")