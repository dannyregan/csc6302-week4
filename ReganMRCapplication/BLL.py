import tabulate

from DAL import DBConnection, Vessel_DAL, Trip_DAL, Passenger_DAL

def connectToDB(username, pswd, host, port):
  db = DBConnection(username, pswd, host, port)
  connection = db.connect()
  if connection:
    return connection
  else:
    return False

def printAllTrips(connection):
  data = Trip_DAL.allTrips(connection)
  headers = ["Date and Time", "Length of Trip", "Vessel", "Passenger", "Address", "Phone", "Total Passengers", "Cost"]
  return tabulate.tabulate(data, headers=headers, tablefmt="fancy_grid")

def printTotalRevenueByVessel(connection):
  data = Vessel_DAL.totalRevenueByVessel(connection)
  headers = ["Vessel", "Total Revenue"]
  return tabulate.tabulate(data, headers=headers, tablefmt="fancy_grid")

def printAllPassengers(connection):
  data = Passenger_DAL.allPassengers(connection)
  headers = ["Name"]
  return tabulate.tabulate(data, headers=headers, tablefmt="fancy_grid")

def addPassenger(connection, name, address, phone):
  res = Passenger_DAL.addPassenger(connection, name, address, phone)
  return res

def addVessel(connection, name, cph):
  res = Vessel_DAL.addVessel(connection, name, cph)
  return res

def addTrip(connection, vesselName, passengerName, dateAndTime, lengthOfTrip, totalPassengers):
  res = Trip_DAL.addTrip(connection, vesselName, passengerName, dateAndTime, lengthOfTrip, totalPassengers)
  return res