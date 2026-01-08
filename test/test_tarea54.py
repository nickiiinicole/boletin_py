import pytest
from datetime import datetime
# Ajusta esta línea si tu carpeta se llama distinto, 
# pero asumo que está en src/boletines/Inmobiliaria.py
from src.boletines.Inmobiliaria import Inmueble_A, Inmueble_B, buscar_inmueble

@pytest.fixture
def piso_a():
    """Crea un piso Zona A para pruebas matemáticas."""
    # Argumentos: año, metros, habitaciones, garaje
    return Inmueble_A(2000, 100, 3, True)

@pytest.fixture
def piso_b():
    """Crea un piso Zona B para pruebas matemáticas."""
    # Argumentos: año, metros, habitaciones, garaje
    return Inmueble_B(2000, 100, 3, True)


def test_precio_positivo():
    """Comprobamos que el precio no sale negativo ni cosas raras."""
    year = datetime.now().year - 5
    piso = Inmueble_A(year, 100, 2, True)
    assert piso.precio > 0 

def test_calculo_precio_zona_a(piso_a):
    """Verificar fórmula Zona A."""
    antiguedad = datetime.now().year - 2000
    
    precio_base = (100*1000 + 3*5000 + 15000) # 130.000
    factor = 1 - (antiguedad / 100)
    
    esperado = precio_base * factor
    
    # acordarse de usar aprox para los decimales
    assert piso_a.precio == pytest.approx(esperado)

def test_calculo_precio_zona_b(piso_b):
    """Verificar fórmula Zona B (x1.5)."""
    antiguedad = datetime.now().year - 2000
    base_a = (100*1000 + 3*5000 + 15000) * (1 - antiguedad/100)
    
    esperado = base_a * 1.5
    
    assert piso_b.precio == pytest.approx(esperado)

def test_anio_futuro_error():
    futuro = datetime.now().year + 1
    with pytest.raises(ValueError, match="inválido"):
        Inmueble_A(futuro, 100, 2, False)

def test_metros_negativos_error():
    with pytest.raises(ValueError, match="metros"):
        Inmueble_A(2000, -50, 2, False)

def test_habitaciones_negativas_error():
    with pytest.raises(ValueError, match="habitaciones"):
        Inmueble_A(2000, 100, -1, False)


def test_buscador_funciona():
    # 1. Creamos 3 pisos con precios muy distintos
    piso_barato = Inmueble_A(1980, 60, 1, False) # ~Barato
    piso_medio  = Inmueble_A(2010, 90, 3, True)  # ~Medio
    piso_caro   = Inmueble_B(2022, 200, 5, True) # ~Muy Caro 

    lista = [piso_barato, piso_medio, piso_caro]

    corte = (piso_medio.precio + piso_caro.precio) / 2

    resultado = buscar_inmueble(lista, corte)

    assert piso_barato in resultado
    assert piso_medio in resultado
    assert piso_caro not in resultado