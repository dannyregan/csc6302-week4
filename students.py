from DAL.studentDAL import StudentDAL


class Student:
    def __init__(self, id, first_name, last_name, email, date_of_birth):
        self.studentDal = StudentDAL()
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.date_of_birth = date_of_birth

    def add(self):
     
        query = self.studentDal.add(self.first_name, self.last_name, self.email, self.date_of_birth)

        return query()

   



