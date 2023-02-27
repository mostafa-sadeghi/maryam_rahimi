def cycle(trafficLights, color, count):
    index = trafficLights.index(color)
    print(f"we start from {color}")

    for i in range(count):
        x = (index+1) % len(trafficLights)
        print(trafficLights[x])
        index += 1


print("first test")
trafficLights = ["green", "orange", "red"]

cycle(trafficLights, "green", 3)

print("second test")
cycle(trafficLights, "orange", 5)
