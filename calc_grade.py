student = {
    "name": None,
    "score": None
    }
def add_name():
    return input("please enter your name:")

def add_score():
    return int(input("please enter your score:"))

def calculate_grade(student):
   if student['score'] >= 80 and student['score'] <=100 :
        student['grade'] = "A"
        return student['grade']


   elif student['score'] >= 70 and student['score'] <80 :
        student['grade'] = "B"
        return student['grade']


   elif student['score'] >= 60 and student['score'] <70 :
        student['grade'] = "C"
        return student['grade']


   elif student['score'] >= 50  :
        student['grade'] = "D"
        return student['grade']


   else :
        student['grade'] = "F"
        return student['grade']
      
student["name"] = add_name()
student["score"] = add_score()
student["grade"] = calculate_grade(student)

print (student)
