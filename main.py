from art import logo
from replit import clear
#HINT: You can call clear() to clear the output in the console.
print (logo)
dictionary={}
print("Welcome to secret auction program.")
name=input("What is your name?: ")
bid=int(input("What's your bid?: $"))
dictionary[name]=bid

yes_no=input("Are there any other bidders? Type 'yes' or 'no'.")
while yes_no=="yes":
  clear()
  name=input("What is your name?: ")
  bid=int(input("What's your bid?: $"))
  dictionary[name]=bid
  yes_no=input("Are there any other bidders? Type 'yes' or 'no'.")
  


max=0
winner=""
for name in dictionary:
  
  if dictionary[name]>max:
    max=dictionary[name]
    winner=name
    
clear()
print(f"The winner is {winner} with a bid of {max}")