from tkinter import *

from BLL import connectToDB

root = Tk()
root.title('Merrimack River Cruise')
root.geometry('350x300')

# FIX COMMIT WHEN TRIPS ADDED OR SOMETHING
# once logged in the options are:
# View all trips
# View Revenue By Vessel
# View All Stored Passengers
# Add Passenger
# Add Vessel
# Add Trip
# No double booking (in BLL)
# If user/vessel doesn't exist for new trip, just add user and vessel

# Configure grid so rows/columns expand
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Inputs
user = Entry(root, width=20)
user.grid(row=0, column=1, padx=20)
user.insert(0, 'root')
pswd = Entry(root, width=20)
pswd.grid(row=1, column=1, padx=20)
pswd.insert(0, 'Legends17!')
host = Entry(root, width=20)
host.grid(row=2, column=1, padx=20)
host.insert(0, '127.0.0.1')
port = Entry(root, width=20)
port.grid(row=3, column=1, padx=20)
port.insert(0, '3306')

# Input Labels
userLabel = Label(root, text='Username')
userLabel.grid(row=0, column=0)
pswdLabel = Label(root, text='Password')
pswdLabel.grid(row=1, column=0)
hostLabel = Label(root, text='Hostname')
hostLabel.grid(row=2, column=0)
portLabel = Label(root, text='Port')
portLabel.grid(row=3, column=0)

# Submit Button
def submit():
    # Get the values from the entry widgets
    username = user.get()
    password = pswd.get()
    host_value = host.get()
    port_value = port.get()
    
    # Call connectToDB function and pass the user inputs
    if connectToDB(username, password, host_value, port_value):
        # Hide the sign-in form
        user.grid_forget()
        pswd.grid_forget()
        host.grid_forget()
        port.grid_forget()
        userLabel.grid_forget()
        pswdLabel.grid_forget()
        hostLabel.grid_forget()
        portLabel.grid_forget()
        submitButton.grid_forget()
    
        viewTripsButton = Button(root, text="View All Trips")
        viewTripsButton.grid(row=0, column=0, padx=10, pady=10)
        
        viewRevenueButton = Button(root, text="View Revenue By Vessel")
        viewRevenueButton.grid(row=0, column=1, padx=10, pady=10)
        
        viewAllPassengers = Button(root, text="View All Passengers")
        viewAllPassengers.grid(row=1, column=0, padx=10, pady=10)
        
        addPassengerButton = Button(root, text="Add Passenger")
        addPassengerButton.grid(row=1, column=1, padx=10, pady=10)
        
        addVesselButton = Button(root, text="Add Vessel")
        addVesselButton.grid(row=2, column=0, padx=10, pady=10)

        addTripButton = Button(root, text="Add Trip")
        addTripButton.grid(row=2, column=1, padx=10, pady=10)

submitButton = Button(root, text = 'Submit', command = submit)
submitButton.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

root.mainloop()