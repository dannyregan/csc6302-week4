import getpass

from DAL import DBConnection, Vessel_DAL

def printChart(data):
  print("--------------------------------")
  spaces = 13
  for row in data:
    print(row[0], " "*(spaces - len(row[0])), "| ", row[1])
  print("--------------------------------")

def main():
  pswd = getpass.getpass("Enter the database's password: ")

  print("Connecting to database...")
  db = DBConnection(pswd)
  connection, res = db.connect()

  if connection:
    print(res)
    input("Press enter to view the Total Revenue by Vessel: ")
    view = Vessel_DAL.totalRevenueByVessel(connection)
    printChart(view)
  else: print(res)


  
# ===========================================
if __name__ == '__main__':
  main()