# References:
# https://tkdocs.com/tutorial/
# https://docs.python.org/3/library/tkinter.html#text-widget
# https://www.tutorialspoint.com/python/tk_text.htm
# https://www.youtube.com/watch?v=AK1J8xF4fuk
# https://www.drupal.org/forum/support/module-development-and-code-questions/2007-03-16/d-and-s-in-sql-queries

from tkinter import *

from BLL import connectToDB, printAllTrips, printTotalRevenueByVessel, printAllPassengers, addPassenger, addVessel, addTrip

# GUI set up
root = Tk()
root.title('Merrimack River Cruise')

# Track if output box has info in it
currentOutput = {"box": None}

# Rows/columns expand within the GUI
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_rowconfigure(6, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_columnconfigure(4, weight=1)
root.grid_columnconfigure(5, weight=1)

def showMainMenu(root, connection):
    root.geometry("1200x50")
    # Clear the GUI
    for widget in root.grid_slaves():
        widget.grid_forget()
    # Add buttons
    viewTripsButton = Button(root, text="View All Trips", command=lambda: viewAllTrips(root, connection))
    viewTripsButton.grid(row=0, column=0, padx=10, pady=10)

    viewRevenueButton = Button(root, text="View Revenue By Vessel", command=lambda: viewRevenueByVessel(root, connection))
    viewRevenueButton.grid(row=0, column=1, padx=10, pady=10)

    viewAllPassengersButton = Button(root, text="View All Passengers", command=lambda: viewPassengers(root, connection))
    viewAllPassengersButton.grid(row=0, column=2, padx=10, pady=10)

    addPassengerButton = Button(root, text="Add Passenger", command=lambda: addNewPassenger(root, connection))
    addPassengerButton.grid(row=0, column=3, padx=10, pady=10)

    addVesselButton = Button(root, text="Add Vessel", command=lambda: addNewVessel(root, connection))
    addVesselButton.grid(row=0, column=4, padx=10, pady=10)

    addTripButton = Button(root, text="Add Trip", command=lambda: addNewTrip(root, connection))
    addTripButton.grid(row=0, column=5, padx=10, pady=10)

def showRes(root, connection, res):
    root.geometry('700x150')
    # Clear the GUI
    for widget in root.grid_slaves():
        widget.grid_forget()
    outputBox = displayOutputBox(root, 90, 1)
    outputBox.insert(END, res)
    okay = Button(root, text='Okay', command=lambda: showMainMenu(root, connection))
    okay.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

def displayOutputBox(root, w, h):
    if currentOutput["box"]:
        currentOutput["box"].destroy()
        currentOutput["box"] = None 
    outputBox = Text(root, width=w, height=h)
    outputBox.grid(row=1, column=0, columnspan=6, padx=20, pady=20)
    currentOutput["box"] = outputBox 
    return outputBox

def viewAllTrips(root, connection):
    root.geometry('1200x700')
    outputBox = displayOutputBox(root, 195, 45)
    outputText = printAllTrips(connection)
    outputBox.insert(END, outputText)

def viewRevenueByVessel(root, connection):
    root.geometry('900x300')
    outputBox = displayOutputBox(root, 45, 10)
    outputText = printTotalRevenueByVessel(connection)
    outputBox.insert(END, outputText)

def viewPassengers(root, connection):
    root.geometry('900x300')
    outputBox = displayOutputBox(root, 20, 15)
    outputText = printAllPassengers(connection)
    outputBox.insert(END, outputText)

def submitPassenger(root, connection, name, address, phone):
    res = addPassenger(connection, name, address, phone)
    outputBox = displayOutputBox(root, 35, 1)
    outputBox.delete("1.0", END)
    outputBox.insert(END, res)
    showRes(root, connection, res)

def submitVessel(root, connection, name, cph):
    res = addVessel(connection, name, cph)
    outputBox = displayOutputBox(root, 35, 1)
    outputBox.delete("1.0", END)
    outputBox.insert(END, res)
    showRes(root, connection, res)

def submitTrip(root, connection, vesselName, passengerName, dateAndTime, lengthOfTrip, totalPassengers):
    res = addTrip(connection, vesselName, passengerName, dateAndTime, lengthOfTrip, totalPassengers)
    outputBox = displayOutputBox(root, 45, 1)
    outputBox.insert(END, res)
    showRes(root, connection, res)
    
def addNewPassenger(root, connection):
    root.geometry('350x250')
    for widget in root.grid_slaves():
        widget.grid_forget()
    # Labels
    title = Label(root, text='Add New Passenger')
    title.grid(row=0, columnspan=2)
    nameLabel = Label(root, text='Name')
    nameLabel.grid(row=1, column=0)
    addressLabel = Label(root, text='Address')
    addressLabel.grid(row=2, column=0)
    phoneLabel = Label(root, text='Phone')
    phoneLabel.grid(row=3, column=0)
    # Inputs
    name = Entry(root, width=20)
    name.grid(row=1, column=1, padx=20)
    address = Entry(root, width=20)
    address.grid(row=2, column=1, padx=20)
    phone = Entry(root, width=20)
    phone.grid(row=3, column=1, padx=20)

    submitPassengerButton = Button(root, text='Submit', command=lambda: submitPassenger(root, connection, name.get(), address.get(), phone.get()))
    submitPassengerButton.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
    
def addNewVessel(root, connection):
    root.geometry('350x250')
    for widget in root.grid_slaves():
        widget.grid_forget()
    # Labels
    title = Label(root, text='Add New Vessel')
    title.grid(row=0, columnspan=2, padx=5)
    nameLabel = Label(root, text='Vessel Name')
    nameLabel.grid(row=1, column=0, padx=5)
    cphLabel = Label(root, text='Cost Per Hour')
    cphLabel.grid(row=2, column=0, padx=5)
    # Inputs
    name = Entry(root, width=20)
    name.grid(row=1, column=1)
    cph = Entry(root, width=20)
    cph.grid(row=2, column=1)
    # Submit button
    submitVesselButton = Button(root, text='Submit', command=lambda: submitVessel(root, connection, name.get(), cph.get()))
    submitVesselButton.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

def addNewTrip(root, connection):
    root.geometry('350x300')
    for widget in root.grid_slaves():
        widget.grid_forget()
    # Labels
    title = Label(root, text='Add New Trip')
    title.grid(row=0, columnspan=2)
    vesselLabel = Label(root, text='Vessel Name')
    vesselLabel.grid(row=1, column=0, padx=5)
    passengerLabel = Label(root, text='Passenger Name')
    passengerLabel.grid(row=2, column=0, padx=5)
    dtLabel = Label(root, text='Date and Time')
    dtLabel.grid(row=3, column=0, padx=5)
    lengthLabel = Label(root, text='Length of Trip')
    lengthLabel.grid(row=4, column=0, padx=5)
    nPassengersLabel = Label(root, text='Total Passengers')
    nPassengersLabel.grid(row=5, column=0, padx=5)
    # Inputs
    vessel = Entry(root, width=20)
    vessel.grid(row=1, column=1)
    passenger = Entry(root, width=20)
    passenger.grid(row=2, column=1)
    dt = Entry(root, width=20)
    dt.grid(row=3, column=1)
    length = Entry(root, width=20)
    length.grid(row=4, column=1)
    nPassengers = Entry(root, width=20)
    nPassengers.grid(row=5, column=1)
    # Submit button
    submitTripButton = Button(root, text='Submit', command=lambda: submitTrip(root, connection, vessel.get(), passenger.get(), dt.get(), length.get(), nPassengers.get()))
    submitTripButton.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

def submitSignIn(user, pswd, host, port):
    global connection
    connection = connectToDB(user, pswd, host, port)
    
    if connection:
        showMainMenu(root, connection)
    else:
        root.geometry('500x100')
        # Clear the GUI
        for widget in root.grid_slaves():
            widget.grid_forget()
        outputBox = displayOutputBox(root, 90, 1)
        outputBox.insert(END, 'Unable to sign in. Try again.')

        okay = Button(root, text='Okay', command=lambda: signIn())
        okay.grid(row=2, column=0, columnspan=2, padx=10, ipadx=100)

def signIn():
    root.geometry('350x200')
    for widget in root.grid_slaves():
        widget.grid_forget()
    # Sign in labels
    title = Label(root, text='Sign In')
    title.grid(row=0, columnspan=2)
    userLabel = Label(root, text='Username')
    userLabel.grid(row=1, column=0, padx=5)
    pswdLabel = Label(root, text='Password')
    pswdLabel.grid(row=2, column=0, padx=5)
    hostLabel = Label(root, text='Hostname')
    hostLabel.grid(row=3, column=0, padx=5)
    portLabel = Label(root, text='Port')
    portLabel.grid(row=4, column=0, padx=5)
    # Sign in inputs
    user = Entry(root, width=20)
    user.grid(row=1, column=1)
    user.insert(0, 'root')
    pswd = Entry(root, width=20)
    pswd.grid(row=2, column=1)
    pswd.insert(0, '')
    host = Entry(root, width=20)
    host.grid(row=3, column=1)
    host.insert(0, '127.0.0.1')
    port = Entry(root, width=20)
    port.grid(row=4, column=1)
    port.insert(0, '3306')

    submitButton = Button(root, text='Sign In', command=lambda: submitSignIn(user.get(), pswd.get(), host.get(), port.get()))
    submitButton.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

signIn()
root.mainloop()