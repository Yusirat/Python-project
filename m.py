Item={'Sugar':[131,50],'Bread(sliced)':[311,200],'Bread(unsliced)':[229,150],'Egg':[545,50],'Three crown(tin)':[201,150],'Peak milk(tin)':[230,120],'Peak milk(sachet)':[791,50],'Bournvita(sachet)':[611,50],'Milo(tin)':[367,500],'Peak milk (Large Sachet)':[889,700],'Milo (Large Sachet)':[934,700],'Bournvita (Large Sachet)':[758,100],'Custard (small sachet)':[383,200],'Corn flakes (small sachet)':[647,150],'Golden morn (small sachet)':[121,100],'Detergent (small Wawu)':[198,120],'Detergent (small Aerial)':[354,115],'Detergent (Big Wawu)':[323,200],'Detergent (Big Aerial)':[222,250],'Corn flakes (big sachet)':[341,750],'Golden morn (Large sachet)':[458,650],'Sprite (small)':[134,80],'Pepsi (small)':[674,80],'Fanta (small)':[757,80],'Lacasera (small)':[127,80],'Sprite (big)':[956,150],'Pepsi (big)':[374,150],'Fanta (big)':[267,150],'Lacasera (big)':[786,150],'Coke (big)':[546,150]}

def PriceOfGoods():
    print ("{:^30}|{:^15}".format("Item","Price"))
    print ('{:^35}'.format("----------------------------------------"))

    for i in Item.keys():
        p=Item[i][1]
        print("{:^30}|{:^15}".format(i,p))
        
def PriceAndQuantity ():
    print ("{:^27}|{:^5}|{:^5}".format("Item","Price","Quantity"))
    print ('{:^35}'.format("----------------------------------------"))

    for i in Item.keys():
        p=Item[i][1]
        print("{:^27}|{:^5}|{:^5}".format(i,p,Item[i][0]))
 
              
def buy():         
    c=input('what do you want to buy: ').split(',')
    d=input('Enter corresponding prices: '). split (',')
    item=dict(zip(c,d))
    print ('Are these what you want? ',item)    
    T=0; 
    for i in c:
        if i in Item:
            j=eval(item[i])*Item[i][1]
            T+=j
            if len(c)<5:
                Tp=(120*T/100)
            elif len(c)>10:
                Tp=(130*T/100)
            elif len(c)>10 and Item[i]>=100:
                Tp=T+800
            else:
                Tp=T    
             
        
                     
                
    print ('Items purchased are:',"\n")
    
    
    print("{:^20}|{:^10}|{:^5}".format('Item bought', 'Quantity','price'))
    print ('{:^35}'.format("----------------------------------------"))
    for i in item.keys():
        if i in Item:
            j=eval(item[i])*Item[i][1]
            Item[i][0]=Item[i][0]-int(item[i]) 
            print ("{:^20}|{:^10}|{:^5}".format(i,item[i],j))
        else:
            print (i," is not available")
            continue
    print ("\n")         
    print (f"Total payment is {Tp} \n")
   


def check ():
    while True:
        d=input("Enter an Item to change its price: ")
        dp=input("Enter new price: ")
    
        if d=="done":
            print ("Price Updated")
            
            break
        elif d in Item:
            Item[d][1]=dp
            continue
        else:
             q=input ("quantity of new item:")
           
             Item[d]=[q,dp]
             continue
    PriceAndQuantity()         
        
    


def user():
    while True:
        l=[]
        n=input ("Are you Admin or User? ")
        if n=="Admin":
            PriceAndQuantity()
            check()
          
        elif n=="User":
            s=input("Enter your name: \n ")
            print ("Welcome "+s)
            PriceOfGoods()
            buy()
        
        
            print ("Thank you",s)
            l.append(n)
        else:
            print ("You have to be an Admin or User \n",)
            print ('kindly check the price list of our available goods')
            PriceOfGoods() 
            quit ()   

user()

 



              


      
    
    
   
    
       
