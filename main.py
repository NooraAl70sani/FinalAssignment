# Importing the libraries
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pickle

# Class representing an Employee
class Employee:
    def __init__(self, name, employeeId, department, jobTitle, basicSalary, managerId):
        # Initialize a Employee object with its attributes
        self.name = name
        self.employeeId = employeeId
        self.department = department
        self.jobTitle = jobTitle
        self.basicSalary = basicSalary
        self.managerId = managerId
        self.managedEmployees = []  # One-to-many relationship with Employee (manager managing employees)
        self.eventsManaged = []  # One-to-many relationship with Event (manager managing events)

    # Add an employee to the list of employees
    def addManagedEmployee(self, employee):
        self.managedEmployees.append(employee)

    # Add an event
    def addEventManaged(self, event):
        self.eventsManaged.append(event)

    def __str__(self):
        # To display a string
        return f"{self.name} - {self.employeeId} - {self.department} - {self.jobTitle} - {self.basicSalary} - {self.managerId}"

# Class representing an Client
class Client:
    def __init__(self, clientId, name, address, contactDetails, budget):
        # Initialize a Client object with its attributes
        self.clientId = clientId
        self.name = name
        self.address = address
        self.contactDetails = contactDetails
        self.budget = budget
        self.events = []  # One-to-many relationship with Event

    # Add an event associated with this client
    def addEvent(self, event):
        self.events.append(event)

    def __str__(self):
        # To display a string
        return f"{self.clientId} - {self.name} - {self.address} - {self.contactDetails} - {self.budget}"

# Class representing an Event
class Event:
    def __init__(self, eventId, eventType, theme, date, time, duration, venue, client, guestList,
                 cateringCompany, cleaningCompany, decorationsCompany, entertainmentCompany, furnitureSupplyCompany,
                 invoice):
        # Initialize a Event object with its attributes
        self.eventId = eventId
        self.eventType = eventType
        self.theme = theme
        self.date = date
        self.time = time
        self.duration = duration
        self.venue = venue  # One-to-one relationship with Venue
        self.client = client  # One-to-many relationship with Client
        self.guestList = guestList
        self.cateringCompany = cateringCompany  # One-to-one relationship with Caterer
        self.cleaningCompany = cleaningCompany
        self.decorationsCompany = decorationsCompany
        self.entertainmentCompany = entertainmentCompany
        self.furnitureSupplyCompany = furnitureSupplyCompany
        self.invoice = invoice

    def __str__(self):
        # To display a string
        return f"{self.eventId} - {self.eventType} - {self.theme} - {self.date} - {self.time} - {self.duration} - {self.venue} - {self.client} - {self.guestList} - {self.cateringCompany} - {self.cleaningCompany} - {self.decorationsCompany} - {self.entertainmentCompany} - {self.furnitureSupplyCompany} - {self.invoice}"

# Class representing an Venue
class Venue:
    def __init__(self, venueId, name, address, contact, minimumGuests, maximumGuests):
        # Initialize a Venue object with its attributes
        self.venueId = venueId
        self.name = name
        self.address = address
        self.contact = contact
        self.minimumGuests = minimumGuests
        self.maximumGuests = maximumGuests
        self.events = []  # One-to-many relationship with Event

    def addEvent(self, event):
        # Add an event associated with this venue
        self.events.append(event)

    def __str__(self):
        # To display a string
        return f"{self.venueId} - {self.name} - {self.address} - {self.contact} - {self.minimumGuests} - {self.maximumGuests}"

# Class representing an Caterer
class Caterer:
    def __init__(self, catererId, name, address, contactDetails, menu= None, minimumGuests= None, maximumGuests= None):
        # Initialize a Caterer object with its attributes
        self.catererId = catererId
        self.name = name
        self.address = address
        self.contactDetails = contactDetails
        self.menu = menu
        self.minimumGuests = minimumGuests
        self.maximumGuests = maximumGuests
        self.event = None  # One-to-one relationship with Event

    def assignEvent(self, event):
        self.event = event

    def __str__(self):
        # To display a string
        return f"{self.catererId} - {self.name} - {self.address} - {self.contactDetails} - {self.menu} - {self.minimumGuests} - {self.maximumGuests}"

# Class representing an Guest
class Guest:
    def __init__(self, guestId, name, address, contactDetails):
        # Initialize a Guest object with its attributes
        self.guestId = guestId
        self.name = name
        self.address = address
        self.contactDetails = contactDetails
        self.events = []  # Many-to-many relationship with Event

    def addEvent(self, event):
        # Add an event associated with this guest
        self.events.append(event)

    def __str__(self):
        # To display a string
        return f"{self.guestId} - {self.name} - {self.address} - {self.contactDetails}"

# Class representing an Supplier
class Supplier:
    def __init__(self, supplierId, name, address, contactDetails):
        # Initialize a Supplier object with its attributes
        self.supplierId = supplierId
        self.name = name
        self.address = address
        self.contactDetails = contactDetails
        self.events = []  # Many-to-many relationship with Event

    def addEvent(self, event):
        # Add an event associated with this supplier
        self.events.append(event)

    def __str__(self):
        # To display a string
        return f"{self.supplierId} - {self.name} - {self.address} - {self.contactDetails}"

# Class representing the Event Management System
class EventManagementSystem:
    def __init__(self):
        # Initialize an EventManagementSystem object with empty lists for storing data
        self.employees = []
        self.events = []
        self.clients = []
        self.guests = []
        self.venues = []
        self.caterers = []
        self.suppliers = []
    #  Load data from pickle files into respective lists.
    def loadData(self):
        try:
            with open('employees.pickle', 'rb') as f:
                self.employees = pickle.load(f)
            with open('events.pickle', 'rb') as f:
                self.events = pickle.load(f)
            with open('clients.pickle', 'rb') as f:
                self.clients = pickle.load(f)
            with open('guests.pickle', 'rb') as f:
                self.guests = pickle.load(f)
            with open('venues.pickle', 'rb') as f:
                self.venues = pickle.load(f)
            with open('caterers.pickle', 'rb') as f:
                self.caterers = pickle.load(f)
        except FileNotFoundError:
            pass
    # Save data from lists into respective pickle files.
    def saveData(self):
        with open('employees.pickle', 'wb') as f:
            pickle.dump(self.employees, f)
        with open('events.pickle', 'wb') as f:
            pickle.dump(self.events, f)
        with open('clients.pickle', 'wb') as f:
            pickle.dump(self.clients, f)
        with open('guests.pickle', 'wb') as f:
            pickle.dump(self.guests, f)
        with open('venues.pickle', 'wb') as f:
            pickle.dump(self.venues, f)
        with open('caterers.pickle', 'wb') as f:
            pickle.dump(self.caterers, f)

    # Methods for managing employees
    def addEmployee(self, employee):
        self.employees.append(employee)

    def deleteEmployee(self, employeeId):
        for i, employee in enumerate(self.employees):
            if employee.employeeId == employeeId:
                del self.employees[i]
                break

    def modifyEmployee(self, employeeId, newEmployee):
        for i, employee in enumerate(self.employees):
            if employee.employeeId == employeeId:
                self.employees[i] = newEmployee
                break

    def displayEmployee(self, employeeId):
        for employee in self.employees:
            if employee.employeeId == employeeId:
                print(employee)
                break

    def displayAllEmployees(self):
        for employee in self.employees:
            print(employee)

    # Methods for managing events
    def addEvent(self, event):
        self.events.append(event)

    def deleteEvent(self, eventId):
        for i, event in enumerate(self.events):
            if event.eventId == eventId:
                del self.events[i]
                break

    def modifyEvent(self, eventId, newEvent):
        for i, event in enumerate(self.events):
            if event.eventId == eventId:
                self.events[i] = newEvent
                break

    def displayEvent(self, eventId):
        for event in self.events:
            if event.eventId == eventId:
                print(event)
                break

    def displayAllEvents(self):
        for event in self.events:
            print(event)

    # Methods for managing clients
    def addClient(self, client):
        self.clients.append(client)

    def deleteClient(self, clientId):
        for i, client in enumerate(self.clients):
            if client.clientId == clientId:
                del self.clients[i]
                break

    def modifyClient(self, clientId, newClient):
        for i, client in enumerate(self.clients):
            if client.clientId == clientId:
                self.clients[i] = newClient
                break

    def displayClient(self, clientId):
        for client in self.clients:
            if client.clientId == clientId:
                print(client)
                break

    def displayAllClients(self):
        for client in self.clients:
            print(client)

    # Methods for managing guests
    def addGuest(self, guest):
        self.guests.append(guest)

    def deleteGuest(self, guestId):
        for i, guest in enumerate(self.guests):
            if guest.guestId == guestId:
                del self.guests[i]
                break

    def modifyGuest(self, guestId, newGuest):
        for i, guest in enumerate(self.guests):
            if guest.guestId == guestId:
                self.guests[i] = newGuest
                break

    def displayGuest(self, guestId):
        for guest in self.guests:
            if guest.guestId == guestId:
                print(guest)
                break

    def displayAllGuests(self):
        for guest in self.guests:
            print(guest)

    # Methods for managing Venue
    def addVenue(self, venue):
        self.venues.append(venue)

    def deleteVenue(self, venueId):
        for i, venue in enumerate(self.venues):
            if venue.venueId == venueId:
                del self.venues[i]
                break

    def modifyVenue(self, venueId, newVenue):
        for i, venue in enumerate(self.venues):
            if venue.venueId == venueId:
                self.venues[i] = newVenue
                break

    def displayVenue(self, venueId):
        for venue in self.venues:
            if venue.venueId == venueId:
                print(venue)
                break

    def displayAllVenues(self):
        for venue in self.venues:
            print(venue)

    # Methods for managing caterer
    def addCaterer(self, caterer):
        self.caterers.append(caterer)

    def deleteCaterer(self, catererId):
        for i, caterer in enumerate(self.caterers):
            if caterer.catererId == catererId:
                del self.caterers[i]
                break

    def modifyCaterer(self, catererId, newCaterer):
        for i, caterer in enumerate(self.caterers):
            if caterer.catererId == catererId:
                self.caterers[i] = newCaterer
                break

    def displayCaterer(self, catererId):
        for caterer in self.caterers:
            if caterer.catererId == catererId:
                print(caterer)
                break

    def displayAllCaterers(self):
        for caterer in self.caterers:
            print(caterer)

    # Methods for managing supplier
    def addSupplier(self, supplier):
        # Add the supplier to the list
        self.suppliers.append(supplier)

    def deleteSupplier(self, supplierId):
        # Delete the supplier from the list based on ID
        for i, supplier in enumerate(self.suppliers):
            if supplier.supplierId == supplierId:
                del self.suppliers[i]
                break

    def modifySupplier(self, supplierId, newSupplier):
        # Modify the details of the supplier in the list
        for i, supplier in enumerate(self.suppliers):
            if supplier.supplierId == supplierId:
                self.suppliers[i] = newSupplier
                break

    def displaySupplier(self, supplierId):
        # Display the details of a specific supplier from the list based on ID
        for supplier in self.suppliers:
            if supplier.supplierId == supplierId:
                print(supplier)  # Or display in your GUI
                break

    def displayAllSuppliers(self):
        # Display all suppliers in the list
        for supplier in self.suppliers:
            print(supplier)


class EventManagementSystemGUI(EventManagementSystem):
    # Initialize the GUI by inheriting from the EventManagementSystem class
    def __init__(self, master):
        super().__init__()
        self.master = master
        master.title("Event Management System")
        self.loadData() # Load existing data when GUI starts
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(fill=BOTH, expand=True)

        # Create tabs
        self.employeeTab = ttk.Frame(self.notebook)
        self.notebook.add(self.employeeTab, text="Employees")
        # Add Employee Section
        self.addEmployeeFrame = ttk.LabelFrame(self.employeeTab, text="Add Employee")
        self.addEmployeeFrame.grid(row=0, column=0, padx=10, pady=10)
        # Add input fields for employee details.
        self.nameLabel = ttk.Label(self.addEmployeeFrame, text="Name:")
        self.nameLabel.grid(row=0, column=0, padx=5, pady=5)
        self.nameEntry = ttk.Entry(self.addEmployeeFrame)
        self.nameEntry.grid(row=0, column=1, padx=5, pady=5)
        self.idLabel = ttk.Label(self.addEmployeeFrame, text="Employee ID:")
        self.idLabel.grid(row=1, column=0, padx=5, pady=5)
        self.idEntry = ttk.Entry(self.addEmployeeFrame)
        self.idEntry.grid(row=1, column=1, padx=5, pady=5)
        self.departmentLabel = ttk.Label(self.addEmployeeFrame, text="Department:")
        self.departmentLabel.grid(row=2, column=0, padx=5, pady=5)
        self.departmentEntry = ttk.Entry(self.addEmployeeFrame)
        self.departmentEntry.grid(row=2, column=1, padx=5, pady=5)
        self.jobTitleLabel = ttk.Label(self.addEmployeeFrame, text="Job Title:")
        self.jobTitleLabel.grid(row=3, column=0, padx=5, pady=5)
        self.jobTitleEntry = ttk.Entry(self.addEmployeeFrame)
        self.jobTitleEntry.grid(row=3, column=1, padx=5, pady=5)
        self.salaryLabel = ttk.Label(self.addEmployeeFrame, text="Basic Salary:")
        self.salaryLabel.grid(row=4, column=0, padx=5, pady=5)
        self.salaryEntry = ttk.Entry(self.addEmployeeFrame)
        self.salaryEntry.grid(row=4, column=1, padx=5, pady=5)
        self.managerIdLabel = ttk.Label(self.addEmployeeFrame, text="Manager ID:")
        self.managerIdLabel.grid(row=5, column=0, padx=5, pady=5)
        self.managerIdEntry = ttk.Entry(self.addEmployeeFrame)
        self.managerIdEntry.grid(row=5, column=1, padx=5, pady=5)
        self.addEmployeeButton = ttk.Button(self.addEmployeeFrame, text="Add Employee", command=self.addEmployeeHandler)
        self.addEmployeeButton.grid(row=6, column=0, columnspan=2, padx=5, pady=5)
        # Delete Employee Section
        self.deleteEmployeeFrame = ttk.LabelFrame(self.employeeTab, text="Delete Employee")
        self.deleteEmployeeFrame.grid(row=0, column=1, padx=10, pady=10)
        self.deleteIdLabel = ttk.Label(self.deleteEmployeeFrame, text="Employee ID:")
        self.deleteIdLabel.grid(row=0, column=0, padx=5, pady=5)
        self.deleteIdEntry = ttk.Entry(self.deleteEmployeeFrame)
        self.deleteIdEntry.grid(row=0, column=1, padx=5, pady=5)
        self.deleteEmployeeButton = ttk.Button(self.deleteEmployeeFrame, text="Delete Employee", command=self.deleteEmployeeHandler)
        self.deleteEmployeeButton.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        # Modify Employee Section
        self.modifyEmployeeFrame = ttk.LabelFrame(self.employeeTab, text="Modify Employee")
        self.modifyEmployeeFrame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        self.modifyIdLabel = ttk.Label(self.modifyEmployeeFrame, text="Employee ID:")
        self.modifyIdLabel.grid(row=0, column=0, padx=5, pady=5)
        self.modifyIdEntry = ttk.Entry(self.modifyEmployeeFrame)
        self.modifyIdEntry.grid(row=0, column=1, padx=5, pady=5)
        self.modifyNameLabel = ttk.Label(self.modifyEmployeeFrame, text="New Name:")
        self.modifyNameLabel.grid(row=1, column=0, padx=5, pady=5)
        self.modifyNameEntry = ttk.Entry(self.modifyEmployeeFrame)
        self.modifyNameEntry.grid(row=1, column=1, padx=5, pady=5)
        self.modifyDepartmentLabel = ttk.Label(self.modifyEmployeeFrame, text="New Department:")
        self.modifyDepartmentLabel.grid(row=2, column=0, padx=5, pady=5)
        self.modifyDepartmentEntry = ttk.Entry(self.modifyEmployeeFrame)
        self.modifyDepartmentEntry.grid(row=2, column=1, padx=5, pady=5)
        self.modifyJobTitleLabel = ttk.Label(self.modifyEmployeeFrame, text="New Job Title:")
        self.modifyJobTitleLabel.grid(row=3, column=0, padx=5, pady=5)
        self.modifyJobTitleEntry = ttk.Entry(self.modifyEmployeeFrame)
        self.modifyJobTitleEntry.grid(row=3, column=1, padx=5, pady=5)
        self.modifySalaryLabel = ttk.Label(self.modifyEmployeeFrame, text="New Basic Salary:")
        self.modifySalaryLabel.grid(row=4, column=0, padx=5, pady=5)
        self.modifySalaryEntry = ttk.Entry(self.modifyEmployeeFrame)
        self.modifySalaryEntry.grid(row=4, column=1, padx=5, pady=5)
        self.modifyManagerIdLabel = ttk.Label(self.modifyEmployeeFrame, text="New Manager ID:")
        self.modifyManagerIdLabel.grid(row=5, column=0, padx=5, pady=5)
        self.modifyManagerIdEntry = ttk.Entry(self.modifyEmployeeFrame)
        self.modifyManagerIdEntry.grid(row=5, column=1, padx=5, pady=5)
        self.modifyEmployeeButton = ttk.Button(self.modifyEmployeeFrame, text="Modify Employee", command=self.modifyEmployeeHandler)
        self.modifyEmployeeButton.grid(row=6, column=0, columnspan=2, padx=5, pady=5)
        # Display Employee Section
        self.displayEmployeeFrame = ttk.LabelFrame(self.employeeTab, text="Display Employee")
        self.displayEmployeeFrame.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        self.displayIdLabel = ttk.Label(self.displayEmployeeFrame, text="Employee ID:")
        self.displayIdLabel.grid(row=0, column=0, padx=5, pady=5)
        self.displayIdEntry = ttk.Entry(self.displayEmployeeFrame)
        self.displayIdEntry.grid(row=0, column=1, padx=5, pady=5)
        self.displayEmployeeButton = ttk.Button(self.displayEmployeeFrame, text="Display Employee", command=self.displayEmployeeHandler)
        self.displayEmployeeButton.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        # Display All Employees Section
        self.displayAllEmployeesFrame = ttk.LabelFrame(self.employeeTab, text="Display All Employees")
        self.displayAllEmployeesFrame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        self.displayAllEmployeesButton = ttk.Button(self.displayAllEmployeesFrame, text="Display All Employees", command=self.displayAllEmployeesHandler)
        self.displayAllEmployeesButton.grid(row=0, column=0, padx=5, pady=5)

        # Event Tab
        self.eventTab = ttk.Frame(self.notebook)
        self.notebook.add(self.eventTab, text="Events")
        # Add Event Section
        self.addEventFrame = ttk.LabelFrame(self.eventTab, text="Add Event")
        self.addEventFrame.grid(row=0, column=0, padx=10, pady=10)
        # Add input fields for event details.
        self.eventIdLabel = ttk.Label(self.addEventFrame, text="Event ID:")
        self.eventIdLabel.grid(row=0, column=0, padx=5, pady=5)
        self.eventIdEntry = ttk.Entry(self.addEventFrame)
        self.eventIdEntry.grid(row=0, column=1, padx=5, pady=5)
        self.eventTypeLabel = ttk.Label(self.addEventFrame, text="Event Type:")
        self.eventTypeLabel.grid(row=1, column=0, padx=5, pady=5)
        self.eventTypeEntry = ttk.Entry(self.addEventFrame)
        self.eventTypeEntry.grid(row=1, column=1, padx=5, pady=5)
        self.themeLabel = ttk.Label(self.addEventFrame, text="Theme:")
        self.themeLabel.grid(row=2, column=0, padx=5, pady=5)
        self.themeEntry = ttk.Entry(self.addEventFrame)
        self.themeEntry.grid(row=2, column=1, padx=5, pady=5)
        self.dateLabel = ttk.Label(self.addEventFrame, text="Date:")
        self.dateLabel.grid(row=3, column=0, padx=5, pady=5)
        self.dateEntry = ttk.Entry(self.addEventFrame)
        self.dateEntry.grid(row=3, column=1, padx=5, pady=5)
        self.timeLabel = ttk.Label(self.addEventFrame, text="Time:")
        self.timeLabel.grid(row=4, column=0, padx=5, pady=5)
        self.timeEntry = ttk.Entry(self.addEventFrame)
        self.timeEntry.grid(row=4, column=1, padx=5, pady=5)
        self.durationLabel = ttk.Label(self.addEventFrame, text="Duration:")
        self.durationLabel.grid(row=5, column=0, padx=5, pady=5)
        self.durationEntry = ttk.Entry(self.addEventFrame)
        self.durationEntry.grid(row=5, column=1, padx=5, pady=5)
        self.venueAddressLabel = ttk.Label(self.addEventFrame, text="Venue Address:")
        self.venueAddressLabel.grid(row=6, column=0, padx=5, pady=5)
        self.venueAddressEntry = ttk.Entry(self.addEventFrame)
        self.venueAddressEntry.grid(row=6, column=1, padx=5, pady=5)
        self.clientIdLabel = ttk.Label(self.addEventFrame, text="Client ID:")
        self.clientIdLabel.grid(row=7, column=0, padx=5, pady=5)
        self.clientIdEntry = ttk.Entry(self.addEventFrame)
        self.clientIdEntry.grid(row=7, column=1, padx=5, pady=5)
        self.guestListLabel = ttk.Label(self.addEventFrame, text="Guest List:")
        self.guestListLabel.grid(row=8, column=0, padx=5, pady=5)
        self.guestListEntry = ttk.Entry(self.addEventFrame)
        self.guestListEntry.grid(row=8, column=1, padx=5, pady=5)
        # Add Event Section
        self.addEventButton = ttk.Button(self.addEventFrame, text="Add Event", command=self.addEventHandler)
        self.addEventButton.grid(row=9, column=0, columnspan=2, padx=5, pady=5)
        # Delete Event Section
        self.deleteEventFrame = ttk.LabelFrame(self.eventTab, text="Delete Event")
        self.deleteEventFrame.grid(row=0, column=1, padx=10, pady=10)
        self.deleteEventIdLabel = ttk.Label(self.deleteEventFrame, text="Event ID:")
        self.deleteEventIdLabel.grid(row=0, column=0, padx=5, pady=5)
        self.deleteEventIdEntry = ttk.Entry(self.deleteEventFrame)
        self.deleteEventIdEntry.grid(row=0, column=1, padx=5, pady=5)
        self.deleteEventButton = ttk.Button(self.deleteEventFrame, text="Delete Event", command=self.deleteEventHandler)
        self.deleteEventButton.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        # Client Tab
        self.clientTab = ttk.Frame(self.notebook)
        self.notebook.add(self.clientTab, text="Clients")
        # Add Client Section
        self.addClientFrame = ttk.LabelFrame(self.clientTab, text="Add Client")
        self.addClientFrame.grid(row=0, column=0, padx=10, pady=10)
        # Input fields for adding a new client.
        self.clientNameLabel = ttk.Label(self.addClientFrame, text="Name:")
        self.clientNameLabel.grid(row=0, column=0, padx=5, pady=5)
        self.clientNameEntry = ttk.Entry(self.addClientFrame)
        self.clientNameEntry.grid(row=0, column=1, padx=5, pady=5)
        self.clientIdLabel = ttk.Label(self.addClientFrame, text="Client ID:")
        self.clientIdLabel.grid(row=1, column=0, padx=5, pady=5)
        self.clientIdEntry = ttk.Entry(self.addClientFrame)
        self.clientIdEntry.grid(row=1, column=1, padx=5, pady=5)
        self.clientAddressLabel = ttk.Label(self.addClientFrame, text="Address:")
        self.clientAddressLabel.grid(row=2, column=0, padx=5, pady=5)
        self.clientAddressEntry = ttk.Entry(self.addClientFrame)
        self.clientAddressEntry.grid(row=2, column=1, padx=5, pady=5)
        self.clientContactLabel = ttk.Label(self.addClientFrame, text="Contact Details:")
        self.clientContactLabel.grid(row=3, column=0, padx=5, pady=5)
        self.clientContactEntry = ttk.Entry(self.addClientFrame)
        self.clientContactEntry.grid(row=3, column=1, padx=5, pady=5)
        self.clientBudgetLabel = ttk.Label(self.addClientFrame, text="Budget:")
        self.clientBudgetLabel.grid(row=4, column=0, padx=5, pady=5)
        self.clientBudgetEntry = ttk.Entry(self.addClientFrame)
        self.clientBudgetEntry.grid(row=4, column=1, padx=5, pady=5)
        self.addClientButton = ttk.Button(self.addClientFrame, text="Add Client", command=self.addClientHandler)
        self.addClientButton.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
        # Delete Client Section
        self.deleteClientFrame = ttk.LabelFrame(self.clientTab, text="Delete Client")
        self.deleteClientFrame.grid(row=0, column=1, padx=10, pady=10)
        self.deleteClientIdLabel = ttk.Label(self.deleteClientFrame, text="Client ID:")
        self.deleteClientIdLabel.grid(row=0, column=0, padx=5, pady=5)
        self.deleteClientIdEntry = ttk.Entry(self.deleteClientFrame)
        self.deleteClientIdEntry.grid(row=0, column=1, padx=5, pady=5)
        self.deleteClientButton = ttk.Button(self.deleteClientFrame, text="Delete Client",
                                             command=self.deleteClientHandler)
        self.deleteClientButton.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        # Modify Client Section
        self.modifyClientFrame = ttk.LabelFrame(self.clientTab, text="Modify Client")
        self.modifyClientFrame.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        self.modifyClientIdLabel = ttk.Label(self.modifyClientFrame, text="Client ID:")
        self.modifyClientIdLabel.grid(row=0, column=0, padx=5, pady=5)
        self.modifyClientIdEntry = ttk.Entry(self.modifyClientFrame)
        self.modifyClientIdEntry.grid(row=0, column=1, padx=5, pady=5)
        self.modifyClientNameLabel = ttk.Label(self.modifyClientFrame, text="New Name:")
        self.modifyClientNameLabel.grid(row=1, column=0, padx=5, pady=5)
        self.modifyClientNameEntry = ttk.Entry(self.modifyClientFrame)
        self.modifyClientNameEntry.grid(row=1, column=1, padx=5, pady=5)
        self.modifyClientAddressLabel = ttk.Label(self.modifyClientFrame, text="New Address:")
        self.modifyClientAddressLabel.grid(row=2, column=0, padx=5, pady=5)
        self.modifyClientAddressEntry = ttk.Entry(self.modifyClientFrame)
        self.modifyClientAddressEntry.grid(row=2, column=1, padx=5, pady=5)
        self.modifyClientContactLabel = ttk.Label(self.modifyClientFrame, text="New Contact:")
        self.modifyClientContactLabel.grid(row=3, column=0, padx=5, pady=5)
        self.modifyClientContactEntry = ttk.Entry(self.modifyClientFrame)
        self.modifyClientContactEntry.grid(row=3, column=1, padx=5, pady=5)
        self.modifyClientBudgetLabel = ttk.Label(self.modifyClientFrame, text="New Budget:")
        self.modifyClientBudgetLabel.grid(row=4, column=0, padx=5, pady=5)
        self.modifyClientBudgetEntry = ttk.Entry(self.modifyClientFrame)
        self.modifyClientBudgetEntry.grid(row=4, column=1, padx=5, pady=5)
        self.modifyClientButton = ttk.Button(self.modifyClientFrame, text="Modify Client",
                                             command=self.modifyClientHandler)
        self.modifyClientButton.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
        # Display Client Section
        self.displayClientFrame = ttk.LabelFrame(self.clientTab, text="Display Client")
        self.displayClientFrame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        self.displayClientIdLabel = ttk.Label(self.displayClientFrame, text="Client ID:")
        self.displayClientIdLabel.grid(row=0, column=0, padx=5, pady=5)
        self.displayClientIdEntry = ttk.Entry(self.displayClientFrame)
        self.displayClientIdEntry.grid(row=0, column=1, padx=5, pady=5)
        self.displayClientButton = ttk.Button(self.displayClientFrame, text="Display Client",
                                              command=self.displayClientHandler)
        self.displayClientButton.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        # Display All Clients Section
        self.displayAllClientsFrame = ttk.LabelFrame(self.clientTab, text="Display All Clients")
        self.displayAllClientsFrame.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
        self.displayAllClientsButton = ttk.Button(self.displayAllClientsFrame, text="Display All Clients",
                                                  command=self.displayAllClientsHandler)
        self.displayAllClientsButton.grid(row=0, column=0, padx=5, pady=5)

        self.modifyEventFrame = ttk.LabelFrame(self.eventTab, text="Modify Event")
        self.modifyEventFrame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        self.modifyEventIdLabel = ttk.Label(self.modifyEventFrame, text="Event ID:")
        self.modifyEventIdLabel.grid(row=0, column=0, padx=5, pady=5)
        self.modifyEventIdEntry = ttk.Entry(self.modifyEventFrame)
        self.modifyEventIdEntry.grid(row=0, column=1, padx=5, pady=5)
        self.modifyEventButton = ttk.Button(self.modifyEventFrame, text="Modify Event", command=self.modifyEventHandler)
        self.modifyEventButton.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        self.displayEventFrame = ttk.LabelFrame(self.eventTab, text="Display Event")
        self.displayEventFrame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        self.displayEventIdLabel = ttk.Label(self.displayEventFrame, text="Event ID:")
        self.displayEventIdLabel.grid(row=0, column=0, padx=5, pady=5)
        self.displayEventIdEntry = ttk.Entry(self.displayEventFrame)
        self.displayEventIdEntry.grid(row=0, column=1, padx=5, pady=5)
        self.displayEventButton = ttk.Button(self.displayEventFrame, text="Display Event",
                                             command=self.displayEventHandler)
        self.displayEventButton.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        self.displayAllEventsFrame = ttk.LabelFrame(self.eventTab, text="Display All Events")
        self.displayAllEventsFrame.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
        self.displayAllEventsButton = ttk.Button(self.displayAllEventsFrame, text="Display All Events",
                                                 command=self.displayAllEventsHandler)
        self.displayAllEventsButton.grid(row=0, column=0, padx=5, pady=5)

        # Supplier Tab
        self.supplierTab = ttk.Frame(self.notebook)
        self.notebook.add(self.supplierTab, text="Supplier")
        # Add Supplier Section
        self.addSupplierFrame = ttk.LabelFrame(self.supplierTab, text="Add Supplier")
        self.addSupplierFrame.grid(row=1, column=2, padx=10, pady=10)
        #  Input fields for adding a new supplier
        self.supplierIdLabel = ttk.Label(self.addSupplierFrame, text="Supplier ID:")
        self.supplierIdLabel.grid(row=0, column=0, padx=5, pady=5)
        self.supplierIdEntry = ttk.Entry(self.addSupplierFrame)
        self.supplierIdEntry.grid(row=0, column=1, padx=5, pady=5)
        self.supplierNameLabel = ttk.Label(self.addSupplierFrame, text="Name:")
        self.supplierNameLabel.grid(row=1, column=0, padx=5, pady=5)
        self.supplierNameEntry = ttk.Entry(self.addSupplierFrame)
        self.supplierNameEntry.grid(row=1, column=1, padx=5, pady=5)
        self.supplierAddressLabel = ttk.Label(self.addSupplierFrame, text="Address:")
        self.supplierAddressLabel.grid(row=2, column=0, padx=5, pady=5)
        self.supplierAddressEntry = ttk.Entry(self.addSupplierFrame)
        self.supplierAddressEntry.grid(row=2, column=1, padx=5, pady=5)
        self.supplierContactLabel = ttk.Label(self.addSupplierFrame, text="Contact Details:")
        self.supplierContactLabel.grid(row=3, column=0, padx=5, pady=5)
        self.supplierContactEntry = ttk.Entry(self.addSupplierFrame)
        self.supplierContactEntry.grid(row=3, column=1, padx=5, pady=5)
        self.addSupplierButton = ttk.Button(self.addSupplierFrame, text="Add Supplier",
                                            command=self.addSupplierHandler)
        self.addSupplierButton.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        # # Delete Supplier Section
        self.deleteSupplierFrame = ttk.LabelFrame(self.supplierTab, text="Delete Supplier")
        self.deleteSupplierFrame.grid(row=2, column=2, padx=10, pady=10)
        self.deleteSupplierIdLabel = ttk.Label(self.deleteSupplierFrame, text="Supplier ID:")
        self.deleteSupplierIdLabel.grid(row=0, column=0, padx=5, pady=5)
        self.deleteSupplierIdEntry = ttk.Entry(self.deleteSupplierFrame)
        self.deleteSupplierIdEntry.grid(row=0, column=1, padx=5, pady=5)
        self.deleteSupplierButton = ttk.Button(self.deleteSupplierFrame, text="Delete Supplier",
                                               command=self.deleteSupplierHandler)
        self.deleteSupplierButton.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        # Modify Supplier Section
        self.modifySupplierFrame = ttk.LabelFrame(self.supplierTab, text="Modify Supplier")
        self.modifySupplierFrame.grid(row=2, column=3, padx=10, pady=10)
        self.modifySupplierIdLabel = ttk.Label(self.modifySupplierFrame, text="Supplier ID:")
        self.modifySupplierIdLabel.grid(row=0, column=0, padx=5, pady=5)
        self.modifySupplierIdEntry = ttk.Entry(self.modifySupplierFrame)
        self.modifySupplierIdEntry.grid(row=0, column=1, padx=5, pady=5)
        self.modifySupplierNameLabel = ttk.Label(self.modifySupplierFrame, text="New Name:")
        self.modifySupplierNameLabel.grid(row=1, column=0, padx=5, pady=5)
        self.modifySupplierNameEntry = ttk.Entry(self.modifySupplierFrame)
        self.modifySupplierNameEntry.grid(row=1, column=1, padx=5, pady=5)
        self.modifySupplierAddressLabel = ttk.Label(self.modifySupplierFrame, text="New Address:")
        self.modifySupplierAddressLabel.grid(row=2, column=0, padx=5, pady=5)
        self.modifySupplierAddressEntry = ttk.Entry(self.modifySupplierFrame)
        self.modifySupplierAddressEntry.grid(row=2, column=1, padx=5, pady=5)
        self.modifySupplierContactLabel = ttk.Label(self.modifySupplierFrame, text="New Contact:")
        self.modifySupplierContactLabel.grid(row=3, column=0, padx=5, pady=5)
        self.modifySupplierContactEntry = ttk.Entry(self.modifySupplierFrame)
        self.modifySupplierContactEntry.grid(row=3, column=1, padx=5, pady=5)
        self.modifySupplierButton = ttk.Button(self.modifySupplierFrame, text="Modify Supplier",
                                               command=self.modifySupplierHandler)
        self.modifySupplierButton.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        # Display Supplier Section
        self.displaySupplierFrame = ttk.LabelFrame(self.supplierTab, text="Display Supplier")
        self.displaySupplierFrame.grid(row=3, column=2, padx=10, pady=10)
        self.displaySupplierIdLabel = ttk.Label(self.displaySupplierFrame, text="Supplier ID:")
        self.displaySupplierIdLabel.grid(row=0, column=0, padx=5, pady=5)
        self.displaySupplierIdEntry = ttk.Entry(self.displaySupplierFrame)
        self.displaySupplierIdEntry.grid(row=0, column=1, padx=5, pady=5)
        self.displaySupplierButton = ttk.Button(self.displaySupplierFrame, text="Display Supplier",
                                                command=self.displaySupplierHandler)
        self.displaySupplierButton.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        # Display All Suppliers Section
        self.displayAllSuppliersButton = ttk.Button(self.supplierTab, text="Display All Suppliers",
                                                    command=self.displayAllSuppliersHandler)
        self.displayAllSuppliersButton.grid(row=4, column=2, columnspan=2, padx=5, pady=5)

        # Guests Tab
        self.guestsTab = ttk.Frame(self.notebook)
        self.notebook.add(self.guestsTab, text="Guests")

        # Add Guest Section
        self.addGuestFrame = ttk.LabelFrame(self.guestsTab, text="Add Guest")
        self.addGuestFrame.grid(row=1, column=2, padx=10, pady=10)
        # Input fields for adding a new guest.
        self.guestIdLabel = ttk.Label(self.addGuestFrame, text="Guest ID:")
        self.guestIdLabel.grid(row=0, column=0, padx=5, pady=5)
        self.guestIdEntry = ttk.Entry(self.addGuestFrame)
        self.guestIdEntry.grid(row=0, column=1, padx=5, pady=5)
        self.guestNameLabel = ttk.Label(self.addGuestFrame, text="Name:")
        self.guestNameLabel.grid(row=1, column=0, padx=5, pady=5)
        self.guestNameEntry = ttk.Entry(self.addGuestFrame)
        self.guestNameEntry.grid(row=1, column=1, padx=5, pady=5)
        self.guestAgeLabel = ttk.Label(self.addGuestFrame, text="Age:")
        self.guestAgeLabel.grid(row=2, column=0, padx=5, pady=5)
        self.guestAgeEntry = ttk.Entry(self.addGuestFrame)
        self.guestAgeEntry.grid(row=2, column=1, padx=5, pady=5)
        self.guestEmailLabel = ttk.Label(self.addGuestFrame, text="Email:")
        self.guestEmailLabel.grid(row=3, column=0, padx=5, pady=5)
        self.guestEmailEntry = ttk.Entry(self.addGuestFrame)
        self.guestEmailEntry.grid(row=3, column=1, padx=5, pady=5)
        self.addGuestButton = ttk.Button(self.addGuestFrame, text="Add Guest",
                                         command=self.addGuestHandler)
        self.addGuestButton.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        # Delete Guest Section
        self.deleteGuestFrame = ttk.LabelFrame(self.guestsTab, text="Delete Guest")
        self.deleteGuestFrame.grid(row=2, column=2, padx=10, pady=10)
        self.deleteGuestIdLabel = ttk.Label(self.deleteGuestFrame, text="Guest ID:")
        self.deleteGuestIdLabel.grid(row=0, column=0, padx=5, pady=5)
        self.deleteGuestIdEntry = ttk.Entry(self.deleteGuestFrame)
        self.deleteGuestIdEntry.grid(row=0, column=1, padx=5, pady=5)
        self.deleteGuestButton = ttk.Button(self.deleteGuestFrame, text="Delete Guest",
                                            command=self.deleteGuestHandler)
        self.deleteGuestButton.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        # Modify Guest Section
        self.modifyGuestFrame = ttk.LabelFrame(self.guestsTab, text="Modify Guest")
        self.modifyGuestFrame.grid(row=2, column=3, padx=10, pady=10)
        self.modifyGuestIdLabel = ttk.Label(self.modifyGuestFrame, text="Guest ID:")
        self.modifyGuestIdLabel.grid(row=0, column=0, padx=5, pady=5)
        self.modifyGuestIdEntry = ttk.Entry(self.modifyGuestFrame)
        self.modifyGuestIdEntry.grid(row=0, column=1, padx=5, pady=5)
        self.modifyGuestNameLabel = ttk.Label(self.modifyGuestFrame, text="New Name:")
        self.modifyGuestNameLabel.grid(row=1, column=0, padx=5, pady=5)
        self.modifyGuestNameEntry = ttk.Entry(self.modifyGuestFrame)
        self.modifyGuestNameEntry.grid(row=1, column=1, padx=5, pady=5)
        self.modifyGuestAgeLabel = ttk.Label(self.modifyGuestFrame, text="New Age:")
        self.modifyGuestAgeLabel.grid(row=2, column=0, padx=5, pady=5)
        self.modifyGuestAgeEntry = ttk.Entry(self.modifyGuestFrame)
        self.modifyGuestAgeEntry.grid(row=2, column=1, padx=5, pady=5)
        self.modifyGuestEmailLabel = ttk.Label(self.modifyGuestFrame, text="New Email:")
        self.modifyGuestEmailLabel.grid(row=3, column=0, padx=5, pady=5)
        self.modifyGuestEmailEntry = ttk.Entry(self.modifyGuestFrame)
        self.modifyGuestEmailEntry.grid(row=3, column=1, padx=5, pady=5)
        self.modifyGuestButton = ttk.Button(self.modifyGuestFrame, text="Modify Guest",
                                            command=self.modifyGuestHandler)
        self.modifyGuestButton.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        # Display Guest Section
        self.displayGuestFrame = ttk.LabelFrame(self.guestsTab, text="Display Guest")
        self.displayGuestFrame.grid(row=3, column=2, padx=10, pady=10)
        self.displayGuestIdLabel = ttk.Label(self.displayGuestFrame, text="Guest ID:")
        self.displayGuestIdLabel.grid(row=0, column=0, padx=5, pady=5)
        self.displayGuestIdEntry = ttk.Entry(self.displayGuestFrame)
        self.displayGuestIdEntry.grid(row=0, column=1, padx=5, pady=5)
        self.displayGuestButton = ttk.Button(self.displayGuestFrame, text="Display Guest",
                                             command=self.displayGuestHandler)
        self.displayGuestButton.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        # Display All Guests Section
        self.displayAllGuestsButton = ttk.Button(self.guestsTab, text="Display All Guests",
                                                 command=self.displayAllGuestsHandler)
        self.displayAllGuestsButton.grid(row=4, column=2, columnspan=2, padx=5, pady=5)
        # Caterers Tab
        self.caterersTab = ttk.Frame(self.notebook)
        self.notebook.add(self.caterersTab, text="Caterers")
        # Add Caterer Section
        self.addCatererFrame = ttk.LabelFrame(self.caterersTab, text="Add Caterer")
        self.addCatererFrame.grid(row=1, column=2, padx=10, pady=10)
        self.catererIdLabel = ttk.Label(self.addCatererFrame, text="Caterer ID:")
        self.catererIdLabel.grid(row=0, column=0, padx=5, pady=5)
        self.catererIdEntry = ttk.Entry(self.addCatererFrame)
        self.catererIdEntry.grid(row=0, column=1, padx=5, pady=5)
        self.catererNameLabel = ttk.Label(self.addCatererFrame, text="Name:")
        self.catererNameLabel.grid(row=1, column=0, padx=5, pady=5)
        self.catererNameEntry = ttk.Entry(self.addCatererFrame)
        self.catererNameEntry.grid(row=1, column=1, padx=5, pady=5)
        self.catererCuisineLabel = ttk.Label(self.addCatererFrame, text="Cuisine:")
        self.catererCuisineLabel.grid(row=2, column=0, padx=5, pady=5)
        self.catererCuisineEntry = ttk.Entry(self.addCatererFrame)
        self.catererCuisineEntry.grid(row=2, column=1, padx=5, pady=5)
        self.catererContactLabel = ttk.Label(self.addCatererFrame, text="Contact:")
        self.catererContactLabel.grid(row=3, column=0, padx=5, pady=5)
        self.catererContactEntry = ttk.Entry(self.addCatererFrame)
        self.catererContactEntry.grid(row=3, column=1, padx=5, pady=5)
        self.addCatererButton = ttk.Button(self.addCatererFrame, text="Add Caterer",
                                           command=self.addCatererHandler)
        self.addCatererButton.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        # Delete Caterer Section
        self.deleteCatererFrame = ttk.LabelFrame(self.caterersTab, text="Delete Caterer")
        self.deleteCatererFrame.grid(row=2, column=2, padx=10, pady=10)
        self.deleteCatererIdLabel = ttk.Label(self.deleteCatererFrame, text="Caterer ID:")
        self.deleteCatererIdLabel.grid(row=0, column=0, padx=5, pady=5)
        self.deleteCatererIdEntry = ttk.Entry(self.deleteCatererFrame)
        self.deleteCatererIdEntry.grid(row=0, column=1, padx=5, pady=5)
        self.deleteCatererButton = ttk.Button(self.deleteCatererFrame, text="Delete Caterer",
                                              command=self.deleteCatererHandler)
        self.deleteCatererButton.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        # Modify Caterer Section
        self.modifyCatererFrame = ttk.LabelFrame(self.caterersTab, text="Modify Caterer")
        self.modifyCatererFrame.grid(row=2, column=3, padx=10, pady=10)
        self.modifyCatererIdLabel = ttk.Label(self.modifyCatererFrame, text="Caterer ID:")
        self.modifyCatererIdLabel.grid(row=0, column=0, padx=5, pady=5)
        self.modifyCatererIdEntry = ttk.Entry(self.modifyCatererFrame)
        self.modifyCatererIdEntry.grid(row=0, column=1, padx=5, pady=5)
        self.modifyCatererNameLabel = ttk.Label(self.modifyCatererFrame, text="New Name:")
        self.modifyCatererNameLabel.grid(row=1, column=0, padx=5, pady=5)
        self.modifyCatererNameEntry = ttk.Entry(self.modifyCatererFrame)
        self.modifyCatererNameEntry.grid(row=1, column=1, padx=5, pady=5)
        self.modifyCatererCuisineLabel = ttk.Label(self.modifyCatererFrame, text="New Cuisine:")
        self.modifyCatererCuisineLabel.grid(row=2, column=0, padx=5, pady=5)
        self.modifyCatererCuisineEntry = ttk.Entry(self.modifyCatererFrame)
        self.modifyCatererCuisineEntry.grid(row=2, column=1, padx=5, pady=5)
        self.modifyCatererContactLabel = ttk.Label(self.modifyCatererFrame, text="New Contact:")
        self.modifyCatererContactLabel.grid(row=3, column=0, padx=5, pady=5)
        self.modifyCatererContactEntry = ttk.Entry(self.modifyCatererFrame)
        self.modifyCatererContactEntry.grid(row=3, column=1, padx=5, pady=5)
        self.modifyCatererButton = ttk.Button(self.modifyCatererFrame, text="Modify Caterer",
                                              command=self.modifyCatererHandler)
        self.modifyCatererButton.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        # Display Caterer Section
        self.displayCatererFrame = ttk.LabelFrame(self.caterersTab, text="Display Caterer")
        self.displayCatererFrame.grid(row=3, column=2, padx=10, pady=10)
        self.displayCatererIdLabel = ttk.Label(self.displayCatererFrame, text="Caterer ID:")
        self.displayCatererIdLabel.grid(row=0, column=0, padx=5, pady=5)
        self.displayCatererIdEntry = ttk.Entry(self.displayCatererFrame)
        self.displayCatererIdEntry.grid(row=0, column=1, padx=5, pady=5)
        self.displayCatererButton = ttk.Button(self.displayCatererFrame, text="Display Caterer",
                                               command=self.displayCatererHandler)
        self.displayCatererButton.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        # Display All Caterers Section
        self.displayAllCaterersButton = ttk.Button(self.caterersTab, text="Display All Caterers",
                                                   command=self.displayAllCaterersHandler)
        self.displayAllCaterersButton.grid(row=4, column=2, columnspan=2, padx=5, pady=5)

    # Define a method to display an error message using a message box
    def displayErrorMessage(self, message):
        messagebox.showerror("Sorry, There is an error in the given input.", message)

    def addEmployeeHandler(self):
        # Retrieve input values from entry fields
        name = self.nameEntry.get()
        employeeId = self.idEntry.get()
        department = self.departmentEntry.get()
        jobTitle = self.jobTitleEntry.get()
        basicSalary = self.salaryEntry.get()
        managerId = self.managerIdEntry.get()
        # Create an Employee object with the retrieved values
        employee = Employee(name, employeeId, department, jobTitle, basicSalary, managerId)
        # Call the method to add the new employee
        self.addEmployee(employee)
        # Clear all entry
        self.clearEmployeeEntries()

    # Define a method to handle deleting an employee
    def deleteEmployeeHandler(self):
        # Retrieve the employee ID
        employeeId = self.deleteIdEntry.get()
        # Call the method to delete the employee with the given ID
        self.deleteEmployee(employeeId)
        # Clear the entry field for employee ID
        self.deleteIdEntry.delete(0, END)

    # Define a method to handle modifying an employee's details
    def modifyEmployeeHandler(self):
        # Retrieve the employee ID
        employeeId = self.modifyIdEntry.get()
        newName = self.modifyNameEntry.get()
        newDepartment = self.modifyDepartmentEntry.get()
        newJobTitle = self.modifyJobTitleEntry.get()
        newBasicSalary = self.modifySalaryEntry.get()
        newManagerId = self.modifyManagerIdEntry.get()
        # Create a new Employee object with the updated details
        newEmployee = Employee(newName, employeeId, newDepartment, newJobTitle, newBasicSalary,
                               newManagerId)
        # Call the method to modify the employee's details
        self.modifyEmployee(employeeId, newEmployee)
        # Clear all entry fields related to modifying employee details
        self.clearModifyEmployeeEntries()

    def displayEmployeeHandler(self):
        employeeId = self.displayIdEntry.get()
        self.displayEmployee(employeeId)
        self.displayIdEntry.delete(0, END)

    # Define a method to handle displaying an employee's details
    def displayAllEmployeesHandler(self):
        self.displayAllEmployees()

    # Define a method to clear all entry fields related to employee details
    def clearEmployeeEntries(self):
        self.nameEntry.delete(0, END)
        self.idEntry.delete(0, END)
        self.departmentEntry.delete(0, END)
        self.jobTitleEntry.delete(0, END)
        self.salaryEntry.delete(0, END)
        self.managerIdEntry.delete(0, END)

    def clearEventEntries(self):
        # Clear the entry fields related to event details
        self.eventIdEntry.delete(0, tk.END)
        self.eventTypeEntry.delete(0, tk.END)
        self.themeEntry.delete(0, tk.END)
        self.dateEntry.delete(0, tk.END)
        self.timeEntry.delete(0, tk.END)
        self.durationEntry.delete(0, tk.END)
        self.venueAddressEntry.delete(0, tk.END)
        self.clientIdEntry.delete(0, tk.END)
        self.guestListEntry.delete(0, tk.END)
    #Define a method to clear all entry fields related to modifying employee
    def clearModifyEmployeeEntries(self):
        self.modifyIdEntry.delete(0, END)
        self.modifyNameEntry.delete(0, END)
        self.modifyDepartmentEntry.delete(0, END)
        self.modifyJobTitleEntry.delete(0, END)
        self.modifySalaryEntry.delete(0, END)
        self.modifyManagerIdEntry.delete(0, END)

    # Define a method to handle adding a new event
    def addEventHandler(self):
        # Retrieve input values from entry fields
        eventId = self.eventIdEntry.get()
        eventType = self.eventTypeEntry.get()
        theme = self.themeEntry.get()
        date = self.dateEntry.get()
        time = self.timeEntry.get()
        duration = self.durationEntry.get()
        venueAddress = self.venueAddressEntry.get()
        clientId = self.clientIdEntry.get()
        guestList = self.guestListEntry.get()
        # Create an Event object with the retrieved values
        event = Event(eventId, eventType, theme, date, time, duration, venueAddress, clientId, guestList, None,
                      None, None, None, None, None)
        # Call the method to add the new event
        self.addEvent(event)
        # Clear all entry fields related to event details
        self.clearEventEntries()

    # Define a method to handle
    def deleteEventHandler(self):
        # Retrieve the event ID
        eventId = self.deleteEventIdEntry.get()
        # Call the method to delete the event
        self.deleteEvent(eventId)
        # Clear the entry field for event ID
        self.deleteEventIdEntry.delete(0, END)

    # Define a method to handle adding a new client
    def addClientHandler(self):
        # Retrieve input values from entry fields
        name = self.clientNameEntry.get()
        clientId = self.clientIdEntry.get()
        address = self.clientAddressEntry.get()
        contactDetails = self.clientContactEntry.get()
        budget = self.clientBudgetEntry.get()

        # Create a Client object
        client = Client(clientId, name, address, contactDetails, budget)
        self.addClient(client)
        self.clearClientEntries()

    # Define a method to handle deleting a client
    def deleteClientHandler(self):
        # Retrieve the client ID
        clientId = self.deleteClientIdEntry.get()
        # Call the method to delete
        self.deleteClient(clientId)
        # Clear the entry field for client ID
        self.deleteClientIdEntry.delete(0, END)

    # Define a method to clear all entry fields related to client details
    def clearClientEntries(self):
        self.clientNameEntry.delete(0, END)
        self.clientIdEntry.delete(0, END)
        self.clientAddressEntry.delete(0, END)
        self.clientContactEntry.delete(0, END)
        self.clientBudgetEntry.delete(0, END)

    def clearModifyClientEntries(self):
        # Clear the entry fields related to modifying client details
        self.modifyClientIdEntry.delete(0, tk.END)
        self.modifyClientNameEntry.delete(0, tk.END)
        self.modifyClientAddressEntry.delete(0, tk.END)
        self.modifyClientContactEntry.delete(0, tk.END)
        self.modifyClientBudgetEntry.delete(0, tk.END)

    def modifyClientHandler(self):
        # Retrieve the client ID and new details from entry fields
        clientId = self.modifyClientIdEntry.get()
        newName = self.modifyClientNameEntry.get()
        newAddress = self.modifyClientAddressEntry.get()
        newContactDetails = self.modifyClientContactEntry.get()
        newBudget = self.modifyClientBudgetEntry.get()
        # Create a new Client object with the updated details
        newClient = Client(clientId, newName, newAddress, newContactDetails, newBudget)
        self.modifyClient(clientId, newClient)
        self.clearModifyClientEntries()

    # Define a method to handle displaying a client's details
    def displayClientHandler(self):
        clientId = self.displayClientIdEntry.get()
        self.displayClient(clientId)
        # Clear the entry field for client ID
        self.displayClientIdEntry.delete(0, END)

    # Define a method to handle displaying details of all clients
    def displayAllClientsHandler(self):
        self.displayAllClients()

    # Define a method to clear entry fields related to modifying event details
    def clearModifyEventEntries(self):
        # Clear the entry fields related to modifying event details
        self.modifyEventIdEntry.delete(0, tk.END)

    # Define a method to handle modifying an event
    def modifyEventHandler(self):
        eventId = self.modifyEventIdEntry.get()
        newEvent = Event(...)
        self.modifyEvent(eventId, newEvent)
        self.clearModifyEventEntries()

    # Define a method to handle displaying details of an event
    def displayEventHandler(self):
        eventId = self.displayEventIdEntry.get()
        self.displayEvent(eventId)
        self.displayEventIdEntry.delete(0, END)

    # Define a method to handle displaying details of all events
    def displayAllEventsHandler(self):
        self.displayAllEvents()

    # Define methods to handle adding, deleting, modifying, and displaying suppliers, guests, and caterers
    def addSupplierHandler(self):
        supplierId = self.supplierIdEntry.get()
        name = self.supplierNameEntry.get()
        address = self.supplierAddressEntry.get()
        contactDetails = self.supplierContactEntry.get()
        newSupplier = Supplier(supplierId, name, address, contactDetails)
        self.addSupplier(newSupplier)

    def deleteSupplierHandler(self):
        supplierId = self.deleteSupplierIdEntry.get()
        self.deleteSupplier(supplierId)

    def modifySupplierHandler(self):
        supplierId = self.modifySupplierIdEntry.get()
        name = self.modifySupplierNameEntry.get()
        address = self.modifySupplierAddressEntry.get()
        contactDetails = self.modifySupplierContactEntry.get()
        newSupplier = Supplier(supplierId, name, address, contactDetails)
        self.modifySupplier(supplierId, newSupplier)

    def displaySupplierHandler(self):
        supplierId = self.displaySupplierIdEntry.get()
        self.displaySupplier(supplierId)

    def displayAllSuppliersHandler(self):
        self.displayAllSuppliers()

    def addGuestHandler(self):
        guestId = self.guestIdEntry.get()
        name = self.guestNameEntry.get()
        age = self.guestAgeEntry.get()
        email = self.guestEmailEntry.get()
        newGuest = Guest(guestId, name, age, email)
        self.addGuest(newGuest)

    def deleteGuestHandler(self):
        guestId = self.deleteGuestIdEntry.get()
        self.deleteGuest(guestId)

    def modifyGuestHandler(self):
        guestId = self.modifyGuestIdEntry.get()
        name = self.modifyGuestNameEntry.get()
        age = self.modifyGuestAgeEntry.get()
        email = self.modifyGuestEmailEntry.get()
        newGuest = Guest(guestId, name, age, email)
        self.modifyGuest(guestId, newGuest)

    def displayGuestHandler(self):
        guestId = self.displayGuestIdEntry.get()
        self.displayGuest(guestId)

    def displayAllGuestsHandler(self):
        self.displayAllGuests()

    def addCatererHandler(self):
        catererId = self.catererIdEntry.get()
        name = self.catererNameEntry.get()
        cuisine = self.catererCuisineEntry.get()
        contact = self.catererContactEntry.get()
        newCaterer = Caterer(catererId, name, cuisine, contact)
        self.addCaterer(newCaterer)

    def deleteCatererHandler(self):
        catererId = self.deleteCatererIdEntry.get()

        # Check if catererId is empty, contains only spaces, or contains non-digit characters
        if catererId == "" or catererId.isspace() or not catererId.isdigit():
            self.displayErrorMessage("INVALID CATERER ID! Caterer ID cannot be empty or contain non-digit characters.")
            return

        # Check if catererId exists in the list of caterers
        if catererId not in [caterer.catererId for caterer in self.caterers]:
            self.displayErrorMessage("Caterer with ID {} does not exist.".format(catererId))
            return

        # If all checks pass, delete the caterer
        self.deleteCaterer(catererId)

    def modifyCatererHandler(self):
        catererId = self.modifyCatererIdEntry.get()
        name = self.modifyCatererNameEntry.get()
        cuisine = self.modifyCatererCuisineEntry.get()
        contact = self.modifyCatererContactEntry.get()

        # Check if catererId is empty, contains only spaces, or contains non-digit characters
        if catererId == "" or catererId.isspace() or not catererId.isdigit():
            self.displayErrorMessage("INVALID CATERER ID! Caterer ID cannot be empty or contain non-digit characters.")
            return

        # Check if catererId exists in the list of caterers
        if catererId not in [caterer.catererId for caterer in self.caterers]:
            self.displayErrorMessage("Caterer with ID {} does not exist.".format(catererId))
            return

        # Check if name, cuisine, and contact are empty or contain only spaces
        if name == "" or name.isspace():
            self.displayErrorMessage("Name cannot be empty.")
            return
        if cuisine == "" or cuisine.isspace():
            self.displayErrorMessage("Cuisine cannot be empty.")
            return
        if contact == "" or contact.isspace():
            self.displayErrorMessage("Contact cannot be empty.")
            return

        # If all checks pass, create new Caterer object and modify the caterer
        newCaterer = Caterer(catererId, name, cuisine, contact)
        self.modifyCaterer(catererId, newCaterer)

    def displayCatererHandler(self):
        catererId = self.displayCatererIdEntry.get()

        # Check if catererId is empty, contains only spaces, or contains non-digit characters
        if catererId == "" or catererId.isspace() or not catererId.isdigit():
            self.displayErrorMessage("INVALID CATERER ID! Caterer ID cannot be empty or contain non-digit characters.")
            return

        # Check if catererId exists in the list of caterers
        if catererId not in [caterer.catererId for caterer in self.caterers]:
            self.displayErrorMessage("Caterer with ID {} does not exist.".format(catererId))
            return

        # If all checks pass, display the caterer
        self.displayCaterer(catererId)

    def displayAllCaterersHandler(self):
        self.displayAllCaterers()


#The main() function initializes the GUI application and starts the event loop
def main():
    root = Tk()
    app = EventManagementSystemGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
