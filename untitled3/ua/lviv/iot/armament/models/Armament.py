from ua.lviv.iot.armament.models.ApartmentType import ApartmentType
from ua.lviv.iot.armament.models.User import User
from ua.lviv.iot.armament.models.Use import Use
from ua.lviv.iot.armament.models.Power import Power

class Armament:

    def __init__(self,
                 type=ApartmentType.PISTOLS, price=0.0,
                 power=Power.LOW, use=Use.DEFENSE,
                 user=User.COLDIER, amount=0):

        self.type = type
        self.price = price
        self.power = power
        self.use = use
        self.user = user
        self.amount = amount



    def __str__(self):

        return ', '.join((f"{name} = {value}" for name, value in self.__dict__.items()))