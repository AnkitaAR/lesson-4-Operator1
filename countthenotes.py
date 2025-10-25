amount=int(input("Enter the amount to withdraw: "))
hundrednote=amount//100
fiftynote=(amount%100)//50
tennote=((amount%100)%50)//10
print("Number of hundred notes are: ",hundrednote)
print("Number of fifty notes are: ",fiftynote)
print("Number of tens notes are: ",tennote)