motorcycles = ['honda', 'yamaha', 'suzuki', ]
print(motorcycles)
too_expensive = 'ducati'
motorcycles.append(too_expensive)
print(motorcycles)
motorcycles.remove(too_expensive)
print(motorcycles)
motorcycles.insert(1, too_expensive)
print(motorcycles)
del motorcycles[3]
print(motorcycles)
print("A " + too_expensive.title() + " is too expensive for me.")
popped = motorcycles.pop()
print(popped)
