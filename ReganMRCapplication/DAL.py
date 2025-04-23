import mysql.connector

class DBConnection:
  def __init__(self, password):
    self.password = password
    self.config = {
      'user': 'root',
      'password': self.password,
      'database': 'mrc'
    }

  def connect(self):
    try:
      mydb = mysql.connector.connect(**self.config)
      return mydb, 'Connection successful.'
    except:
      return None, "Connection failed."

