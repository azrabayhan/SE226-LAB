class Vehicle:
    def __init__(self, vid, model, year):
        self.vid = vid
        self.model = model
        self.year = year

    def __str__(self):
        return f"VID: {self.vid} | {self.model} ({self.year})"

    def __eq__(self, other):
        return self.vid == other.vid

    def is_new(self, n):
        return self.year >= (2026 - n)


class Car(Vehicle):
    def __init__(self, vid, model, year, fuel_type, doors):
        super().__init__(vid, model, year)
        self.fuel_type = fuel_type
        self.doors = doors

    def __str__(self):
        return f"[Car] VID: {self.vid} | {self.model} ({self.year}) | Fuel: {self.fuel_type} | {self.doors} Doors"


class Truck(Vehicle):
    def __init__(self, vid, model, year, max_load, axles):
        super().__init__(vid, model, year)
        self.max_load = max_load
        self.axles = axles

    def __str__(self):
        return f"[Truck] VID: {self.vid} | {self.model} ({self.year}) | Load: {self.max_load}kg | {self.axles} Axles"


class Motorcycle(Vehicle):
    def __init__(self, vid, model, year, engine_cc, type):
        super().__init__(vid, model, year)
        self.engine_cc = engine_cc
        self.type = type

    def __str__(self):
        return f"[Motorcycle] VID: {self.vid} | {self.model} ({self.year}) | Eng: {self.engine_cc}cc | Type: {self.type}"


def save_fleet_to_file(vehicles, filename):
    file = open(filename, "w")

    for vehicle in vehicles:
        if isinstance(vehicle, Car):
            file.write(
                f"Car,{vehicle.vid},{vehicle.model},{vehicle.year},{vehicle.fuel_type},{vehicle.doors}\n"
            )

        elif isinstance(vehicle, Truck):
            file.write(
                f"Truck,{vehicle.vid},{vehicle.model},{vehicle.year},{vehicle.max_load},{vehicle.axles}\n"
            )

        elif isinstance(vehicle, Motorcycle):
            file.write(
                f"Motorcycle,{vehicle.vid},{vehicle.model},{vehicle.year},{vehicle.engine_cc},{vehicle.type}\n"
            )

    file.close()


def load_fleet_from_file(filename):
    vehicles = []
    file = open(filename, "r")

    for line in file:
        data = line.strip().split(",")

        if data[0] == "Car":
            vehicle = Car(data[1], data[2], int(data[3]), data[4], int(data[5]))

        elif data[0] == "Truck":
            vehicle = Truck(data[1], data[2], int(data[3]), int(data[4]), int(data[5]))

        elif data[0] == "Motorcycle":
            vehicle = Motorcycle(data[1], data[2], int(data[3]), int(data[4]), data[5])

        vehicles.append(vehicle)

    file.close()
    return vehicles



v1 = Car("V001", "Tesla Model 3", 2023, "Electric", 4)
v2 = Car("V002", "Toyota Corolla", 2018, "Petrol", 4)

v3 = Truck("T101", "Volvo FH16", 2019, 25000, 6)
v4 = Truck("T102", "Mercedes Actros", 2021, 18000, 4)

v5 = Motorcycle("M301", "Yamaha R1", 2024, 998, "Sport")
v6 = Motorcycle("M302", "Harley Davidson", 2015, 1200, "Cruiser")

fleet = [v1, v2, v3, v4, v5, v6]

save_fleet_to_file(fleet, "fleet.txt")

print("Loading fleet data from 'fleet.txt'...")
loaded_fleet = load_fleet_from_file("fleet.txt")
print(len(loaded_fleet), "vehicles loaded successfully.")

print("\n--- All Vehicles ---")
for vehicle in loaded_fleet:
    print(vehicle)

print("\n--- Recent Vehicles (Last 4 Years) ---")
for vehicle in loaded_fleet:
    if vehicle.is_new(4):
        print(vehicle)

print("\n--- Electric Cars Only ---")
for vehicle in loaded_fleet:
    if isinstance(vehicle, Car) and vehicle.fuel_type == "Electric":
        print(vehicle)