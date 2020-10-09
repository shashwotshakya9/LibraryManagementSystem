
import reading #imports the reading module
import borrow #imports the borrow 
import returned
print("\t\t\t\tWelcome to the library")
user=input("Please enter your name:")#asking the user name before the while loop so that same user need not to enter their name again and again
while True:
   
    choice=input("Hey"+" "+user+" "+"you want to borrow(1) or return(2) the book :") #asking user to make chooice betn borrowing and returning the book
    
    if choice =="1":
        n=open("invoice.txt","a")
        n.write("name of the borrower:"+" "+user)
        n.close()
        borrow.borrow()#if the user wants to borrow then only calling this function

    elif choice=="2":
        b=open("return_invoice.txt","a")
        b.write("name of the returner:"+" "+user)
        b.close()
        returned.returned()#if the user wants to return the book then only Calling this function

    else:
        print("not a valid input")#if user enter except 1 or 2 this pritns out and the program is reiterated with the help of continue function
        continue
    user1=input("do you want to return to the main menu(y/n)")
    if user1=="y":#after borrowing or returning the book if the user wants to borrow or returns the book 
        continue#then they can do so as the program is reiterated from the while loop with the help of this continue function
    else:
        print("Thank you for visiting")
        break#else if they dont want any more transaction then the program is breaked from here        
        
    
    



