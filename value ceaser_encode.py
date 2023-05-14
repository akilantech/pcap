value = input("enter the string: ")

delta = int(input("enter delta:"))

result = ''
for e in value:
    if e.isalpha() :
        target = ord(e) + delta
        ordzZ = ord('z') if e.islower() else ord('Z')
        ordaA = ord('a') if e.islower() else ord('A')
        diff = ordzZ - target #65 - 67 = -2
        if diff >= 0 :
            result+=chr(target)
        else:
            derived = (ordaA-1) + abs(diff) 
            result+=chr(derived)
    else:
        result+=e
        
print(result)        