class HouseForSale:
  def __init__(self,houseNumber,houseType,salePrice,areaInSqft,isFurnished):
    self.houseNumber=houseNumber
    self.houseType=houseType
    self.salePrice=salePrice
    self.areaInSqft=areaInSqft
    self.isFurnished=isFurnished
  

  def calculateNewPrice(self,newRate):
    self.salePrice= (self.areaInSqft*newRate)
    if self.isFurnished == "SEMI FURNISHED":
      return self.salePrice+(self.salePrice*0.1)
    elif self.isFurnished == "FULLY FURNISHED":
      return self.salePrice+(self.salePrice*0.2)

class Realtor:
  def __init__(self,realtorId,newRate,listOfHousesForSale):
    self.realtorId=realtorId
    self.newRate=newRate
    self.listOfHousesForSale=listOfHousesForSale


  def getAvailableHouses(self,inputsaleprice,inputhousetype):
    returnlist=[]
    for i in self.listOfHousesForSale:
      newsaleprice=i.calculateNewPrice(self.newRate)
      if newsaleprice <= inputsaleprice and i.houseType == inputhousetype:
        i.salePrice=newsaleprice
        returnlist.append(i)  
    return returnlist


t=int(input())
houseforsaleobjectlist=[]
for i in range(t):
    houseNumber=int(input())
    houseType=input()
    salePrice=float(input())
    areaInSqft=int(input())
    isFurnished=input()
    temp=HouseForSale(houseNumber,houseType,salePrice,areaInSqft,isFurnished)
    houseforsaleobjectlist.append(temp)

realtorId=12
newRate=float(input())  # rate per square feet

Realtorobj=Realtor(realtorId,newRate,houseforsaleobjectlist)

inputhousetype=input()
inputsaleprice=float(input())

#1st question
answer2=Realtorobj.getAvailableHouses(inputsaleprice,inputhousetype)

if not answer2:
  print("Preferred House Not Available")
else:
  for i in answer2:
    print(i.houseNumber,i.houseType,i.areaInSqft,i.salePrice)
