from datetime import datetime

Name=input("Enter the name: ")
# list of items
Lists='''
      Rice           Rs     45/kg
        Salt           Rs     20/kg
        Sugar          Rs     14/kg
        Pepsi          Rs     50/ltr
        Sunflower oil  Rs    140/ltr
        Coconut oil    Rs    250/ltr
        Milk           Rs     60/ltr
        closeup        Rs     250/kg
        '''

items={'Rice':45,
       'Salt':20,
       'Sugar':14,
       'Pepsi':50,
       'Sunflower oil':140,
       'Coconut oil':250,
       'Milk':60,
       'Closeup':250}
Price=0
Pricelist=[]
Totalprice=0
Finalprice=0
ilist=[]
qlist=[]
plist=[]

proceed=int(input("For list of itmes press 1: "))
if proceed==1:
    print(Lists)
for i in range(len(items)):
    welcome=int(input("to buy press 1 or to exit press 2: "))
    if welcome==2:
        break
    if welcome==1:
        item=input("Enter items: ")
        quantity=int(input("Enter no of quantities: "))
        if item in items.keys():
            price=quantity*(items[item])
            Pricelist.append((item,quantity,items,price))
            Totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            Gst=(Totalprice*4.5)/100
            Finalamount=Totalprice+Gst
        else:
            print("Sorry! not available this item")
    else:
        print("you entered wrong input")
    bill=input("Are you proceed with these items Yes or No: ")
    if bill=='Yes':
        pass
        if Finalamount!=0:
            print(25*"*","Mr&Mrs supermarket",25*"*")
            print(30*" ","Bapatla")
            print("Name:",Name,30*' ',"Date:",datetime.now())
            print(75*"-")
            print("s.no",8*' ',"item",8*' ',quantity,3*' ',"price")
            for i in range(len(Pricelist)):
                print(i,8*" ",ilist[i],5*' ',qlist[i],3*' ',plist[i])
            print(75*"-")
            print(50*" ","Totalprice:",'Rs',Totalprice)
            print("gst amount",50*" ",'Rs',Gst)
            print(75*"-")
            print(50*" ",'Finalamount:','Rs',Finalamount)
            print(75*"-")
            print(20*" ","Thanks For Visiting")
            print(75*"-")
            for i in range(len(Pricelist)):
                print(i,ilist[i],qlist[i],plist[i])

