from reading import listed#imports listed 
import reading
import datetime
def borrow():
    f=open("invoice.txt","a+")#creating invoice file inside the function so that the file is created when the function is called
    f.write("--------------------------------------invoice of library----------------------------------------")#writing value in invoice
    time=str(datetime.datetime.now())#assign converter dateand time to a variable
    f.write("\t\t\t"+time)#use the converted variable to have the date an dtime
    f.write("\n"+"\tYou have borrowed"+" " )
    f.close()
    while True:
        reading.read()#calling the function inside the while loop 
        try:#first try this then if any error occurs then the exceopt code is run
            book=input("Enter the book no. from above list: ")#asking the usr to enter the book code
            if book=="c01":
                book1=int(input("How many book of \"Brokenwing \"you want to borrow:"))
                if (book1>int(listed[0][2]) or int(listed[0][2])<0):#comparing the user inputvalue with the listed quantity value to check the no of book
                    print("Out of stock")
                    continue
                else:
                    print("you have borrowed ",book1,"of"+" "+listed[0][0])
                    listed[0][2]=str(int(listed[0][2])-book1)#list is updated as per the vlue given by ht user
                    f=open("invoice.txt","a")
                    f.write(str(book1)+" "+"book of Brokenwing")
                    f.write("\n \tTotal book borrowed:"+str(book1))
                    f.write("\n \tRate of 1 book($):"+listed[0][3])
                    f.write("\n \tTotal amount:"+str(book1*int(listed[0][3]))+"$")
                    f.close()
                   
            elif book=="c02":
                book2=int(input("How many book of \"Muna Madan \"you want to borrow:"))
                if (book2>int(listed[1][2]) or int(listed[1][2])<0):
                    print("out of stock")
                    continue
                else:
                    print("you have borrowed ",book2,"of"+" "+listed[1][0])
                    listed[1][2]=str(int(listed[1][2])-book2)
                    f=open("invoice.txt","a")
                    f.write(str(book2)+" "+"book of Muna Madan")
                    f.write("\n \tTotal book borrowed:"+str(book2))
                    f.write("\n \tRate of 1 book($):"+listed[1][3])
                    f.write("\n \tTotal amount:"+str(book2*int(listed[1][3]))+"$")
                    f.close()
                    
            elif book=="c03":
                book3=int(input("How many book of \"Summer love\" you want to borrow:"))
                if book3>20:
                    print(book3>int(listed[2][2]) or int(listed[2][2])<0)
                    continue
                else:
                    print("you have borrowed ",book3,"of"+" "+listed[2][0])
                    listed[2][2]=str(int(listed[2][2])-book3)
                    f=open("invoice.txt","a")
                    f.write(str(book3)+" "+"book of Brokenwing")
                    f.write("\n \tTotal book borrowed:"+str(book3))
                    f.write("\n \tRate of 1 book($):"+listed[2][3])
                    f.write("\n \tTotal amount:"+str(book3*int(listed[2][3]))+"$")
                    f.close()
                    
            elif book=="c04":
                book4=int(input("How many book of \"Programming Python \" you want to borrow:"))
                if (book4>int(listed[3][2]) or int(listed[3][2])<0):
                    print("Out of stock")
                    continue
                else:
                    print("you have borrowed",book4,"of"+" "+listed[3][0])
                    listed[3][2]=str(int(listed[3][2])-book4)
                    f=open("invoice.txt","a")
                    f.write(str(book4)+" "+"book of Brokenwing")
                    f.write("\n \tTotal book borrowed:\t"+str(book4))
                    f.write("\n \tRate of 1 book($):\t"+listed[3][3])
                    f.write("\n \tTotal amount"+str(book4*int(listed[3][3]))+"$")
                    f.close()
            else:
                print("!!please enter the valid no from above list")
                continue
            f=open("invoice.txt","a")
            f.write("\n------------------------lending duration is 10 days--------------------------")#writing value in invoice
            f.write("\n-----------------------------VISIT-AGAIN--------------------------------------")#writing value in invoice
            f.close()
   
        except (SyntaxError):
            print("Value not recognized. Retry")
            continue
        ask=input("Do you want to Borrow anything(y/n)")
        
        if ask=="y":
            continue
        else:
            
            print("Thank you for visiting ")
            break

    
    
    
    
    
    

    

            
    
    
    
        
        
