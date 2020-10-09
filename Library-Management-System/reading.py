#declaring listed ans list variable and appending the value to the list
listed=[]
file=open("booklist.txt","r")
file_read=file.readlines()
for i in file_read:
    a=i.replace("\n","").split(",")# replacing the \n with empty string and then spliting the file
    listed.append(a)#the value is appended to the in list which is named as listed
file.close()

def read():
    print("Following books are available in our library")
    print("---------------------------------------------------------------------------------------------------------------------")
    print("S.N.\t\t\tBook\t\t\t\tAuthor\t\t\tQuantity\t\tPrice($)")
    print("---------------------------------------------------------------------------------------------------------------------")
    for j in range(len(listed)):
        print("C0"+str(j+1),"\t\t",listed[j][0],"\t\t\t",listed[j][1],"\t\t",listed[j][2],"\t\t\t",listed[j][3])
    print("---------------------------------------------------------------------------------------------------------------------")

        
