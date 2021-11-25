#People in the class
    
class Student:

    def __init__(self, fname, lname, age, score):
        self.fname = fname 
        self.lname = lname
        self.age = age 
        self.score = score



paul = Student("Paul", "Ukaegbu", 32, 93)
dema = Student("Dema", "Um", 23, 89)
ray = Student("Ray", "Smith", 27, 77)
buddy = Student("Buddy", "Love", 21, 68) 

user = input("Who grades are you looking for?\nPaul, Dema, Ray, or Buddy?\n")

if user == "Paul":
    print(paul.score)
elif user == "Dema":
    print(dema.score)   
elif user == "Ray":
    print(ray.score) 
elif user == "Buddy":
    print(buddy.score)
else:
    print("Student doesn't exist")

