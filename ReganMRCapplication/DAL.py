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
    
  def addVessel(connection, name, cph):
    cursor = connection.cursor()
    try:
      cursor.execute("SELECT getVesselID(%s)", (name,))
      result = cursor.fetchone()

      if result and result[0] == -1:
        args = (name, cph)
        cursor.callproc("addVessel", args)
        connection.commit()
        return 'Vessel added successfully.'
      else:
        return 'Vessel already exists.'
    except:
      return 'Vessel was unable to be added.'
    finally:
      cursor.close()
  
class Trip_DAL:
  def addTrip(connection, vesselName, passengerName, dateAndTime, lengthOfTrip, totalPassengers):
    cursor = connection.cursor()
    try:
        # Get start and end time for the new trip
        start_time = dateAndTime
        cursor.execute("SELECT DATE_ADD(%s, INTERVAL %s HOUR)", (dateAndTime, lengthOfTrip))
        end_time = cursor.fetchone()[0]

        # Get passenger and vessel IDs
        cursor.execute("SELECT getPassengerID(%s)", (passengerName,))
        passenger_id = cursor.fetchone()[0]

        cursor.execute("SELECT getVesselID(%s)", (vesselName,))
        vessel_id = cursor.fetchone()[0]

        # Check for overlapping trips for the passenger
        cursor.execute("""
            SELECT COUNT(*) FROM Trips
            WHERE passengerID = %s
              AND (%s < DATE_ADD(dateAndTime, INTERVAL lengthOfTrip HOUR))
              AND (dateAndTime < %s)
        """, (passenger_id, start_time, end_time))
        passenger_overlap = cursor.fetchone()[0]

        # Check for overlapping trips for the vessel
        cursor.execute("""
            SELECT COUNT(*) FROM Trips
            WHERE vesselID = %s
              AND (%s < DATE_ADD(dateAndTime, INTERVAL lengthOfTrip HOUR))
              AND (dateAndTime < %s)
        """, (vessel_id, start_time, end_time))
        vessel_overlap = cursor.fetchone()[0]

        if passenger_overlap > 0 or vessel_overlap > 0:
            return "Unable to add trip. That passenger or vessel is already booked during this time."

        # Call stored procedure to add the trip
        args = (vesselName, passengerName, dateAndTime, lengthOfTrip, totalPassengers)
        cursor.callproc("addTrip", args)

        for result in cursor.stored_results():
            data = result.fetchall()
            if data:
                res = data[0][0]
                if res == -3:
                    return "Vessel and passenger not found. Add them then try again."
                if res == -2:
                    return "Passenger not found. Add them then try again."
                if res == -1:
                    return "Vessel not found. Add it then try again."

        connection.commit()
        return "Trip added successfully."

    except Exception as e:
        print(e)
        return "Unable to add trip. Check your inputs and try again."
    finally:
        cursor.close()



  # def addTrip(connection, vesselName, passengerName, dateAndTime, lengthOfTrip, totalPassengers):
  #   cursor = connection.cursor()
  #   try:
  #     # passDB = cursor.execute("""
  #     #   SELECT COUNT(*)
  #     #   FROM trips 
  #     #   WHERE passengerName = %s AND dateandtime = %s
  #     #   """, (passengerName, dateAndTime))
  #     # passDB = cursor.fetchone()[0]
  #     # print(passDB)

  #     # cursor.execute("""
  #     #   SELECT COUNT(*)
  #     #   FROM Trips 
  #     #   WHERE vesselName = %s AND dateandtime = %s
  #     #   """, (vesselName, dateAndTime))
  #     # vesselDB = cursor.fetchone()[0]

  #     # if (passDB + vesselDB) == 0:
  #     args = (vesselName, passengerName, dateAndTime, lengthOfTrip, totalPassengers)
  #     cursor.callproc("addTrip", args)

  #     for result in cursor.stored_results():
  #       data = result.fetchall()
  #       if data:
  #         res = data[0][0]
  #         if res == -3: return "Vessel and passenger not found. Add them then try again."
  #         if res == -2: return "Passenger not found. Add them then try again."
  #         if res == -1: return "Vessel not found. Add it then try again."

  #       connection.commit()
  #       return "Trip added successfully."
  #     # else:
  #       # return "Unable to add trip. You're double booking the passenger or vessel."
  #   except:
  #     return "Unable to add trip. Check your inputs and try again."
  #   finally:
  #     cursor.close()
  
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
      cursor.execute("SELECT getPassengerID(%s)", (passengerName,))
      result = cursor.fetchone()

      if result and result[0] == -1:
        args = (passengerName, address, phone)
        cursor.callproc("addPassenger", args)
        connection.commit()
        return 'Passenger added successfully.'
      else:
        return 'Passenger already exists.'
    except:
      return 'Passenger was unable to be added.'
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
      return False
    
  def allPassengers(connection):
    cursor = connection.cursor()
    query = "SELECT name FROM passengers;"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result