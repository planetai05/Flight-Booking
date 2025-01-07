from tkinter import * 
from tkinter import ttk
import csv 


flight_info = []
passenger_info = []
passenger_info2 = []
bookings = []
with open(file="flights.csv",mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        dummy_list = []
        dummy_list.append(row['Flight ID'])
        dummy_list.append(row['Departure'])
        dummy_list.append(row['Arrival'])
        dummy_list.append(row['Date'])
        dummy_list.append(row['Time'])
        dummy_list.append(row['Seats Available'])
        flight_info.append(dummy_list)

with open(file="passengers.csv",mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        dummy_list = []
        dummy_list2 = []
        dummy_list.append(row['Passenger_ID'])
        dummy_list.append(row['Name'])
        dummy_list.append(row['Contact'])
        dummy_list.append(row['Booked_Flights'])
        dummy_list2.append(row['Passenger_ID'])
        dummy_list2.append(row['Name'].lower())
        dummy_list2.append(row['Contact'])
        dummy_list2.append(row['Booked_Flights'].lower())
        passenger_info2.append(dummy_list2)
        passenger_info.append(dummy_list)

class Flight:
        global flight_info
        
        def command1():
            for val in my_flight.get_children():
                my_flight.delete(val)
            for val in flight_info:
                if my_str1.get().lower() == "all flights" or my_str1.get() == "":
                    my_flight.insert(parent="",index=END,values=(val[0],val[1],val[2],val[3],val[4],val[5]))
                elif my_str1.get().upper()==val[0]:
                    my_flight.insert(parent="",index=END,values=(val[0],val[1],val[2],val[3],val[4],val[5]))
                        
                

            
        
class Passenger:   
    def command1():
            Label(root, text="Search Passenger Info", fg="#E8BA40",bg="#DED4E8",font=("Aerial",15)).place(x=10,y=375)
            global my_str2
            my_str2 = StringVar()
            my_entry2 = Entry(root,textvariable=my_str2,borderwidth=2)
            my_entry2.place(x=10,y=415)

            my_button2 = Button(root, text="Search Info", command=Search_Info)
            my_button2.place(x=155,y=415)
            global my_passenger
            my_passenger = ttk.Treeview(root,columns=("Passenger_ID","Name","Contact_Details","Booked_flights"),show="headings")
            my_passenger.heading("Passenger_ID",text="Passenger ID")
            my_passenger.heading("Name",text="Name")
            my_passenger.heading("Contact_Details",text="Contact Details")
            my_passenger.heading("Booked_flights",text="Booked Flights")    
            my_passenger.place(x=10,y=450)

def Search_Info():
    global my_passenger
    global my_str2
    global passenger_info
    for result in my_passenger.get_children():
        my_passenger.delete(result)
    for val in passenger_info:
        if my_str2.get().lower() == "all passengers" or my_str2.get() == "":
            my_passenger.insert(parent="",index=END,values=(val[0],val[1],val[2],val[3]))
        elif my_str2.get()==val[0]:
            my_passenger.insert(parent="",index=END,values=(val[0],val[1],val[2],val[3]))
        


class Booking_Details:   
    def book_flight():
            global passenger_info
            Label(root, text="Flight ID", fg="#E8BA40",bg="#DED4E8",font=("Aerial",15)).place(x=1000,y= 385)
            Label(root, text="Flight ID", fg="#E8BA40",bg="#DED4E8",font=("Aerial",15)).place(x=1000,y= 415)
            Label(root, text="Passenger ID", fg="#E8BA40",bg="#DED4E8",font=("Aerial",15)).place(x=1000,y=445)
            Label(root, text="Date", fg="#E8BA40",bg="#DED4E8",font=("Aerial",15)).place(x=1000,y=475)
            global str1,str2,str3,str4
            str1 = StringVar()
            Entry(root,textvariable=str1).place(x=1200,y=385)
            str2 = StringVar()
            Entry(root,textvariable=str2).place(x=1200,y=415)
            str3 = StringVar()
            Entry(root,textvariable=str3).place(x=1200,y=445)
            str4 = StringVar()
            Entry(root,textvariable=str3).place(x=1200,y=475)
            Button(root,text="Check Booking",command=check_availability).place(x=1000,y=515)
            Button(root,text="Cancel Booking",command=cancel_booking).place(x=1100,y=515)
            Button(root,text="Book me",command=booking).place(x=1200,y=515)
            
            
def check_availability():
    global passenger_info2
    global bookings
    global my_listbox
    my_listbox = Listbox(root,height=5,width=50)
    my_listbox.place(x=1000,y=560)
    dummy_list2 = []
    dummy_list2.append(str4.get().lower())
    dummy_list2.append(str1.get())
    dummy_list2.append(str2.get())
    dummy_list2.append(str3.get())
    my_listbox.delete(0,END)
    if dummy_list2 in bookings:
        my_listbox.insert(END,f"You have already booked this flight")
    else:
        my_listbox.insert(END,f"You have not yet booked a flight")

def booking():
    global passenger_info2
    global bookings
    global my_listbox
    my_listbox = Listbox(root,height=5,width=50)
    my_listbox.place(x=1000,y=560)
    dummy_list = ["booked"]
    dummy_list.append(str1.get())
    dummy_list.append(str2.get())
    dummy_list.append(str3.get())
    data = dummy_list.copy()
    my_listbox.delete(0,END)
    if dummy_list in bookings:
        my_listbox.insert(END,f"You have already booked this flight")
    else:
        bookings.append(dummy_list)
        with open("bookings.csv","a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(data)
        my_listbox.insert(END,f"Successfully Booked the flight")

            
def cancel_booking():
    global passenger_info2
    global bookings
    global my_listbox
    my_listbox = Listbox(root,height=5,width=50)
    my_listbox.place(x=1000,y=560)
    dummy_list = ["booked"]
    dummy_list.append(str1.get())
    dummy_list.append(str2.get())
    dummy_list.append(str3.get())
    dummy_list1 = ["cancelled"]
    dummy_list1.append(str1.get())
    dummy_list1.append(str2.get())
    dummy_list1.append(str3.get())
    my_listbox.delete(0,END)
    if (dummy_list not in bookings and dummy_list1 not in bookings) or (dummy_list1 in bookings and dummy_list in bookings):
        my_listbox.insert(END,f"You haven't yet booked this flight")
    else:
        dummy_list.pop(0)
        dummy_list.insert(0,"cancelled")
        data = dummy_list.copy()
        bookings.append(dummy_list)
        with open("bookings.csv","a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(data)
        my_listbox.insert(END,f"Successfully Cancelled the flight")
    


root = Tk()
root.title("Flight Booking System")
root.geometry("1920x1080")
root.configure(bg="#DED4E8")


Label(root, text="Search Flights", fg="#E8BA40",bg="#DED4E8",font=("Aerial",15)).place(x=10,y=20)

my_str1 = StringVar()
my_entry1 = Entry(root,textvariable=my_str1,borderwidth=2)
my_entry1.place(x=10,y=55)

my_button1 = Button(root, text="Check Schedule", command=Flight.command1)
my_button1.place(x=155,y=55)

my_flight = ttk.Treeview(root,columns=("Flight_ID","Departure","Arrival","Date","Time","Seats_Available"),show="headings")
my_flight.heading("Flight_ID",text="Flight ID")
my_flight.heading("Departure",text="Departure")
my_flight.heading("Arrival",text="Arrival")
my_flight.heading("Date",text="Date")
my_flight.heading("Time",text="Time")
my_flight.heading("Seats_Available",text="Seats Available")
my_flight.place(x=10,y=100)


Button(root,text="Search Passanger Info",command=Passenger.command1).place(x=10,y=350)
Button(root,text="Book a Flight",command=Booking_Details.book_flight).place(x=200,y=350)



root.mainloop()