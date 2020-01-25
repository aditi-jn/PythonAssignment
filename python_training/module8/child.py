from automobile import *

class Car(Automobile):
    def __init__(self,make,model,mileage,price,doors):
        Automobile.__init__(self,make,model,mileage,price)
        self.__doors=doors

    def set_doors(self,doors):
        self.__doors=doors
    def get_doors(self):
        return self.__doors

class Truck(Automobile):
    def __init__(self,make,model,mileage,price,drive_type):
        Automobile.__init__(self, make, model, mileage, price)
        self.__drive_type=drive_type

    def set_drive(self, drive_type):
        self.__drive_type = drive_type

    def get_drive(self):
        return self.__drive_type

class SUV(Automobile):
    def __init__(self, make, model, mileage, price,pass_cap):
        Automobile.__init__(self,make,model,mileage,price)
        self.__pass_cap=pass_cap

    def set_pass_cap(self, pass_cap):
        self.__pass_cap= pass_cap

    def get_pass_cap(self):
        return self.__pass_cap
def main():
    c1=Car(2017,'Swift',60,2000000,4)
    t1=Truck(2019,'Halo Nation',70,500000,5)
    s1=SUV(2000,'Jeep Wrangler ',60,666666,55)
    print("Details of  Car \nMake :",c1.get_make(),"\nModel :",c1.get_model(),"\nMileage :",c1.get_mileage(),"\nPrice :",c1.get_price(),"\nDoors :",c1.get_doors())
    print("\nDetails of  Truck \nMake :",t1.get_make(),"\nModel :",t1.get_model(),"\nMileage :",t1.get_mileage(),"\nPrice :",t1.get_price(),"\n Drive Type :",t1.get_drive())
    print("\nDetails of  SUV \nMake :",s1.get_make(),"\nModel :",s1.get_model(),"\nMileage :",s1.get_mileage(),"\nPrice :",c1.get_price(),"\nPass Cap",s1.get_pass_cap())

main()