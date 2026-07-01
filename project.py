student=[]

def add_student():
 
 n=int(input("Enter no of students:"))
 for i in range(0,n):
    roll_no=int(input("Enter student roll no:"))

    name=input("Enter student name:")

    m1=int(input("Enter marks of Physics: "))
    m2=int(input("Enter marks of Chemistry: "))
    m3=int(input("Enter marks of Biology: "))
    total=m1 + m2 + m3
    per=(total / 300)*100
    per=round(per,2)
    if per>=90:
       grade="A"
    elif per>=80 or per<=90:
      grade="B"
    elif per>=70 or per<=90:
         grade="C"
    elif per>=60 or per<=70:
         grade="D"
    else:
       print("Fale")
         

    data = {
       "Roll":roll_no,
       "Name":name,
       "Per":per,
       "Grade":grade,
       "Marks":{
          "Physics":m1,
          "Chemistry":m2,
          "Biology":m3
       }
    }
    student.append(data)


def update():
  
  rno=int(input("Enter roll no :"))
  for s in student:
   if s["Roll"] == rno:
      print("\n1. Update Roll_no")
      print("2. Update Name")
      print("3. Update Marks")
      print("4. Update All deatils")

      choice=int(input("Enter your choice:"))
      if(choice==1):
         s["Roll"] =input("Enter new rollno:")
      elif(choice==2):
         s["Name"] =input("Enter new name:")

      elif(choice==3):
         s["Marks"]["Physics"] =int(input("Enter new marks:"))
         s["Marks"]["Chemistry"] =int(input("Enter new marks:"))
         s["Marks"]["Biology"] =int(input("Enter new marks:"))
      elif(choice==4):
         s["Name"] =input("Enter new name:")
         s["Roll"] =int(input("Enter new roll no:"))
         s["Marks"]["Physics"] =int(input("Enter new marks:"))
         s["Marks"]["Chemistry"] =int(input("Enter new marks:"))
         s["Marks"]["Biology"] =int(input("Enter new marks:"))
      else:
         print("Invalid choice")
         return
 
   total= s["Marks"]["Physics"] + s["Marks"]["Chemistry"] + s["Marks"]["Biology"]
   per=(total / 300)*100
   per=round(per,2)
   if per>=90:
       grade="A"
   elif per>=80 or per<=90:
      grade="B"
   elif per>=70 or per<=90:
         grade="C"
   elif per>=60 or per<=70:
         grade="D"
  else:
       print("Fale")

def delete():
   #rno=int(input("Enter roll_no to delete:"))
   #for s in student:
    #if s["Roll"] == rno:
   print("\n1. Delete by rollno")
   print("2. Delete by name")
   print("3. Delete all details")
   choice=int(input("Enter choice to delete="))

   if choice==1:
         rno=int(input("Enter roll no:"))
         for s in student:
            if s["Roll"]==rno:
              student.remove(s)


   elif choice==2:
         name=input("Enter name:")
         for s in student:
            if s["Name"]==name:
              student.remove(s)
         
   elif choice==3:
         student.remove(s)

         print("Studet all details deleted successfully!!")
   else:
         print("Invalid choice")
   return

def search():
      print("\n1. Search by rollno")
      print("2. Search by name")
      print("3. Search by grade")

      choice=int(input("Enter choice to search="))

      if choice==1:
       rno=int(input("Enter roll no to search:"))
       print("Rollno\tName\tPhysics\t\tChemistry\tBiology\t\tPercentage\tGrade\n")

       for s in student:
            if s["Roll"]==rno:  
             print(f"{s['Roll']}\t{s['Name']}\t{s['Marks']['Physics']}\t\t{s['Marks']['Chemistry']}\t\t{s['Marks']['Biology']}\t\t{s['Per']}\t\t{s['Grade']}")

      if choice==2:
       name=input("Enter name to search:")
       print("Rollno\tName\tPhysics\t\tChemistry\tBiology\t\tPercentage\tGrade\n")

       for s in student:
            if s["Name"]==name:
             
             print(f"{s['Roll']}\t{s['Name']}\t{s['Marks']['Physics']}\t\t{s['Marks']['Chemistry']}\t\t{s['Marks']['Biology']}\t\t{s['Per']}\t\t{s['Grade']}")


      if choice==3:
       grade=input("Enter grade to search:")
       print("Rollno\tName\tPhysics\t\tChemistry\tBiology\t\tPercentage\tGrade\n")

       for s in student:
            if s["Grade"]==grade:
             print(f"{s['Roll']}\t{s['Name']}\t{s['Marks']['Physics']}\t\t{s['Marks']['Chemistry']}\t\t{s['Marks']['Biology']}\t\t{s['Per']}\t\t{s['Grade']}")

def sorting():
   print("\n1. Sort by roll no")
   print("2. Sort by name")
   print("3. Sort by percentage")

   choice=int(input("Enter your choice:"))

   if choice==1:
      for i in range(len(student)):
         for j in range(i+1,len(student)):
            if student[i]["Roll"] > student[j]["Roll"]:
               student[i], student[j] = student[j], student[i]

   elif choice==2:
      for i in range(len(student)):
         for j in range(i+1,len(student)):
            if student[i]["Name"] > student[j]["Name"]:
               student[i], student[j] = student[j], student[i]

   elif choice==3:
      for i in range(len(student)):
         for j in range(i+1,len(student)):
            if student[i]["Per"] > student[j]["Per"]:
               student[i], student[j] = student[j], student[i]
   else:
         print("Invalid choice")
         return
         print("Data sorted successfully")
   output()



def output():
   if(len(student)==0):
      print("Data not found")
   else:
      print("Rollno\tName\tPhysics\t\tChemistry\tBiology\t\tPercentage\tGrade")
   
      for s in student:
        print(f"{s['Roll']}\t{s['Name']}\t{s['Marks']['Physics']}\t\t{s['Marks']['Chemistry']}\t\t{s['Marks']['Biology']}\t\t{s['Per']}\t\t{s['Grade']}")
   

while True:
   print("---------------------------------------------Students details---------------------------------------------")
   print("\n1. Add")
   print("2. Update")
   print("3. Output")
   print("4. Delete")
   print("5. Search")
   print("6. Sorting")
   print("7. Exit")

   choice=int(input("Enter your choice:"))
   if choice==1:
      add_student()
   elif choice==2:
      update()
   elif choice==3:
      output()
   elif choice==4:
      delete()
   elif choice==5:
      search()
   elif choice==6:
      sorting()
   elif choice==7:
      print("Thank you!!")
      break
   else:
      print("Invalid choice")









   

       
