x, y, w, h = map(int, input().split())
distance = []
distance.append(h - y)
distance.append(w - x)
distance.append(y - 0)
distance.append(x - 0)
print(min(distance))