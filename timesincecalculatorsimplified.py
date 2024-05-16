def totaldayscalculator(montha,daya,yeara):
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    totala = 0
    for i in range(montha-1):
        totala += months[i]
    totala += daya

    for i in range(1,yeara):
        if i % 4 != 0 or (i % 100 == 0 and i % 400 !=0): 
            totala += 365 
        else: 
            totala += 366 

    if montha > 2:
        if yeara % 4 != 0 or (yeara % 100 == 0 and yeara % 400 !=0):
            totala += 0
        else:
            totala += 1
    return totala

infoa = input("Please enter the starting date in the following format xx/xx/xxxx: ")
infob = input("Please enter the ending date in the following format xx/xx/xxxx: ")
infoa = infoa.split("/");infob = infob.split("/")
montha = int(infoa[0]);daya = int(infoa[1]);yeara = int(infoa[2])
monthb = int(infob[0]);dayb = int(infob[1]);yearb = int(infob[2])
print(infoa,infob)
beginning = totaldayscalculator(montha,daya,yeara)
ending = totaldayscalculator(monthb,dayb,yearb)

totalx = beginning - ending
print("The amount of time that has passed between the start date and end date is: %d days" % totalx)
print("-This program was created for the date 4/24/2024")