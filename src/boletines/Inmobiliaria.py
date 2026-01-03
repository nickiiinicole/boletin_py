from dataclasses import dataclass
from datetime import datetime
@dataclass
class Inmobiliaria(): 
    año:int
    metros:float
    habitaciones:int
    garaje: bool 

    @property
    def antiguedad(self)->int: 
        return datetime.now().year- self.año
    
    def precio(self)->float: 
        # acordarse que python deja muitplicar booleanos trnasoformando susvalores en 0 y en 1
        return (self.metros*1000+self.habitaciones*5000+self.garaje*1500)*1(1-self.antiguedad)

@dataclass
class Inmueble_A(Inmobiliaria):
    @property
    def precioA(self)->float:
        return self.precio()

@dataclass
class Inmueble_B(Inmobiliaria):
    @property
    def precioA(self)->float:
        return self.precio()*1.5
    

def procura_inmueble(lista_pisos: list[Inmobiliaria], pre):

    