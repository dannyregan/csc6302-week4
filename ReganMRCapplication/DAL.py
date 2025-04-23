import mysql.connector

class DBConnection:
  def __init__(self, password):
    self.password = password
    self.config = {
      'user': 'root',
      'password': self.password,
      'database': 'mrc'
    }
    self.connection = None

  def connect(self):
    try:
      self.connection = mysql.connector.connect(**self.config)
      return self.connection, 'Connection successful.'
    except:
      return self.connection, "Connection failed."
  
  def cursor(self):
    if self.connection:
      return self.connection.cursor()
    else:
      return "Not connected to a database."
  
  def close(self):
    if self.connection:
      self.connection.close()
      self.connection = None

class Vessel_DAL:

  def totalRevenueByVessel(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM TotalRevenuebyVessel;"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result
  
  def getVesselID(connection, vesselName):
    cursor = connection.cursor()
    func = f"getVesselID({vesselName});"
    cursor.execute(func)
    result = cursor.fetchall()
    cursor.close()
    return result