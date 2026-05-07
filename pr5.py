# import time
print("hellow welcome to our cofee shop : ")
list = []


resorces = { 
    "tea":"without sugar "        ,                                                                      
    "water" :"water with sugar with",
    "blacktea":"without milk with",
    "coffe":"normal coffee with ",
    "coffee":"with full choclate  with ",
        
}
print(resorces)
i = input("Enter your favorite drink : ")

if i in resorces:
 d = list.append(i)
 print(list,"thankyou!!")
 

weffers  = {
    "oreo":"bestesss ever",
    "parle":"you will like it",
    "tosses":"test good with tea",
    
}
print(weffers)
p = input("give me your loving weffers ")
if p in weffers:
 g = list.append(p)
print(list)