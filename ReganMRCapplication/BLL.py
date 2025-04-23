import getpass

from DAL import DBConnection

def main():
  pswd = getpass.getpass("Enter the database's password: ")

  print("Connecting to database...")
  config = DBConnection(pswd)
  connection, res = config.connect()
  print(res) if connection else print(res)

  
# =========================================
if __name__ == '__main__':
  main()