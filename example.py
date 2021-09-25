class Vehicle:
    type = "bus"
    colour = "red"
    wheels = 4
    seats = 50


DeansBus = Vehicle()

DeansBus.colour = "blue"
DeansBus.driver = "Dean"

print(DeansBus.colour, DeansBus.driver)
