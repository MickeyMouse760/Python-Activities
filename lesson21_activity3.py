weather = (1,0,0,0,1,1,0)
rain = 0
sun = 0
for i in range(0,7):
    if weather[i]==0:
        sun+=1
    else:
        rain+=1
if sun>rain:
    print("good weather")
else:
    print("bad weather")