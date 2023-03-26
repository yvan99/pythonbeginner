weight = input("Weight: ")
weighType = input("(K)g or (L) bs :")

if weighType.upper() == "K":
   convertedWeight = float(weight) * 0.453592
   print("Weight in " +  str(weighType)  +"is" + str(convertedWeight))

else:
   convertedWeight = float(weight) * 0.453592
   print("Weight in " + str(weighType) +"is" + str(convertedWeight))