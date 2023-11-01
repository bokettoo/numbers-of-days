def determine_the_number_of_days():
 month=int(input("enter the number of month"))
 if month in {1,3,5,7,9,11} :
  print("31")
 elif month in {4,6,8,10,12} :
  print("30")
 elif month == "2":
  print("28 or 29")