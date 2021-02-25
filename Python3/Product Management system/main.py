class Product:
  def __init__(self,productId,productName,productPrice,stockQuantity,reorderingQuantity,ownerName):
    self.productId=productId
    self.productName=productName
    self.productPrice=productPrice
    self.stockQuantity=stockQuantity
    self.reorderingQuantity=reorderingQuantity
    self.ownerName=ownerName

class ProductManagementSystem:
  def __init__(self,productList):
    self.productList=productList
  
  def getMaxProductPrice(self,Oname):
    pricelist=[]
    for i in self.productList:
      if str.lower(i.ownerName) == str.lower(Oname):
        pricelist.append(i.productPrice)
    if not pricelist:
      return None
    else:
      return max(pricelist)
  
  def isStockAvailable(self,Pdctname):
    productlist=[]
    for i in self.productList:
      if str.lower(Pdctname) == str.lower(i.productName) and (i.stockQuantity <= i.reorderingQuantity) :
        productlist.append(i)
    if not productlist:
      return None
    else:
      return productlist


# --------inputs-----------#
t=5
productobjlist=[]
for i in range(t):
    productId=int(input())
    productName=input()
    productPrice=int(input())
    stockQuantity=int(input())
    reorderingQuantity=int(input())
    ownerName=input()
    temp=Product(productId,productName,productPrice,stockQuantity,reorderingQuantity,ownerName)
    productobjlist.append(temp)

PMSobject=ProductManagementSystem(productobjlist)
Oname=input()
Pdctname=input()


#1st question
answer1=PMSobject.getMaxProductPrice(Oname)
if answer1 != None:
  print(answer1)
else:
  print("Product Not Found.")

#2nd question
answer2=PMSobject.isStockAvailable(Pdctname)
#print(answer2)
if answer2 != None:
  for i in answer2:
    print(i.productId,i.stockQuantity)
else:
  print("Product Not Found.")
