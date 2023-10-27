import random
# Restaurant Menu
menu = [['Rice',30],['Roti',10],['Kadhi chawal',30],['Dal',35],['Mixed Veg',50],['Bhindi Masala',45],
        ['Chilly chicken',60],['Malabar chicken',90],['Veg Soup',30],['Non Veg Soup',45]]
j=0
# Generating orderID
orderID = random.randint(0,9)
def orderid():
    for i in range(0,5):
      orderID = orderID + random.randint(0,9)

def neworder():
   N=input('Please select the no. of dishes you would like to choose')
   order = [{
      'orderID':orderid()
      dish=input(): price=input()
      quantity: a=input()
      total quantity: int(price)*int(a),
      }]
   while( j<N):
      dict= {dish=input(): price=input()
      'quantity': a=input()
      'total quantity': int(price)*int(a),
      }
      order.append(dict)
      j+=1
   j=0
   for j<N:
      Grandtotal =  dict['total quantity'] 