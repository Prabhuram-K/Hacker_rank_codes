# Enter your code here. Read input from STDIN. Print output to STDOUT
class Table:
  #-------------------------------------------------#
  def __init__(self,tableNo,waiterName,status):
    self.tableNo=tableNo
    self.waiterName=waiterName
    self.status=status
  #-------------------------------------------------#
    

class Hotel:
#-------------------------------------------------#
  def __init__(self,hotelName,tableList):
    self.hotelName=hotelName
    self.tableList=tableList

#--------------------TEMPLATE ENDS----------------------#

  def findStatusWiseTotalNoOfTable(self):
    statusdict={}
    for i in self.tableList:
      if i.status in statusdict.keys():
        statusdict[i.status]+=1

      else:
        statusdict[i.status]=1
      
    return statusdict


  def findWaiterNameByTableNo(self,table_info_ref_no):
    for i in self.tableList:
      if i.tableNo == table_info_ref_no:
        return i
    return None


#----------------------MAIN----------------------#
t=int(input())
tableobjlist=[]
for i in range(t):
    tableNo=int(input())
    waiterName=input()
    status=input()
    temp=Table(tableNo,waiterName,status)
    tableobjlist.append(temp)

hotelname= "Taj Vivanta" #given in question that any name can be hard coded for the name of the hotel
hotelobject=Hotel(hotelname,tableobjlist)

#---------------------TEMPLATE ENDS--------------------#
table_info_ref_no=int(input())

#1st question :

answer1=hotelobject.findStatusWiseTotalNoOfTable()
for i in sorted(answer1):
  print(str(i)+"-"+str(answer1[i]))


#2nd question :

answer2=hotelobject.findWaiterNameByTableNo(table_info_ref_no)
if (answer2 != None):
  print(answer2.waiterName)

else:
  print('No Table Found')
