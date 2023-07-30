class Car:
    def __init__(self, fuel, wheels) :
        self.fuel = fuel
        self.wheels = wheels
        

# 클래스명(상속받을 클래스명)
class Bike(Car):
    def __init__(self, fuel, wheels, size):
        # super()로 부모 클래스를 지정
        super().__init__(fuel, wheels)
				# 또는 Car.__init__(self, fuel, wheels)로 직접 지정도 가능
        self.size = size

bike = Bike("gas", 2, "small")
print (bike.fuel, bike.wheels, bike.size) 