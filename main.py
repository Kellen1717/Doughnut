print("Hello, welcome to Kellen's doughnuts")
:
  print ("what kind of doughnut do you want")
  myorder=input ("A - chocolate B - glazed C - strawbarry")
  toppings=""
  order=""

  if(myorder == "A" ):
    toppings=input ("would you like sprikles")
    order="chocolate doughnut"
  elif(myorder == "B"):
    toppings=input ("would you like it warm")
    order="glazed doughnuts"
  elif(myorder == "C"): 
    toppings=input ("would you like extra strawbarrys")
    order="strawbarry doughnuts"
  print (" thank you for your order of a " +order +toppings)






