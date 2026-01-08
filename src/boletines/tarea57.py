from dataclasses import dataclass

@dataclass(frozen=True)
class User: 
    name : str
    surname : str
    username : str
    password : str
# el 1 or eque si es none pasa a valar none
    card_number : str | None= None

    def __post_init__(self): 
        self.card_number.strip()

    def check_sum(self,card_number):
        '''La fórmula de Lunh'''
        if len(card_number.strip())<13 or not card_number.isdigit() : 
            raise Gamin_exception("Invalid card number")
        # digits_odd = self.card_number[::2]
        # digits_odd = [int(digit) for digit in digits_odd]
        # digits_odd = [digit*2 for digit in digits_odd]
        # hacerlo en una linea 
        digits_odd = [int(digit) * 2 for digit in card_number[::2]]
        
        modified_digits = [digit - 9 if digit > 9 else digit for digit in digits_odd]
        remaining_digits = [int(digit) for digit in card_number[1::2]]

        total_digits = sum(modified_digits) + sum(remaining_digits)
        
        if total_digits%10 ==0 :
            return True
        else: 
            raise Gamin_exception("ERROR, INVALID COMPROBATION LUHN:/// ")
    
        