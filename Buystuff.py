username=input("Enter Your Name: ") #taking input
print("Greetings👋   Mr/Ms",username,"!! Buy anything with the price equal to your age!") #printing username
while True: #inclduding user_age to the loop to avoid crashing code
  try:
      user_age=float(input("enter your age: "))
      
      break
  except ValueError:
    print("Kindly enter in numerical form:")
if user_age>=19: #condition1 if the age is equal to more than 19
  print("Buy without discount:$",user_age) #price with no discount
else:
  print("Buy with 50% discount🎉: $", user_age/2) #price with discount
print("Happy Shopping✅  ")