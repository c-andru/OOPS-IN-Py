#OOPS-Class and Objects ,constructor
#1. Student Registration-Here init doesn't offers a customization for grade so use init when the attributes initializes at the object creation else it won't be flexible 
class student:
    scl_name="Ab High School"
    def __init__(self,name,rollno,grade="A"):
        self.name=name
        self.rollno=rollno
stud=student("Alice",20,"B")
print("student 1\n",stud.name,"\n",stud.rollno)
#2.Bank Account System -Here can create only one init per class and another method is defined here iused dict to assign a multiple values under same objects
class bank:
    bnk="axis Bank"
    def __init__(self):
        self.data={}
bnkobj=bank()
bnkobj.data["chennai","1000"]=1
bnkobj.data["Mumbai","1001"]=2
print(bnkobj.data)
#3. Library data
class lib:
    lib_N="Anna"
    def __init__(self):
        self.book={}
bookdata=lib()
bookdata.book['bookstatus']={'Booktitle':"George"}
print(bookdata.book)

