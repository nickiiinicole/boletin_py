from datetime import datetime
from src.boletines.Inmobiliaria import Inmobiliaria, Inmueble_A, Inmueble_B

def test_precio_negativo_0():
    last_year = datetime.now().year - 5
    apartamento = Inmueble_A(año=last_year, metros=100, habitaciones=2, garaje=True)
    
    assert apartamento.precio > 0 