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
    
    def precio_base(self)->float: 
        # acordarse que python deja muitplicar booleanos trnasoformando susvalores en 0 y en 1
        valor_garaje = 15000 * self.garaje # True es 1, False es 0
        return (self.metros*1000+self.habitaciones*5000+valor_garaje)*(1-self.antiguedad)

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
    
    apartam_filtrad = [i for i in lista_apartam if i.precio_base <= presupuesto_max]

    return apartam_filtrad
    