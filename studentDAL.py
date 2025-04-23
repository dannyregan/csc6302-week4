import mysql.connector

from mysql.connector import errorcode

class StudentDAL:
    def __init__(self):
        self.admin_cnx = mysql.connector.connect(user='user_name', password='password',
                              host='127.0.0.1',
                              database='database_name')
    
    def add(self, fname, lname, email, dob):
        cursor = self.admin_cnx.cursor(dictionary=True)
        args = (fname,lname,email, dob)
        
        cursor.callproc('addStudent', args)
        self.admin_cnx.commit()
        list = []
      
        for result in cursor.stored_results():
           for item in result.fetchall():
               list.append((item['first_name'], item['last_name']))
        cursor.close()
        return list

