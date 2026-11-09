class Envio:
    def __init__(self, peso_kg: float, distancia_km: float):
        self.peso_kg = peso_kg
        self.distancia_km = distancia_km

    def calcular_costo(self, monto_base: float) -> float:
        # Método base (será sobreescrito por las subclases)
        return monto_base


# B. Subclase EnvioEstandar
class EnvioEstandar(Envio):
    def calcular_costo(self, monto_base: float) -> float:
        # A. Recargo del 5% sobre el monto base
        return monto_base * 1.05


# B. Subclase EnvioExpress
class EnvioExpress(Envio):
    def calcular_costo(self, monto_base: float) -> float:
        # B. Recargo del 15% sobre el monto base
        return monto_base * 1.15


# --- PRUEBA DE REGISTRO DE DATOS (EJERCICIO 2) ---
print("\n=== PRUEBAS EJERCICIO 2 ===")

# 2. Crear una lista mixta de envíos (Polimorfismo)
lista_envios = [
    EnvioEstandar(peso_kg=5.0, distancia_km=120.0),
    EnvioExpress(peso_kg=2.0, distancia_km=450.0),
    EnvioEstandar(peso_kg=15.0, distancia_km=30.0),
    EnvioExpress(peso_kg=1.5, distancia_km=800.0)
]

# Recorrer la colección ejecutando el mismo método en diferentes clases
monto_base_paquete = 50000.0 # Supongamos un valor base de $50,000 para la prueba

print(f"Calculando costos para un monto base de: ${monto_base_paquete:,}\n")

for i, envio in enumerate(lista_envios, start=1):
    # Obtenemos el nombre de la clase actual para identificarla en el print
    tipo_envio = envio.__class__.__name__
    costo_final = envio.calcular_costo(monto_base_paquete)
    
    print(f"Envío #{i} [{tipo_envio}]:")
    print(f"   - Peso: {envio.peso_kg} kg | Distancia: {envio.distancia_km} km")
    print(f"   - Costo Total con recargo: ${costo_final:,.2f}")
