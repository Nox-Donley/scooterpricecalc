def main():
    miles = 0.0
    kilometers = 0.0
    mok = input("miles or kilometers")
    if (mok == "miles" or mok == "Miles" or mok == "m" or mok == "M"):
        miles = int(input("What is the distance of your trip in miles?"))
        kilometers = miles * 1.60934
        print("your distance in miles is", miles, "and your distance in kilometers is", kilometers)
    elif (mok == "kilometers" or mok == "Kilometers" or mok == "k" or mok == "K"):
        kilometers = int(input("What is the distance of your trip in kilometers?"))
        miles = kilometers / 1.60934
        print("your distance in kilometers is", kilometers, "and your distance in miles is", miles)
    else:
        print("not an option")
    time = miles / 15
    CompanyA = 1 + ((time*60)*0.15)
    CompanyB = 0.0
    if (time*60) > 5:
        CompanyB = 2.50 + ((time*60)*0.12)
    elif (time*60) < 5:
        CompanyB = ((time*60)*0.50)
    CompanyC = 5 + ((time*60)*0.06)
    timeround = round(time, 2)
    CompanyAR = round(CompanyA, 2)
    CompanyBR = round(CompanyB, 2)
    CompanyCR = round(CompanyC, 2)
    print("your trip should take", timeround, "hours, at a rate of 15 miles per hour")
    print("Using Company A will cost you $", CompanyAR)
    print("Using Company B will cost you $", CompanyBR)
    print("Using Company C will cost you $", CompanyCR)
    if (CompanyAR < CompanyBR and CompanyAR < CompanyCR):
        print("Company A will be the cheapest for this trip")
    if (CompanyBR < CompanyAR and CompanyBR < CompanyCR):
        print("Company B will be the cheapest for this trip")
    if (CompanyCR < CompanyBR and CompanyCR < CompanyAR):
        print("Company C will be the cheapest for this trip")
main()