from dataclasses import dataclass
from datetime import datetime
@dataclass
class Inmobiliaria(): 
    año:int
    metros:float
    habitaciones:int
    garaje: bool 

#este metodo se ejecutaria después del init 
    def __post_init__(self):
        current_year = datetime.now().year

        # Valide que no sea del futuro
        # tb le puse lo de 1800 por si acaso osea mete algo muy antiguo ...
        if self.año > current_year or self.año<1800:
            raise ValueError(f"El año {self.año} es inválido.")

        # Valide que los metros sean lógicos
        if self.metros <= 0:
            raise ValueError("Los metros deben ser mayores a 0.")

        # Valide habitaciones puedes ser 0 por ejemplo si es un estudio... 
        if self.habitaciones < 0:
            raise ValueError("No puedes tener habitaciones negativas.")

    @property
    def antiguedad(self)->int: 
        return datetime.now().year- self.año
    
    def precio_base(self)->float: 
        # acordarse que python deja multiplicar booleanos trnasoformando susvalores en 0 y en 1
        valor_garaje = 15000 * self.garaje # True es 1, False es 0
        return (self.metros*1000+self.habitaciones*5000+valor_garaje)*(1-self.antiguedad/100)

@dataclass
class Inmueble_A(Inmobiliaria):
    @property
    def precio(self)->float:
        return self.precio_base()

@dataclass
class Inmueble_B(Inmobiliaria):
    @property
    def precio(self)->float:
        return self.precio_base()*1.5
    

def buscar_inmueble(lista_apartam: list[Inmobiliaria], presupuesto_max: float):
    
    apartam_filtrad = [i for i in lista_apartam if i.precio <= presupuesto_max]

    return apartam_filtrad
    