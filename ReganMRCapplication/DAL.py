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
    query = f"SELECT getVesselID('{vesselName}');"
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    if result and result[0] != -1:
      return result[0]
    else: 
      return "Vessel not found."
  
class Trip_DAL:
  def addTrip(connection, vesselName, passengerName, dateAndTime, lengthOfTrip, totalPassengers):
    cursor = connection.cursor()
    try:
      args = (vesselName, passengerName, dateAndTime, lengthOfTrip, totalPassengers)
      cursor.callproc("addTrip", args)

      for result in cursor.stored_results():
        data = result.fetchall()
        if data:
          res = data[0][0]
          if res == -3: return "Vessel and passenger not found."
          if res == -2: return "Passenger not found."
          if res == -1: return "Vessel not found."

      connection.commit()
      return "Trip added successfully."
    
    finally:
      cursor.close()
  
  def allTrips(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM AllTrips;"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result
  
class Passenger_DAL:
  def addPassenger(connection, passengerName, address, phone):
    cursor = connection.cursor()
    try:
      args = (passengerName, address, phone)
      cursor.callproc("addPassenger", args)
      connection.commit()
      return "Passenger is now in the database."
    
    finally:
      cursor.close()
  
  def getPassengerID(connection, passengerName):
    cursor = connection.cursor()
    query = f"SELECT getPassengerID('{passengerName}');"
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    if result and result[0] != -1:
      return result[0]
    else: 
      return "Passenger not found."