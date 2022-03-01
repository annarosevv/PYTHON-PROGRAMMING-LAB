cyr=int(input("Enter the Current year: "))
fyr=int(input("Enter the Future year:  "))
for cyr in range(cyr,fyr):
    if (cyr % 400 == 0)or(cyr % 4 == 0) and (cyr % 100 != 0):
        print(cyr ,"It is a  leap year ")
    else:
        print(cyr,"It is  not a leap year")
