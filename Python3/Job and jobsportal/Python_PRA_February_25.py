class Job:
  def __init__(self,job_id,company,job_role,start_salary,high_salary):
    self.job_id=job_id
    self.company=company
    self.job_role=job_role
    self.start_salary=start_salary
    self.high_salary=high_salary

class jobsportal:
  def __init__(self,portal_name,job_list):
    self.portal_name=portal_name
    self.job_list=job_list
  
  def get_bestjobbyrole(self,jobroleinput):
    returnvalue=[]
    a=[]
    temp=[]
    for i in self.job_list:
      if str.lower(i.job_role) == str.lower(jobroleinput):
        temp.append(i)
        a.append(i.high_salary)
    for i in temp:
      if i.high_salary == max(a):
          returnvalue.append(i)
    return returnvalue


  def jobswithsalary(self,salaryinput):
    dict={}
    for i in self.job_list:
      if i.start_salary < salaryinput and i.high_salary > salaryinput:
        dict[i.job_id]=i.company
    return dict


#--------input----------#
t=int(input())
jobobjectlist=[]
for i in range(t):
    job_id=int(input())
    company=input()
    job_role=input()
    start_salary=int(input())
    high_salary=int(input())
    temp=Job(job_id,company,job_role,start_salary,high_salary)
    jobobjectlist.append(temp)

portalnameinput="TCS ION"
jobsportalobject=jobsportal(portalnameinput,jobobjectlist)

jobroleinput=input()
salaryinput=int(input())
#--------input ends-------#

#1st question
answer1=jobsportalobject.get_bestjobbyrole(jobroleinput)

if not answer1:
  print ("No Job Found for the given role")
else:
  for i in answer1:
    print (i.job_id,i.company,i.start_salary)


#2 question
answer2=jobsportalobject.jobswithsalary(salaryinput)
if not answer2:
  print("No matching jobs")
else:
  for i in answer2:
    print (i,answer2[i])
