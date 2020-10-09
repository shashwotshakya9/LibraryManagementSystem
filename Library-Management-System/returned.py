from reading import listed
import datetime
import reading
def returned():
    w=open("return_invoice.txt","a")
    w.write("---------------------Return-Book-Invoice----------------------")
    time=str(datetime.datetime.now())
    w.write("\t\t\t"+time)
    w.write("\nyou have returned")
    w.close()
    while True:
        reading.read()
           #asking for usr to input the valid book id of which book you want to return    
        print("which book you want to return")
        choice=input("please inter the book code you want to return:")
        c1=int(input("how many days you have book:"))
        if c1>10:
            print("!!!Extra charge for late returning(0.25$ for each day!!!)")#promting the late submission error
            a=str((c1-10)*0.25)#fine been charged according to the extra no of days they have kept the book for 
            
        if choice=="c01":
            cho1=int(input("how many book you want to return"))
            listed[0][2]=str(int(listed[0][2])+cho1)
            w=open("return_invoice.txt","a")
            w.write(str(cho1)+" "+"books")
            w.close()
            
        elif choice=="c02":
            cho2=int(input("how many book you want to return"))
            listed[1][2]=str(int(listed[1][2])+cho2)
            w=open("return_invoice.txt","a")
            w.write(str(cho2)+" "+"books")
            w.close()

        elif choice=="c03":
            cho3=int(input("how many book you want to return"))
            listed[2][2]=str(int(listed[1][2])+cho3)
            w=open("return_invoice.txt","a")
            w.write(str(cho3)+" "+"books")
            w.close()

        elif choice=="c04":
            cho4=int(input("how many book you want to return"))
            listed[3][2]=str(int(listed[3][2])+cho4)
            w=open("return_invoice.txt","a")
            w.write(str(cho4)+" "+"books")
            w.close()

        else:
            print("Enter a valid book id")
            continue
        if c1>10:
            
            w=open("return_invoice.txt","a")
            w.write("\nfine for late Submission($):"+a)
            w.close()
            
        w=open("return_invoice.txt","a")
        w.write("---------------------------Visit-Again----------------------------")
        w.close()

        other=input("Do you want to return any other book (y/n)")
        if other=="y":
            
            continue
        
        else:
            print("Thank you for visiting")
            break
        

