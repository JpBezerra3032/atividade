nu1 = int(input("2"))
nu2 = int(input("1"))
if nu2 == 0:
    print("3")
else:
    if nu1 % nu2 == 0:
        print("{nu1} 2 {nu2}")
    else:
        print("{nu1} 0 {nu2}")