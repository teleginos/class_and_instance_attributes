class Building:
    total = 0

    def __init__(self):
        Building.total += 1


list_building = []

for i in range(40):
    house = Building()
    print(house)
    list_building.append(house)


print(f"Общее количество созданных зданий: {Building.total}")
