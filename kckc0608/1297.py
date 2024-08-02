d, h, w = map(int, input().split())
y = ((d**2) / (1+(w*w)/(h*h)))**0.5

print(int(y), int(w/h*y))
