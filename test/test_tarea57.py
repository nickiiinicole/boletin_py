import pytest
from dataclasses import FrozenInstanceError # error que da instanciar mal dataclass frozen
from src.boletines.tarea57 import User
from src.boletines.gamin_exception import Gamin_exception
@pytest.fixture
def tarjeta_valida():
    return "1111111111111"
@pytest.fixture
def tarjeta_invalida_luhn():
    return "11111111111111"
# test para crear los usuarios: 
def test_usuario_sin_targe():
    user = User("nicka", "Perez", "1221234")
    assert user.card_number is None

def test_usuario_tarjeta_valida(tarjeta_valida):
    u = User("Luis", "Mariahno", "46564", card_number=tarjeta_valida)
    assert u.card_number == tarjeta_valida

# test para validar la formula de lunh
def test_tarjeta_muy_corta():
    with pytest.raises(Gamin_exception, match="format"):
        User("maricarkmren", "pepe", "0034", "408976")

def test_tarjeta_con_letras():
    with pytest.raises(Gamin_exception, match="format"):
        User("Pepe", "Sanz", "7564", "1n5678901633a")

def test_tarjeta_checksum_incorrecto(tarjeta_invalida_luhn):
    with pytest.raises(Gamin_exception, match="Invalid Luhn"):
        User("Noel", "martiinex", "3212", tarjeta_invalida_luhn)

#test de inmutabilidad es decir no se puede modifciar mas adelante
def test_usuario_es_inmutable():
    user = User("nicka", "Perez", "1221234")
    
    with pytest.raises(FrozenInstanceError):
        user.name = "jesuuu"
