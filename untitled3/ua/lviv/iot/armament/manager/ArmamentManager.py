import sys
sys.path.insert(0, '../models')
from ua.lviv.iot.armament.models.Armament import Armament
from ua.lviv.iot.armament.models.ApartmentType import ApartmentType
from ua.lviv.iot.armament.models.Power import Power
from ua.lviv.iot.armament.models.Use import Use
from ua.lviv.iot.armament.models.User import User
from ua.lviv.iot.armament.models.Grenade import Grenade
from ua.lviv.iot.armament.models.Pistol import Pistol
from ua.lviv.iot.armament.models.SniperRifles import SniperRifles
from ua.lviv.iot.armament.models.SpecialAutomotiveEquipment import SpecialAutomotiveEquipment

class ArmamentManager:
    def __init__(self, *args):
        self.armaments = args

    @staticmethod
    def sortByPrice(armaments, descending=False):
        return sorted(armaments, key=lambda armament: armament.price, reverse=descending)

    @staticmethod
    def sortByPriceAscending(armaments):
        return ArmamentManager.sortByPrice(armaments)

    @staticmethod
    def sortByPriceDescending(armaments):
        return ArmamentManager.sortByPrice(armaments, True)

    @staticmethod
    def sortByAmount(armaments, descending=False):
        return sorted(armaments, key=lambda armament: armament.amount, reverse=descending)

    @staticmethod
    def sortByAmountAscending(armaments):
        return ArmamentManager.sortByAmount(armaments)

    @staticmethod
    def sortByAmountDescending(armaments):
        return ArmamentManager.sortByAmount(armaments, True)

    # return [security for security in self.securities if security.pricePerUnit == price]

    def filterByType(self, type):
        return list(filter(lambda armament: armament.type == type, self.armaments))

    def filterByPower(self, power):
        return list(filter(lambda armament: armament.power == power, self.armaments))

    def filterByUser(self, user):
        return list(filter(lambda armament: armament.user == user, self.armaments))

def main():
    armaments = [
        Armament(ApartmentType.PISTOLS, 1500, Power.LOW, Use.ATTACK, User.CIVIL, 3),
        Grenade(ApartmentType.GRENADES, 3000, Power.HIGH, Use.DEFENSE, User.CIVIL, 5, "Best", 2),
        Pistol(ApartmentType.SNIPERDEVISE, 2500, Power.MIDDLE, Use.DEFENSE, User.COLDIER, 6, "Germany", 3),
        SniperRifles(ApartmentType.PISTOLS, 2000, Power.LOW, Use.ATTACK, User.CIVIL, 9, "English", "Musya"),
        SpecialAutomotiveEquipment(ApartmentType.SNIPERDEVISE, 4000, Power.HIGH, Use.DEFENSE, User.COLDIER, 1, "First", "TANK")
    ]
    manager = ArmamentManager(*armaments)

    filteredList = manager.filterByType(0)
    for s in filteredList:
        print(s)
    print()

    sortedList = ArmamentManager.sortByPriceAscending(armaments)
    for s in sortedList:
        print(s)
    print()

    sortedFilteredList = ArmamentManager.sortByAmountDescending(filteredList)
    for s in sortedFilteredList:
        print(s)

if __name__ == '__main__':
    main()