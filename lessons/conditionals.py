# Practicing Conditionals

def less_than_10(num: int) -> bool:

# Tells us if num < 10
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:
        print("Small number.")
    else:
        print("Large  number.")
    
print(less_than_10(num=2))

def wake_up(alarm: bool) -> str:
    #Returns a message if the alarm is going off
    if alarm is True:
        return "Wake up!"
    else:
        return "Keep sleeping!"    

print(wake_up(alarm=False))