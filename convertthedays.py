days=int(input("Enter the number of days: "))
year=days//365
weeks=((days%365)//7)
days=((days%365)%7)
print("Number of years :",year)
print("NUmber of weeks:",weeks)
print("Number of days:",days)