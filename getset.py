class Student:
    def __init__(self, student_name, student_id, grades, password):
        self.student_name = student_name
        self.student_id = student_id
        self.__grades = grades
        self.__password = password

    def public_info(self):
        return (self, self.student_id)
    
    def private_info(self, password):
        if self.__password == password:
            return (self.__grades, self.__password)
        else:
            return ("Password Error")
    
    def id(self):
        id = (842518)


    def grades(self):
        grades = {'Math':'D', 'English':'B', 'Art':'C', 'Music':'B', 'Hospitality':'Satisfactory'}
    

