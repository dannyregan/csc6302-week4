import getpass
import tabulate

from DAL import DBConnection, Vessel_DAL, Trip_DAL, Passenger_DAL

def printTotalRevenueByVessel(connection):
  data = Vessel_DAL.totalRevenueByVessel(connection)
  headers = ["Vessel", "Total Revenue"]
  return tabulate.tabulate(data, headers=headers, tablefmt="fancy_grid")

def printAllTrips(connection):
  data = Trip_DAL.allTrips(connection)
  headers = ["Date and Time", "Length of Trip", "Vessel", "Passenger", "Address", "Phone", "Total Passengers", "Cost"]
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

def connectToDB(username, pswd, host_value, port_value):
  db = DBConnection(pswd)
  connection, res = db.connect()
  if connection:
    print(res)
    return connection
  else:
    print("No connection")
    return False

def main():
  # Password required to access the database
  # pswd = getpass.getpass("Enter the password for the database 'mrc': ")

  # print("Connecting to database...")
  # db = DBConnection(pswd)
  # connection, res = db.connect()

  if connection:
    print(res) # Connection successful

    # Total revenue by vessel table display
    input("Press enter to view the TOTAL REVENUE BY VESSEL: ")
    view = Vessel_DAL.totalRevenueByVessel(connection)
    printTotalRevenueByVessel(view)

    # Get vessel ID given a vessel name
    input("Press enter to view the vessel ID for SEA BREEZE: ")
    vesselId = Vessel_DAL.getVesselID(connection, "Sea Breeze")
    print(f'Vessel ID: {vesselId}')

    input("Press enter to view the vessel ID for DOES NOT EXIST: ")
    vesselId = Vessel_DAL.getVesselID(connection, "Does Not Exist")
    print(f'Vessel ID: {vesselId}')

    # Add a trip
    input("Press enter to add a new trip for an EXISTING passenger and vessel: ")
    trip = Trip_DAL.addTrip(connection, "Sea Breeze", "Emily Clark", "2025-04-24 10:00:00", 1, 8)
    print(trip)

    input("Press enter to add a new trip for a NON-EXISTING passenger and vessel: ")
    trip = Trip_DAL.addTrip(connection, "New Boat", "New Passenger", "2025-04-24 10:00:00", 1, 8)
    print(trip)

    # View all trips
    input("Press enter to view ALL TRIPS: ")
    view = Trip_DAL.allTrips(connection)
    printAllTrips(view)

    # View passenger ID given passenger name
    input("Press enter to view the passenger ID for EMILY CLARK: ")
    passengerId = Passenger_DAL.getPassengerID(connection, "Emily Clark")
    print(f'Passenger ID: {passengerId}')

    input("Press enter to view the passenger ID for DANNY REGAN: ")
    passengerId = Passenger_DAL.getPassengerID(connection, "Danny Regan")
    print(f'Passenger ID: {passengerId}')

    # Add new passenger
    input("Press enter to add a NEW PASSENGER.")
    passenger = Passenger_DAL.addPassenger(connection, "Abe Lincoln", "1 Main St., Boston, MA 01234", "617-555-5555")
    print(passenger)

  else: print(res) # Connection failed

# ===========================================
if __name__ == '__main__':
  main()