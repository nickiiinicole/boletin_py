# -----------------------------------------------------------------------------
# 1. DECORADOR REUTILIZABLE (DRY)
# -----------------------------------------------------------------------------
# Como temos 3 atributos (plato, piñon, suspensión) que seguen a MESMA regra 
# (non negativos e cambio de 1 en 1), facemos un decorador para non repetir código.

def validar_cambio_gradual(func):
    """
    Valida que o novo valor non sexa negativo e que 
    a diferenza co valor anterior non sexa maior de 1.
    """
    def wrapper(self, novo_valor):
        if novo_valor < 0:
            print(f"Error: O valor {novo_valor} non pode ser negativo.")
            return

        # 2. Validar o cambio gradual (só de 1 en 1)
        # Necesitamos ler o valor actual. Usamos o nome da función (propiedade)
        # para saber que variable interna (_variable) ler.
        nome_variable = "_" + func.__name__
        valor_actual = getattr(self, nome_variable)

        # Calculamos a diferenza absoluta (para arriba ou para abaixo)
        diferenza = abs(novo_valor - valor_actual)

        if diferenza > 1:
            print(f"Error: Non se pode cambiar {func.__name__} de {valor_actual} a {novo_valor} de golpe.")
            return 

        # 3. Se todo está ben, executamos o setter orixinal
        return func(self, novo_valor)
    
    return wrapper
class Bicicleta:
    # Constructor con valores por defecto
    def __init__(self, velocidadActual=0, platoActual=1, piñonActual=1):
        # Inicializamos as variables privadas directamente para evitar 
        # que o decorador salte no __init__ (porque no inicio non hai "cambio", hai creación)
        self._velocidadActual = max(0, velocidadActual)
        self._platoActual = max(0, platoActual)
        self._piñonActual = max(0, piñonActual)

    @property
    def velocidadActual(self):
        return self._velocidadActual

    @velocidadActual.setter
    def velocidadActual(self, valor):
        if valor < 0:
            print("A velocidade non pode ser negativa.")
        else:
            self._velocidadActual = valor

    @property
    def platoActual(self):
        return self._platoActual

    @platoActual.setter
    @validar_cambio_gradual  
    def platoActual(self, valor):
        self._platoActual = valor

    @property
    def piñonActual(self):
        return self._piñonActual

    @piñonActual.setter
    @validar_cambio_gradual # <--- Reutilizamos a lóxica
    def piñonActual(self, valor):
        self._piñonActual = valor

    def acelerar(self):
        """Duplica a velocidade. Se é 0, pasa a 1."""
        if self.velocidadActual == 0:
            self.velocidadActual = 1
        else:
            self.velocidadActual = self.velocidadActual * 2

    def frear(self):
        """Reduce á metade (enteira)."""
        self.velocidadActual = self.velocidadActual // 2

    def __str__(self):
        return f"[Bici] Vel: {self.velocidadActual}, Plato: {self.platoActual}, Piñon: {self.piñonActual}"

