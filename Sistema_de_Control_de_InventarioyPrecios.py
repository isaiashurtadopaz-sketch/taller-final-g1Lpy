class Producto:
    def __init__(self, nombre: str, precio_inicial: float):
        self.__nombre = nombre
        self.__precios_historicos = []
        
        # Usamos el setter para validar también el precio inicial
        self.nuevo_precio = precio_inicial

    # Getter para obtener el nombre (opcional, ayuda a las pruebas)
    @property
    def nombre(self):
        return self.__nombre

    # Getter para ver la lista de precios históricos
    @property
    def precios_historicos(self):
        return self.__precios_historicos

    # 2. Propiedad para calcular el precio promedio del producto
    @property
    def precio_promedio(self):
        if not self.__precios_historicos:
            return 0.0
        return sum(self.__precios_historicos) / len(self.__precios_historicos)

    # 3. Setter para la actualización e inserción de precios con validación
    @property
    def nuevo_precio(self):
        # Devuelve el último precio registrado si existe
        return self.__precios_historicos[-1] if self.__precios_historicos else None

    @nuevo_precio.setter
    def nuevo_precio(self, valor: float):
        if valor < 0 or valor > 10000:
            print(f"⚠️ ADVERTENCIA: El precio ${valor} está fuera de rango (0 - 10,000). No se registró.")
        else:
            # 1. Registra el nuevo precio en el historial si es válido
            self.__precios_historicos.append(valor)
            print(f"✅ Precio de ${valor} registrado con éxito para '{self.__nombre}'.")


# --- PRUEBA DE REGISTRO DE DATOS (EJERCICIO 1) ---
print("=== PRUEBAS EJERCICIO 1 ===")
# Crear un producto con un precio inicial válido
prod = Producto("Computador Portátil", 1500.0)

# 1. Registrar nuevos precios válidos usando el setter
prod.nuevo_precio = 1600.0
prod.nuevo_precio = 1450.0

# 3. Intentar registrar valores inválidos (debe lanzar advertencias)
prod.nuevo_precio = -50.0
prod.nuevo_precio = 12000.0

# Mostrar historial final y promedio calculado
print(f"\nHistorial de precios de {prod.nombre}: {prod.precios_historicos}")
print(f"Precio promedio final: ${prod.precio_promedio:.2f}")
