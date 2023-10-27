class Menu:
    def __init__(self):
        self.orders=[]
    def addOrder(self,order):
        self.orders.append(order)
    def printData(self,order):
        if order not in self.orders:
            print("Order is not available")
        else:
            print(order)
s1=Menu()

print("="*50)
print("welcome to Inzamaam's Dhaba")
print("="*50)
print("1.add order")
print("2.see order")
print("3.Quit")
print("-"*50)

choice=input("Please Enter your Choice: ")

while True:
    if choice=="1":
        order=("Please Enter what you want to order: ")
        s1.addOrder(order)
    elif choice=="2":
        s1.printData()
    elif choice=="3":
        break
    else:
        print("invalid input")
