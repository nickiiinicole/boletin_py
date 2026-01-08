from dataclasses import dataclass, field
from .gamin_exception import Gamin_exception
@dataclass(frozen=True)
class User: 
    name : str
    surname : str
    # TODO IMPORTANTE: init=False hace que 'fullname' no se pida en el constructor
    fullname: str = field(init=False)
    password : str
    card_number : str | None= None
# el 1 or eque si es none pasa a valar none

    @staticmethod # le ponemos static porque solo trabaja con el numero que le paso 
    # no mncesita leer
    def check_card_number(card_number):
        '''La fórmula de Lunh'''
        number = card_number.strip()
        
        if len(number) < 13 or not number.isdigit(): 
            raise Gamin_exception("Invalid card number format")
        # digits_odd = self.card_number[::2]
        # digits_odd = [int(digit) for digit in digits_odd]
        # digits_odd = [digit*2 for digit in digits_odd]
        # hacerlo en una linea 
        digits_odd = [int(digit) * 2 for digit in number[::2]]
        
        modified_digits = [digit - 9 if digit > 9 else digit for digit in digits_odd]
        remaining_digits = [int(digit) for digit in number[1::2]]

        total_digits = sum(modified_digits) + sum(remaining_digits)
        
        if total_digits % 10 == 0:
            return True
        else: 
            raise Gamin_exception("ERROR: Invalid Luhn Checksum")
    
    def __post_init__(self): 
        # TODO : Como está frozen, no podemos usar self.fullname = ACORDARSE
        # Tenemos que usar object.__setattr__ para "saltarnos" la protección una vez.
        nombre_completo = f"{self.name} {self.surname}"
        object.__setattr__(self, 'fullname', nombre_completo)
        if self.card_number is not None:
            # comprobamos que exista antes de hacer la comprobacion de tarjeta
            self.check_card_number(self.card_number)
@dataclass
class UserMutable:
    name: str
    surname: str
    password: str
    fullname: str = field(init=False)
    _card_number: str | None = None

    @staticmethod
    def check_card_number(card_number):
        '''La fórmula de Lunh'''
        number = card_number.strip()
        
        if len(number) < 13 or not number.isdigit(): 
            raise Gamin_exception("Invalid card number format")
        digits_odd = [int(digit) * 2 for digit in number[::2]]
        
        modified_digits = [digit - 9 if digit > 9 else digit for digit in digits_odd]
        remaining_digits = [int(digit) for digit in number[1::2]]

        total_digits = sum(modified_digits) + sum(remaining_digits)
        
        if total_digits % 10 == 0:
            return True
        else: 
            raise Gamin_exception("ERROR: Invalid Luhn Checksum")

    def __post_init__(self):
        self.fullname = f"{self.name} {self.surname}"
        
        if self._card_number is not None:
            self.check_card_number(self._card_number)
    @property
    def card_number(self) -> str | None:
        return self._card_number
    @card_number.setter
    def card_number(self, value: str | None):
        if value is not None:
            self.check_card_number(value) 
        
        # Si todo va bien, guardamos
        self._card_number = value



if __name__ == "__main__":
    tarjeta_buena = "49927398716"
    tarjeta_mala = "1234567890123"
    try:
        # Caso Válido
        u1 = User("Ana", "Perez", "1234", "49927398716")
        print("Usuario creado")
        
        # Caso Inválido
        u2 = User("Pepe", "Lopez" "1234", "1234567890123") 
    except Gamin_exception as e:
        print(f"Errorrr")

    #prueba para el que no es inmutable : 
    try:
        u5 = UserMutable("PACO", "Lopez","5324", None)
        print(f"Usuario mutable creado sin tarjeta.")
        
        u5.card_number = tarjeta_buena
        print(f"Tarjeta asignada: {u2.card_number}")

        # Intentamos asignar tarjeta mala
        print("Intentando asignar tarjeta mala...")
        u5.card_number = tarjeta_mala 

    except Gamin_exception as e:
        print(f"EXCEPCIÓN CAPTURADA:D")