from ua.lviv.iot.armament.models.Armament import Armament
from ua.lviv.iot.armament.models.ApartmentType import ApartmentType
from ua.lviv.iot.armament.models.Power import Power
from ua.lviv.iot.armament.models.Use import Use
from ua.lviv.iot.armament.models.User import User

class Pistol(Armament):

    def __init__(self,

                 type=ApartmentType.PISTOLS, price=0.0,
                 power=Power.LOW, use=Use.DEFENSE,
                 user=User.COLDIER, amount=0,
                 caliber=0, origin="NoName"

                 ):

        super(Pistol, self).__init__(
            type, price,
            power, use,
            user, amount

        )

        self.origin = origin
        self.caliber = caliber