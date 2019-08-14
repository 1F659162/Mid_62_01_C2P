import random
n1 = n2 = n3 = n4 = n5 = n5 = n6 = 0

print("Random number 1 to 6")
print("----------------------------------------------------------------------------------")
for i in range(1,100+1):
    r = random.randint(1,6)
    print("\t",r, end = ' ')
    if i % 10 == 0 :
        print()
    if r == 1 :
        n1 += 1
    if r == 2 :
        n2 += 1
    if r == 3 :
        n3 += 1
    if r == 4 :
        n4 += 1
    if r == 5 :
        n5 += 1
    if r == 6 :
        n6 += 1
print("----------------------------------------------------------------------------------")
print()
print(f"Number    Requency")
print(f"  1          {n1}")
print(f"  2          {n2}")
print(f"  3          {n3}")
print(f"  4          {n4}")
print(f"  5          {n5}")
print(f"  6          {n6}")

