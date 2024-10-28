def HotelCost(Nights):
    return 140*Nights
def planeridecost(City):
    if "Lahore"==City:
        return 183
    elif "Tokyo"==City:
        return 220
    elif "Hong Kong"==City:
        return 222
    elif "California"==City:
        return 475
def RentalCarCost(Days):
    if Days>=7:
        return 40*Days-50
    elif Days>=3:
        return 40*Days-20
    else:
        return 40*Days
def TripCost(City,Days,SpendingMoney):
    return RentalCarCost(Days)+HotelCost(Days)+planeridecost(City)+SpendingMoney
print("Cost of Car Rental ",RentalCarCost(5))
print("Cost of Plane Ride ",planeridecost("Tokyo"))
print("Cost of Hotel Room ", HotelCost(7))
print("Total cost of Trip ",TripCost("Tokyo",7,500))
    
