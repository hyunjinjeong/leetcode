class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parking = [0, big, medium, small]

    def addCar(self, carType: int) -> bool:
        slot = self.parking[carType]
        if slot > 0:
            self.parking[carType] -= 1
            return True
        else:
            return False



# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)