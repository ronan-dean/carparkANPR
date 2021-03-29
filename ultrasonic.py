from recognition.ultrasonicdriver import distance
dis = distance()
if dis <= 25:
    print("car found taking pic")
    print(dis)
if dis <= 24:
    print("car too close")
if dis >= 30:
    print("car too far")

