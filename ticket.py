print("WELCOME TO  MOVIE TICKET BOOKING SYSTEM")

lst = list()
for i in range(1,20):
   lst.append(i)
fname = list()
for j in range(1,20):
   fname.append(j)
lname = list()
for k in range(1,20):
   lname.append(k)
agep = list()
for i in range(1,20):
   agep.append(i)
r = 1
while r!=0:

    print("1.Book ticket")
    print("2.Check Ticket Status")
    print("3.Cancel ticket")
    print("4.Check detail of booked ticket")
    print("5.Exit")

    choice = int(input("\nEnter your option:")) 


    if choice==1:
         tic = int(input('Enter seat no:'))
         if lst[tic-1]==tic:
            fname1 = str(input('Enter your first name:\n'))
            lname1 = str(input('Enter your last name:\n'))
            age1 = int(input('Enter your age:\n'))
            lst.pop(tic-1)
            fname.pop(tic-1)
            lname.pop(tic-1)
            agep.pop(tic-1)
            lst.insert(tic-1,'B')
            fname.insert(tic-1,fname1)
            
            lname.insert(tic-1,lname1)
            agep.insert(tic-1,age1)
            print('\n************************')
            print("your Ticket is booked")
            print('************************\n')
         else: 
            print('\n************************')
            print('seat is already booked try other seat')
            print('***************************\n')

    elif choice==2:
       for k in lst:
          print(k,end="\t")

    elif choice==3:
      tic=int(input('Enter seat no'))
      if lst[tic-1]==tic:
            print('\n*************************')
            print("This seat is not Booked")
            print('***********************\n')
      else:
                lst.pop(tic-1)
                lst.insert(tic-1,tic)
                print('\n************************')
                print('your ticket is canceled')
                print('**************************\n')

    elif choice==4:
      s = int(input('Enter seat no\n'))
      s = s-1
      if fname[s]==s+1:
            print('\n**********************')
            print('this seat is not booked')
            print('***********************\n')


      else:
            print('\n**********************')
            print('Customer Name is:',fname[s].title(),lname[s].title(),'and Age is:',agep[s])
            print('************************\n')
                
    elif choice==5:
      r=0
      exit()



    else:
        print('\n**********************')
        print('you are enter wrong key\n')
        print('************************\n')
        
                      
                               
