from field import Field

class Phone(Field):
        def __init__(self, number):
          self.value = self.validate(number)

        def validate(self, number): 
            
            if not number.isdigit(): 
                raise ValueError("Only digits")
            
            if len(number) != 10: 
                raise ValueError("Only 10 digits")
              
            return number