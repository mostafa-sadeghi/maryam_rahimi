def cycle(my_list, c, count):
    index = my_list.index(c)
    print(f"we start from {c}")
    for i in range(count):
        x = (index+1) % len(my_list)
        print(my_list[x])
        index += 1


print("first test")
trafficLights = ["green", "orange", "red"]
cycle(trafficLights, "green", 3)
print("second test")
cycle(trafficLights, "orange", 5)
print("third test")
hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
cycle(hours, 10, 5)
print("forth test")
cycle(hours, 12, 0)
