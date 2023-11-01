import math
def Booking():
    print("\nWelcome to the Room Booking Portal of Hotel Paradise!!!\n")
    list_1= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    list_2= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    list_3= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    list_4= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    list_5= [1,2,3,4,5]
    list_6= [1,2,3,4,5,6,7,8,9,10]
    number_rooms= int(input("enter the number of rooms: "))
    room=1
    for room in range(1,number_rooms+1):
      print("\nThe room options available are: \n")
      print("Press 1 for Single Bed Non AC Room")
      print("Press 2 for Single Bed AC Room")
      print("Press 3 for Double Bed Non AC Room")
      print("Press 4 for Double Bed AC Room")
      print("Press 5 for Non AC Suite")
      print("Press 6 for AC Suite")
      print("Press 7 for quit")
      choice= int(input("enter your choice: "))
      if choice==1:
          list_room1=[]
          print("You have been allocated the room number ", list_1[0])
          r = list_1[0]
          del list_1[0]
          name = input("enter your name: ")
          dict_= {'customer_name':name, 'room_no':r, 'room_type':'single bed Non AC', 'charges':150 }
          list_room1.append(dict_)
          print("Customer Details -\n")
          print(list_room1)
      elif choice==2:
          list_room2=[]
          print("You have been allocated the room number ", list_2[0])
          r = list_2[0]
          del list_2[0]
          name = input("enter your name: ")
          dict_= {'customer_name':name, 'room_no':r, 'room_type':'single bed AC', 'charges':250 }
          list_room2.append(dict_)
          print("Customer Details -\n")
          print(list_room2)
      elif choice==3:
          list_room3=[]
          print("You have been allocated the room number ", list_3[0])
          r = list_3[0]
          del list_3[0]
          name = input("enter your name: ")
          dict_= {'customer_name':name, 'room_no':r, 'room_type':'double bed Non AC', 'charges':500 }
          list_room3.append(dict_)
          print("Customer Details -\n")
          print(list_room3)
      elif choice==4:
          list_room4=[]
          print("You have been allocated the room number ", list_4[0])
          r = list_4[0]
          del list_4[0]
          name = input("enter your name: ")
          dict_= {'customer_name':name, 'room_no':r, 'room_type':'double bed AC', 'charges':600 }
          list_room4.append(dict_)
          print("Customer Details -\n")
          print(list_room4)
      elif choice==5:
          list_room5=[]
          print("You have been allocated the room number ", list_5[0])
          r = list_5[0]
          del list_5[0]
          name = input("enter your name: ")
          dict_= {'customer_name':name, 'room_no':r, 'room_type':'Non AC Suite', 'charges':1000 }
          list_room5.append(dict_)
          print("Customer Details -\n")
          print(list_room5)
      elif choice==6:
          list_room6=[]
          print("You have been allocated the room number ", list_6[0])
          r = list_6[0]
          del list_6[0]
          name = input("enter your name: ")
          dict_= {'customer_name':name, 'room_no':r, 'room_type':'AC Suite', 'charges':1200 }
          list_room6.append(dict_)
          print("Customer Details -\n")
          print(list_room6)
      elif choice==7:
          break
      room=room+1


def Restaurant():
  #Class for breakfast entries
  bEntries = ["Upma","FrenchToast","Cheese Sandwich","Chole Bhature","Masala Dosa"]

  #class for breakfast sides
  bSides = ["Eggs","Puri","Toast","Fruit salad","Samosa"]

  #Class for lunch entries
  lEntries = ["Veg Pulao","Fried Rice","Egg curry","Chicken Biriyani","Chilli Paneer"]

  #class for lunch sides
  lSides = ["Plain Rice","Masala Kulcha","Soup","Tandoori Chicken","Raita"]

  #class for dinner entries
  dEntries = ["Butter chicken", "Paneer kadhai", "Mutton curry", "Mushroom curry"]

  #class for dinner sides
  dSides = ["Roti", "Masala Papad", "Salad", "Butter Naan"]

  #Class for drinks
  Drinks = ["Water","Fruit Juice","Assorted Mocktails","Cold Drinks","Masala Soda"]


  #FIRST PROMPT WELCOME
  dineWithus=input("\nWelcome to the Restaurant! Would you like to dine with us today? [Y/N]")
  if dineWithus =="N":
    print("Have a nice day!.")
  if dineWithus=="Y":
    amountCustomer=int(input("How many will be dining with us today?"))


  #define my breakfast menu
  breakfastMenu = ["Pancake 100rs, Frech Toast 100rs, Chicken Fried Steak 100rs, Omlet 100rs, Scramble 100rs,Eggs 100rs, Bacon 100rs, Toast, 100rs, Fruit 1$, Sausage 100rs"]
  #define my lunch menu
  lunchMenu = ["Burger 100rs, Chili 100rs, Sandwich 100rs, Hotdog 100rs, Chicken 100rs, Fries 100rs, Rolls 100rs, Salad 100rs, Gormet Nachos 100rs"]
  #define my drink menu
  drinkmenu=["Water 100rs, Juice 100rs, Milk 100rs, Soda 100rs, Beer 100rs"]

  grandTotal=0

  #Possible Counters
  orderNumber=1
  x=0
  y=0
  counter = 1
  counter2 = 1
  drinkOrder = 0


  while orderNumber <= amountCustomer:
    print("Customer Order Number:",orderNumber)
    order=input("Would you like to order breakfast,lunch or dinner?[B/L/D]")
    i=0
    j=0

    #LOOP FOR BREAKFAST ENTRIES
    if order == "B":
      while i < len(bEntries):
        print("Breakfast menu is",i+1,bEntries[i])
        i += 1
      entrieB = int(input("Which would you like? "))
      if entrieB == 1:
        print("You have chosen",bEntries[0])
        grandTotal+=100
      if entrieB == 2:
        print("You have chosen",bEntries[1])
        grandTotal+=100
      if entrieB == 3:
        print("You have chosen",bEntries[2])
        grandTotal+=100
      if entrieB == 4:
        print("You have chosen",bEntries[3])
        grandTotal+=100
      if entrieB == 5:
        print("You have chosen",bEntries[4])
        grandTotal+=100

      #LOOP FOR BREAKFAST SIDES
      while j < len(bSides):
        print("Breakfast sides are",j+1,bSides[j])
        j += 1
      sideB = int(input("Which would you like? "))
      if sideB == 1:
        print("You have chosen",bSides[0])
        grandTotal+=100
      if sideB == 2:
        grandTotal+=100
        print("You have chosen",bSides[1])
        grandTotal+=100
      if sideB == 3:
        print("You have chosen",bSides[2])
        grandTotal+=100
      if sideB == 4:
        print("You have chosen",bSides[3])
        grandTotal+=100
      if sideB == 5:
        print("You have chosen",bSides[4])
        grandTotal+=100

    #LUNCH ENTRIES LOOP
    l = 0
    if order == "L":
      while l < len(lEntries):
        print("Lunch options are",l+1,lEntries[l])
        l += 1
      entrieL = int(input("Which would you like? "))
      if entrieL == 1:
        print("You have chosen",lEntries[0])
        grandTotal+=100
      if entrieL == 2:
        print("You have chosen",lEntries[1])
        grandTotal+=100
      if entrieL == 3:
        print("You have chosen",lEntries[2])
        grandTotal+=100
      if entrieL == 4:
        print("You have chosen",lEntries[3])
        grandTotal+=100
      if entrieL == 5:
        print("You have chosen",lEntries[4])
        grandTotal+=100

      #LUNCH SIDES LOOP
      k = 0
      while k < len(lSides):
        print("Side options are",k+1,lSides[k])
        k += 1
      sideL = int(input("Which would you like? "))
      if sideL == 1:
        print("You have chosen",lSides[0])
        grandTotal+=100
      if sideL == 2:
        print("You have chosen",lSides[1])
        grandTotal+=100
      if sideL == 3:
        print("You have chosen",lSides[2])
        grandTotal+=100
      if sideL == 4:
        print("You have chosen",lSides[3])
        grandTotal+=100
      if sideL == 5:
        print("You have chosen",lSides[4])
        grandTotal+=100

    #DINNER ENTRIES LOOP
    q = 0
    if order == "D":
      while q < len(dEntries):
        print("Lunch options are",q+1,dEntries[q])
        q += 1
      entrieD = int(input("Which would you like? "))
      if entrieD == 1:
        print("You have chosen",dEntries[0])
        grandTotal+=100
      if entrieD == 2:
        print("You have chosen",dEntries[1])
        grandTotal+=100
      if entrieD == 3:
        print("You have chosen",dEntries[2])
        grandTotal+=100
      if entrieD == 4:
        print("You have chosen",dEntries[3])
        grandTotal+=100

      #DINNER SIDES LOOP
      p = 0
      while p < len(dSides):
        print("Side options are",p+1,dSides[p])
        p += 1
      sideD = int(input("Which would you like? "))
      if sideD == 1:
        print("You have chosen",dSides[0])
        grandTotal+=100
      if sideD == 2:
        print("You have chosen",dSides[1])
        grandTotal+=100
      if sideD == 3:
        print("You have chosen",dSides[2])
        grandTotal+=100
      if sideD == 4:
        print("You have chosen",dSides[3])
        grandTotal+=100


    #DRINK LOOP
    d = 0
    drink = input("Woudld you like a drink?[Y/N]")
    if drink =="Y":
      while d < len(Drinks):
        print("Drink options are",d+1,Drinks[d])
        d += 1
      drinkC = int(input("Which would you like? "))
      if drinkC == 1:
        print("You have chosen",Drinks[0])
        grandTotal+=100
      if drinkC == 2:
        print("You have chosen",Drinks[1])
        grandTotal+=100
      if drinkC == 3:
        print("You have chosen",Drinks[2])
        grandTotal+=100
      if drinkC == 4:
        print("You have chosen",Drinks[3])
        grandTotal+=100
      if drinkC == 5:
        print("You have chosen",Drinks[4])
        grandTotal+=100
    orderNumber+=1

  #PRINT TOTAL
  print("\nYour total cost is",grandTotal,"rupees. Thank you for dining with us! Come again!")

def Roomservices():
  print("Welcome to our room service portal")
  print("Dial 101 for room cleaning")
  print("Dial 102 for ordering the food")
  print("Dial 103 for network fixing")
  print("Dial 104 for laundry service")
  print("Dial 105 for electrical appliances")
  print("Dial 106 for any other related problems")

  n=int(input("please dial the number on telephone for the respective enquiry."))
  if n==102:
    Restaurant()
  else:
    print("\nYour query has been recorded.Our staff will be soon reaching to you.")
def Checkout():
  print("\nHope you enjoyed your stay.\nThank You, visit again.\n")
flag=True
while flag==True:
  print("\nHi! Welcome to Hotel Paradise!\nHow can we help you today?\n")
  print("Press 1 for Room Booking")
  print("Press 2 for Dine In")
  print("Press 3 for Room Service")
  print("Press 4 for quit")
  first_input= int(input("enter your choice: "))
  if first_input==1:
      Booking()
  elif first_input==2:
      Restaurant()
  elif first_input==3:
      Roomservices()
  elif first_input==4:
      flag=False
Checkout()