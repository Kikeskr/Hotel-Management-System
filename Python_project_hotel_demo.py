import time

# import project_hotel_reserve
import project_hotel_db2
import project_personal_info_db
import project_demo_db
#from tkcalendar import Calendar
from tkinter import ttk
from tkinter import *
import sys
import re
from time import strftime
import collections
from tkinter import messagebox as mb
import random as rd
activeid = 0
from PIL import ImageTk, Image
bg = "#bcc6cc"
window = Tk()
window.title("Hotel Management")
window.geometry("800x480")

window.config(bg=bg)

# import project_reserve&_personal_info_db

#fx admin
def Admin():
    # def cancel_bookings():
    # opp = entry_room_no.get()
    # if opp == "Enter Room Number*":
    #     mb.showerror('Error', "I don't understand, please input something iterable")
    # elif str(opp) == "":
    #     mb.showerror('Error', 'Please input something iterable')
    # else:
    #     messagebox = mb.askquestion("Unreserve!", "Are you sure you want "
    #                                                 "to unreserve? \nRoom can be taken by another guest"
    #                                                 "", icon='warning')

    #     if messagebox == 'yes':
    #         unreserved = project_hotel_db2.riob(opp, 0)
    #         mb.showinfo('Message', f'Room {opp} successfully unreserved')

    #     else:
    #         mb.showinfo("Return", "Room is still yours")

    #view all data
    def view_personal():
        view_all = project_demo_db.view_guest_details()
        textbox_.delete(1.0, END)
        textbox_.insert(INSERT, f"S/N | FIRST   MIDDLE   LAST NAME\t\t | STREET ADDRESS \t\t\t\t\t| "
                                f"CITY \t | STATE \t | PHONE NUMBER    | EMAIL       \t\t    | DOA \t\t\t\t  | TOA \t| DOL \t\t| TOL | NOA \t| NOK\t| RN\n")
        for i in view_all:
            # textbox_.insert(INSERT, f"{i}\n")


            textbox_.insert(INSERT, f"{i[0]} | {i[1]}       \t {i[2]} \t {i[3]} \t\t| {i[4]} \t\t\t| {i[5]} | {i[6]} | {i[7]}{i[8]} | {i[9]} | {i[10]} | {i[11]} | {i[12]} |"
                                    f" {i[13]} | {i[14]} | {i[15]} | {i[16]}  \n\n")
        # d = len(view_all)
        # textbox_.insert(INSERT, f"The number of guests are {d}")

    #view empty room
    def admin_empty():
        opp = project_hotel_db2.cbr(0)
        textbox_.delete(1.0, END)
        textbox_.insert(INSERT, f"ROOM NUMBER | NUMBER OF BEDS | AC \t\t\t   | TV     \t\t\t| WIFI \t\t| PRICE \n")

        for i in opp:
           textbox_.insert(INSERT, f"{i[1]} \t              | {i[2]}\t\t\t  | {i[3]}\t| {i[4]}\t| {i[5]}\t\t| {i[6]}\n")
      

    #view  booked room
    def admin_booked():

        opp = project_hotel_db2.cbr(1)
        textbox_.delete(1.0, END)
        textbox_.insert(INSERT, f"ROOM NUMBER | NUMBER OF BEDS | AC \t\t\t   | TV     \t\t\t| WIFI \t\t| PRICE \n")

        for i in opp:
           textbox_.insert(INSERT, f"{i[1]} \t              | {i[2]}\t\t\t  | {i[3]}\t| {i[4]}\t| {i[5]}\t\t| {i[6]}\n")

    def clear():
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)
        entry6.delete(0, END)

        global activeid
        activeid = 0
    #view room
    def view_one_room():
        id = entry_select.get()
        result = project_hotel_db2.view_self(id)
        if result == None:
            mb.showerror('Error Message', 'Error, room number does not exist'
                         )
        else:
            clear()
            entry2.insert(0, result[2])
            entry3.insert(0, result[3])
            entry4.insert(0, result[4])
            entry5.insert(0, result[5])
            entry6.insert(0, result[6])
        global activeid
        activeid = id
    #view
    def view():
        opp = project_hotel_db2.view_hotel_details()
        textbox_.delete(1.0, END)
        textbox_.insert(INSERT, f"ROOM NUMBER | NUMBER OF BEDS | AC \t\t\t   | TV     \t\t\t| WIFI \t\t| PRICE \n")

        for i in opp:
           textbox_.insert(INSERT, f"{i[1]} \t              | {i[2]}\t\t\t  | {i[3]}\t| {i[4]}\t| {i[5]}\t\t| {i[6]}\n")
        o = len(opp)
        textbox_.insert(INSERT, f"Number of rooms are {o}")
    #updaterooms
    def update_rooms():
        entry = entry_select.get()
        if int(activeid)>0:
            mb.showinfo('Success message', project_hotel_db2.Update_hotel_details(entry, entry2.get(), entry3.get(),
                                                                                  entry4.get(), entry5.get(), entry6.get()))
        else:
            mb.showerror('Error message', 'Error: The room selected does not exist.\n Please select a valid room')
            view()


    body = Tk()
    body.title("student database")
    body.geometry("800x480")
    body.config(bg="#bcc6cc")

    admin_frame_main = Frame(body, bg="blue", height=500, width=985, highlightbackground="#D5EAF1", highlightthickness=2)
    admin_frame3 = Frame(admin_frame_main, bg="blue", height=330, width=600, highlightbackground="#D5EAF1", highlightthickness=2)
    admin_frame1 = Frame(admin_frame_main, bg="blue", height=495, width=380, highlightbackground="#D5EAF1", highlightthickness=2)

    # labels
    label1 = Label(admin_frame1, text="Hotel Rooms", font=('Times 20 Italics', 25), bg="blue", fg="white")
    label2 = Label(admin_frame3, text="ADMIN", font=('Gothic', 25, 'bold'), bg="blue", fg="white")
    # labelsn = Label(frame1, text="ID:", font=('Aerial', 15), bg="blue", fg="white", borderwidth=1, relief="solid")
    labeln = Label(admin_frame1, text="Bed(s):", font=('Aerial', 15), bg="blue", fg="white", borderwidth=1, relief="solid")
    labelg = Label(admin_frame1, text="AC:", font=('Aerial', 15), bg="blue", fg="white", borderwidth=1, relief="solid")
    labelc = Label(admin_frame1, text="TV:", font=('Aerial', 15), bg="blue", fg="white", borderwidth=1, relief="solid")
    labels = Label(admin_frame1, text="Wifi:", font=('Aerial', 15), bg="blue", fg="white", borderwidth=1, relief="solid")
    label_price = Label(admin_frame1, text="Price:", font=('Aerial', 15), bg="blue", fg="white", borderwidth=1, relief="solid")
    label_select = Label(admin_frame1, text="Room No.:", font=('Helvitica', 11, 'bold',), fg="white", bg="blue",
                         borderwidth=1, relief="solid", height=2)
    label_note = Label(admin_frame_main, text="NOTE: DOA-Date Of Arrival, TOA-Time Of Arrival, DOL-Date Of Leave,\nTOL-Time Of Leave, "
                                          "NOA-Number Of Adults, NOK-Number Of Kids, RN-Room Number ",
                       font=('Italics', 10, 'bold'), bg="blue", fg="black")    #             bg="blue")
    # Entries
    # entry1 = Entry(frame1, font=('Times 20 Italics', 15), width=23)
    entry2 = Entry(admin_frame1, font=('Times 20 Italics', 15), width=23)
    entry3 = Entry(admin_frame1, font=('Times 20 Italics', 15), width=23)
    entry4 = Entry(admin_frame1, font=('Times 20 Italics', 15), width=23)
    entry5 = Entry(admin_frame1, font=('Times 20 Italics', 15), width=23)
    entry6  = Entry(admin_frame1, font=('Times 20 Italics', 15), width=23)


    entry_select = Entry(admin_frame1, font=('Helvitica', 23, 'bold',), width=4, bg="blue", fg="white")
    # buttons
    button1 = Button(admin_frame1, text="Clear", bg="#D5EAF1", fg="black", font=('Aerial', 15, 'bold'), command=clear)
    button2 = Button(admin_frame1, text="View", bg="#D5EAF1", fg="black", font=('Aerial', 15, 'bold'), command=view)
    button_view_guests = Button(admin_frame_main, text="View All Guests", bg="#D5EAF1", fg="black", font=('Aerial', 11, 'bold'), command=view_personal)
    button_view_rooms = Button(admin_frame_main, text="View Booked Rooms", bg="#D5EAF1", fg="black", font=('Aerial', 11, 'bold'), command=admin_booked)
    button_empty_rooms = Button(admin_frame_main, text="View Empty Rooms", bg="#D5EAF1", fg="black", font=('Aerial', 11, 'bold'), command=admin_empty)

    button_select = Button(admin_frame1, text="View Room", bg="#D5EAF1", fg="black", font=('Helvitica', 15, "bold"),
                           activebackground="blue", activeforeground="white", command=view_one_room)
    # button_update = Button(admin_frame1, text="Update", bg="#D5EAF1", fg="black", font=('Helvitica', 15, "bold"),
    #                        activebackground="blue", activeforeground="white", command=update_rooms)
    button_delete = Button(admin_frame1, text="Update", bg="#D5EAF1", fg="black", font=('Helvitica', 15, "bold"),
                           activebackground="blue", activeforeground="white", command=update_rooms)
    button_update_personal_info = Button(admin_frame_main, text="Update\nGuest", bg="#D5EAF1", fg="black", font=('Aerial', 8, "bold"),
                           activebackground="blue", activeforeground="white", width=5)
    # textbox
    scrollbar1 = Scrollbar(admin_frame3, orient='vertical')
    scrollbar2 = Scrollbar(admin_frame3, orient=HORIZONTAL)
    textbox_ = Text(admin_frame3,xscrollcommand=scrollbar2.set, yscrollcommand=scrollbar1.set, font=('Times New Roman', 15), fg="blue", bg="white",
                    height=14, width=70, wrap=NONE)

    # placing all
    admin_frame1.propagate(0)
    admin_frame_main.propagate(0)
    admin_frame3.propagate(False)
    admin_frame_main.place(x=50, y=50)
    admin_frame1.place(x=0, y=0)
    admin_frame3.place(x=381, y=0)#x=435, y=50)
    label1.place(x=80, y=6)
    label2.place(x=600, y=10)
    labeln.place(x=20, y=200)
    labelg.place(x=20, y=250)
    labelc.place(x=20, y=300)
    labels.place(x=20, y=350)
    label_price.place(x=20, y=400)
    entry2.place(x=110, y=200)
    entry3.place(x=110, y=250)
    entry4.place(x=110, y=300)
    entry5.place(x=110, y=350)
    entry6.place(x=110, y=400)
    button1.place(x=170, y=440)
    button2.place(x=260, y=440)
    scrollbar1.pack(side="right", fill=Y)
    textbox_.pack()
    scrollbar1.config(command=textbox_.yview)
    scrollbar2.pack(side="bottom", fill=X)
    scrollbar2.config(command=textbox_.xview)
    label_note.place(x=390, y=340)

    button_view_guests.place(x=386, y=400)
    button_view_rooms.place(x=540, y=400)
    button_empty_rooms.place(x=719, y=400)
    # button_update_personal_info.place(x=386, y=440)
    label_select.place(x=0, y=120)
    entry_select.place(x=75, y=120)
    button_select.place(x=130, y=120)
    # button_update.place(x=60, y=440)
    button_delete.place(x=280, y=120)
    # lup.place(x=120, y=50)
    body.mainloop()

#fx payment
def payments():
    payment_frame = Frame(height=400, width=600, bg="#123456", highlightbackground="#737ca1", highlightthickness=4)
    payment_frame.place(x=100, y=170)
    label = Label(payment_frame, text='Sorry, due to network issues,\n '
                                      'payments are done over the counter,\nThank you'
                                      ' for your patronage', font=('Gothic', 20, 'bold'),
                  bg='#123456', fg='black')
    label.place(x=20, y=20)


def time():
    string = strftime('%A, %B %d, %Y\n%H: %M: %S')
    label_time.config(text=string, font=('Aerial',10, 'bold'))
    label_time.after(1000, time)


#exit f(x)
def Exit():
    messagebox = mb.askquestion("Exit application!", "Are you sure you want "
                                        "to exit?", icon='warning')
    if messagebox =='yes':
        sys.exit()
    else:
        mb.showinfo("Return", "You will now return to the application")



#personal information f(x)
def personal_information():
    global activeid
    activeid = 0

    activeid = id
    def add_new_guest():
        first_name = entry_first_name.get()
        middle_name = entry_middle_name.get()
        last_name = entry_last_name.get()
        address = entry_address.get()
        city = entry_city.get()
        state = entry_state.get()
        country_code = entry_country_code.get()
        phone_no  = entry_phone_no.get()
        email = entry_email.get()
        date1 = entry_mm_dd_yyyy.get()
        time1 = entry_hh_mm.get()
        date2 = entry_mm_dd_yyyy2.get()
        time2 = entry_hh_mm2.get()
        noa = entry_no_adults.get()
        nok = entry_no_kids.get()
        rn = entry_room_no.get()
        if first_name == "First Name*" or middle_name == "Middle Name*"\
                or last_name == "Last Name*" or address == "Street Address*" or city == "City*"\
                or state == "State/Province*" or country_code == "Country code*" or phone_no == "Phone No: -123-4567-890*"\
                or email == "Email: e.g: myemail@gmail.com*" or date1 == "MM-DD-YYYY*" or time1 == "HH:MM*" \
                or date2 == "MM-DD-YYYY*" or time2 == "HH:MM*"\
                or noa == "Digits only*" or nok == "Digits only*" or rn == "":
            mb.showinfo('error', 'Please input your details')
        elif first_name == "" or middle_name == ""\
                or last_name == "" or address == "" or city == ""\
                or state == "" or country_code == "" or phone_no == "" or email =="" or date1 ==""\
                or time1 =="" or date2 =="" or time2 =="" or noa =="" or nok =="" or rn =="":
            mb.showinfo('error', 'Please input your details')
        else:
            reg_no = project_demo_db.get_reg_no()
            mb.showinfo('Information entered', project_demo_db.personal_details(reg_no, first_name, middle_name,
                                                                                last_name,address, city, state, country_code, phone_no, email,
                                                                                date1, time1, date2,
                                                                                time2, noa, nok, rn))
    #bookings fx
    def room_bookings():
        opp = entry_room_no.get()

        if opp == "Enter Room Number*":
            mb.showerror('Error', "I don't understand, please input something iterable")
        elif str(opp) == "":
            mb.showerror('Error', 'Please input something iterable')

        else:
            rooms = project_hotel_db2.kirib(opp)
            g = rooms[7]
            if g == 0:
                mb.showinfo('booked', f'Room {opp} booked successfully')
                taken = project_hotel_db2.riob(opp, 1)

            else:
                mb.showinfo("Error", f"Room {opp} is not available at the moment")
            global activeid
            activeid = 0

    def cancel_bookings():
        opp = entry_room_no.get()
        if opp == "Enter Room Number*":
            mb.showerror('Error', "I don't understand, please input something iterable")
        elif str(opp) == "":
            mb.showerror('Error', 'Please input something iterable')
        else:
            messagebox = mb.askquestion("Unreserve!", "Are you sure you want "
                                                      "to unreserve? \nRoom can be taken by another guest"
                                                      "", icon='warning')

            if messagebox == 'yes':
                unreserved = project_hotel_db2.riob(opp, 0)
                mb.showinfo('Message', f'Room {opp} successfully unreserved')

            else:
                mb.showinfo("Return", "Room is still yours")

    frame2_personal_info = Frame(height=550, width=600, bg="#123456", highlightbackground="#737ca1", highlightthickness=4)

    #LABELS
    label_personal_info = Label(frame2_personal_info, text="PERSONAL INFORMATION:", font=('Aerial', 15), bg="#123456", fg="black")#, borderwidth=1, relief="solid")
    label_address = Label(frame2_personal_info, text="ADDRESS:", font=('Aerial', 15), bg="#123456", fg="black")#, borderwidth=1, relief="solid")
    label_contacts = Label(frame2_personal_info, text="CONTACTS:", font=('Aerial', 15), bg="#123456", fg="black")#, borderwidth=1, relief="solid")
    label_arrival = Label(frame2_personal_info, text="Arrival - "
                                                   "Date and Time",
                          font=('Aerial', 15), bg="#123456", fg="black")
    label_departure = Label(frame2_personal_info, text="Departure - "
                                                     "Date and Time",
                            font=('Aerial', 15), bg="#123456", fg="black")
    label_number_adults = Label(frame2_personal_info, text="Number of adults :",
                                font=('Aerial', 15), bg="#123456", fg="black")
    label_number_kids = Label(frame2_personal_info, text="Number of kids: "
                              , font=('Aerial', 15), bg="#123456",
                              fg="black")
    label_room_no = Label(frame2_personal_info, text="Room number: "
                              , font=('Aerial', 15), bg="#123456",
                              fg="black")
    # entry
    #entries
    entry_first_name = Entry(frame2_personal_info, font=('Times New Roman', 15), width=12, bg="white")
    entry_middle_name = Entry(frame2_personal_info, font=('Times New Roman', 15), width=12, bg="white")
    entry_last_name = Entry(frame2_personal_info, font=('Times New Roman', 15), width=12, bg="white")
    entry_address = Entry(frame2_personal_info, font=('Times New Roman', 15), width=44, bg="white")
    # entry_address2 = Entry(frame2_personal_info, font=('Times New Roman', 15), width=22, bg="white")
    entry_city = Entry(frame2_personal_info, font=('Times New Roman', 15), width=10, bg="white")
    entry_state = Entry(frame2_personal_info, font=('Times New Roman', 15), width=15, bg="white")
    entry_country_code = Entry(frame2_personal_info, font=('Times New Roman', 15), width=15, bg="white")
    entry_phone_no = Entry(frame2_personal_info, font=('Times New Roman', 12), width=28, bg="white")
    entry_email = Entry(frame2_personal_info, font=('Times New Roman', 12), width=28, bg="white")
    entry_mm_dd_yyyy = Entry(frame2_personal_info, font=('Times New Roman', 12), width=18, bg="white")
    entry_hh_mm = Entry(frame2_personal_info, font=('Times New Roman', 12), width=10, bg="white")
    entry_mm_dd_yyyy2 = Entry(frame2_personal_info, font=('Times New Roman', 12), width=18, bg="white")
    entry_hh_mm2 = Entry(frame2_personal_info, font=('Times New Roman', 12), width=10, bg="white")
    entry_no_adults = Entry(frame2_personal_info, font=('Times New Roman', 12), width=10, bg="white")
    entry_no_kids = Entry(frame2_personal_info, font=('Times New Roman', 12), width=10, bg="white")
    entry_room_no = Entry(frame2_personal_info, font=('Times New Roman', 12), bg="white", width=9)

    frame2_personal_info.propagate()
    frame2_personal_info.place(x=100, y=170)

    #button
    button_done = Button(frame2_personal_info, text="Done", font=('Aerial', 15, 'bold'), bg="#123456", activebackground="#123456", bd=2, command=add_new_guest)
    button_reserve = Button(frame2_personal_info, text="Reserve room", font=('Aerial', 10, 'bold'), fg="#536846",
                            bg="#123456", activeforeground="#536846", activebackground="#123456", bd=2, command=room_bookings
                            )
    button_unreserve = Button(frame2_personal_info, text="Unreserve room", font=('Aerial', 10, 'bold'), fg="#536846",
                              bg="#123456", activeforeground="#536846", activebackground="#123456", bd=2, command=cancel_bookings
                              )
#placings
    label_personal_info.place(x=200, y=5)
    entry_first_name.place(x=30, y=49)
    entry_middle_name.place(x=250, y=49)
    entry_last_name.place(x=450, y=49)
    label_address.place(x=220, y=90)
    entry_address.place(x=30, y=124)
    # entry_address2.place(x=300, y=164)
    entry_city.place(x=30, y=164)
    entry_state.place(x=180, y=164)
    entry_country_code.place(x=370, y=164)
    label_contacts.place(x=200, y=199)
    entry_phone_no.place(x=30, y=230)
    entry_email.place(x=350, y=230)
    label_arrival.place(x=200, y=260)
    entry_mm_dd_yyyy.place(x=30, y=290)
    entry_hh_mm.place(x=250, y=290)
    label_departure.place(x=200, y=320)
    entry_mm_dd_yyyy2.place(x=30, y=350)
    entry_hh_mm2.place(x=250, y=350)
    label_number_adults.place(x=30, y=380)
    entry_no_adults.place(x=200, y=380)
    label_number_kids.place(x=320, y=380)
    entry_no_kids.place(x=468, y=380)
    label_room_no.place(x=30, y=410)
    entry_room_no.place(x=180, y=413)
    button_reserve.place(x=280, y=412)
    button_unreserve.place(x=400, y=412)
    button_done.place(x=260, y=467)

    # button_done.place(x=270, y=340)
    #textbinder
    entry_first_name.insert(0, "First Name*")
    entry_first_name.bind("<FocusIn>", lambda e:entry_first_name.delete(0, "end"))
    entry_middle_name.insert(0, "Middle Name*")
    entry_middle_name.bind("<FocusIn>", lambda e:entry_middle_name.delete(0, "end"))
    entry_last_name.insert(0, "Last Name*")
    entry_last_name.bind("<FocusIn>", lambda e:entry_last_name.delete(0, "end"))
    entry_address.insert(0, "Street Address*")
    entry_address.bind("<FocusIn>", lambda e:entry_address.delete(0, "end"))
    # entry_address2.insert(0, "Street Address Line 2:")
    # entry_address2.bind("<FocusIn>", lambda e:entry_address2.delete(0, "end"))
    entry_city.insert(0, "City*")
    entry_city.bind("<FocusIn>", lambda e:entry_city.delete(0, "end"))
    entry_state.insert(0, "State/Province*")
    entry_state.bind("<FocusIn>", lambda e:entry_state.delete(0, "end"))
    entry_country_code.insert(0, "Country code*")
    entry_country_code.bind("<FocusIn>", lambda e:entry_country_code.delete(0, "end"))
    entry_phone_no.insert(0, "Phone No: -123-4567-890*")
    entry_phone_no.bind("<FocusIn>", lambda e:entry_phone_no.delete(0, "end"))
    entry_email.insert(0, "Email: e.g: myemail@gmail.com*")
    entry_email.bind("<FocusIn>", lambda e:entry_email.delete(0, "end"))
    entry_mm_dd_yyyy.insert(0, "MM-DD-YYYY*")
    entry_mm_dd_yyyy.bind("<FocusIn>", lambda e: entry_mm_dd_yyyy.delete(0, "end"))
    entry_hh_mm.insert(0, "HH:MM*")
    entry_hh_mm.bind("<FocusIn>", lambda e: entry_hh_mm.delete(0, "end"))
    entry_mm_dd_yyyy2.insert(0, "MM-DD-YYYY*")
    entry_mm_dd_yyyy2.bind("<FocusIn>", lambda e: entry_mm_dd_yyyy2.delete(0, "end"))
    entry_hh_mm2.insert(0, "HH:MM*")
    entry_hh_mm2.bind("<FocusIn>", lambda e: entry_hh_mm2.delete(0, "end"))
    entry_no_adults.insert(0, "Digits only*")
    entry_no_adults.bind("<FocusIn>", lambda e: entry_no_adults.delete(0, "end"))
    entry_no_kids.insert(0, "Digits only*")
    entry_no_kids.bind("<FocusIn>", lambda e: entry_no_kids.delete(0, "end"))


#rseseve f(x)
#frames
frame1 = Frame(height=170, width=900, bg="#123456")
frame2 = Frame(height=400, width=600, bg="#123456", highlightbackground="#737ca1", highlightthickness=4)
frame3 = Frame(height=550, width=300, bg="#123456", highlightbackground="#737ca1", highlightthickness=4)
#frames on frames
framehotelstatus = Frame(frame1, height=140, width=200, bg="#123456")
framerooms = Frame(frame1, height=140, width=250, bg="#875439")
framepaymentsinfo = Frame(frame1, height=140, width=250, bg="#643822")
frameexit = Frame(frame1, height=140, width=200, bg="#843022")
#hotel rooms
img_reserve_room = (Image.open("reserve_room_photo.jpg"))
i2 = img_reserve_room.resize((250, 150))
reserver = ImageTk.PhotoImage(i2)
ii2 = Label(framerooms, height=140, width=250, bg="black", image=reserver, compound=RIGHT)
ii2.place(x=0, y=0)

#hotel
img_hotel = (Image.open("Hotel.png"))
i1 = img_hotel.resize((250, 150))
hotel = ImageTk.PhotoImage(i1)
ii1 = Label(framehotelstatus, height=140, width=240, bg="#384765", image=hotel, compound=RIGHT)
ii1.place(x=0, y=0)
#hotel payment
img_payment = (Image.open("payment.png"))
i3 = img_payment.resize((255, 150))
payment = ImageTk.PhotoImage(i3)
ii3 = Label(framepaymentsinfo, height=140, width=250, bg="red", image=payment, compound=RIGHT)
ii3.place(x=0, y=0)

#hotel exit
img_exit = (Image.open("exit.jpg"))
i4 = img_exit.resize((245, 150))
exitt = ImageTk.PhotoImage(i4)
ii4 = Label(frameexit, height=140, width=240, bg="#384765", image=exitt, compound=RIGHT)
ii4.place(x=0, y=0)

personal_information()
#fx filter
def get_room_choice():
    bed = entry_bed.get()
    ac = entry_ac.get()
    tv = entry_tv.get()
    wifi = entry_wifi.get()
    if bed == "" or ac == "" or  tv== "" or wifi == "":
        mb.showerror('Error', 'Please input something using the key')
        textbox_filter.delete(1.0, END)
        textbox_filter.insert(INSERT, word)
    else:
        msg = "Room number: "
        textbox_filter.delete(1.0, END)
        filter = project_hotel_db2.book_room(bed, ac, tv, wifi)
        for i in filter:
            textbox_filter.insert(INSERT,f" {msg}{(i[1])}, Price: {i[6]}")


#entry
entry_bed = Entry(frame3, font=('Times New Roman', 12), width=10, bg="white")
entry_ac = Entry(frame3, font=('Times New Roman', 12), width=10, bg="white")
entry_tv = Entry(frame3, font=('Times New Roman', 12), width=10, bg="white")
entry_wifi = Entry(frame3, font=('Times New Roman', 12), width=10, bg="white")


#label
label_time = Label(framehotelstatus, font=('Calibri', 13, 'bold'), bg='#111B37', fg="WHITE", width=21)
label_filter = Label(frame3, text="Filter", font=('Calibri', 23, 'bold'), bg='#123456', fg="Black")
label_bed = Label(frame3, text="Bed(s):", font=('Aerial', 15), bg="#123456",
                  fg="black")
label_ac = Label(frame3, text="AC:", font=('Aerial', 15), bg="#123456",
                 fg="black")
label_tv = Label(frame3, text="TV:", font=('Aerial', 15), bg="#123456",
                 fg="black")
label_wifi = Label(frame3, text="Wifi:", font=('Aerial', 15), bg="#123456",
                   fg="black")

def combobox():

    # fx

    # combobox
    # beds
    beds = StringVar()
    cc = ttk.Combobox(frame3, textvariable=beds, width=20, state="readonly")
    cc['values'] = ("Please select...", '1',
                    "2",
                    "3",
                    "4",
                    "more than 4")
    cc.place(x=90, y=70)
    cc.current(0)
    # ac
    ac = StringVar()
    cc = ttk.Combobox(frame3, width=20, textvariable=ac, state="readonly")
    cc['values'] = ("Please select...", 'Yes',
                    "No",)
    cc.place(x=90, y=103)
    cc.current(0)
    #
    tv = StringVar()

    cc = ttk.Combobox(frame3, width=20, textvariable=tv, state="readonly")
    cc['values'] = ("Please select...", 'Yes',
                    "No",)
    cc.place(x=90, y=133)
    cc.current(0)

    wifi = StringVar()
    cc = ttk.Combobox(frame3, width=20, textvariable=wifi, state="readonly")
    cc['values'] = ("Please select...", 'Yes',
                    "No",)
    cc.place(x=90, y=163)
    cc.current(0)
    # def get_choice(*arg):textbox_filter.delete(1.0, END)
    b = str(beds.get())
    a = str(ac.get())
    t = str(tv.get())
    w = str(wifi.get())
    beds.trace('w', b)
    ac.trace('w', a)
    tv.trace('w', t)
    wifi.trace('w', w)
    print(b, a, t, w)
#finding rooms filter

#buttton
button_personal_info = Button(frame1, text="Personal Information",
                              font=('Aerial', 10, 'bold'), bg="#123456",
                              width=23, activebackground="#123456", bd=7,
                               command=personal_information, state='disabled')
buttonreserve = Button(frame1, text="Reserve Room",
                       bg="#123456", font=('Aerial', 10, 'bold'),
                       width=28, activebackground="#123456", bd=7, state='disabled')
buttonAdmin = Button(frame1, text="Admin ",
                    font=('Aerial', 10, 'bold'), bg="#123456",
                    width=29, activebackground="#123456", bd=7, command=Admin)
buttonexit = Button(frame1, text="Exit", font=('Aerial', 10, 'bold'),
                    bg="#123456", width=22, activebackground="#123456",
                    bd=7, command=Exit)
button_find_rooms = Button(frame3, text="Find Rooms", font=('Aerial', 10, 'bold'), bg="#123456",
                           activebackground="#123456", bd=3, command=get_room_choice, width=9)
time()
#textbox
textbox_filter = Text(frame3, height=8, width=32, font=('Times new roman', 12), bg="#bcc6cc",
                      fg="#127498")
word = "Key: Beds;1/2/3/4\n" \
       "         Ac;yes/no\n         Tv;yes/no\n         Wifi;yes/no\n"


textbox_filter.insert(END, word)
#placings
frame1.propagate()
frame2.propagate()
frame3.propagate()
framehotelstatus.propagate()
framerooms.propagate()
framepaymentsinfo.propagate()
frameexit.propagate()

frame1.place(x=100, y=0)
frame2.place(x=100, y=170)
frame3.place(x=700, y=170)
framehotelstatus.place(x=1, y=1)
framerooms.place(x=201, y=1)
framepaymentsinfo.place(x=451, y=1)
frameexit.place(x=701, y=1)
button_personal_info.place(x=0, y=143)
buttonreserve.place(x=205, y=143)
buttonAdmin.place(x=451, y=143)
buttonexit.place(x=705, y=143)
label_time.place(x=2, y=2)
label_filter.place(x=100, y=10)
label_bed.place(x=4,y=67)
label_ac.place(x=4, y=100)
label_tv.place(x=4, y=130)
label_wifi.place(x=4, y=160)
button_find_rooms.place(x=80, y=193)
textbox_filter.place(x=15, y=230)
entry_bed.place(x=80, y=69)
entry_ac.place(x=80, y=102)
entry_tv.place(x=80, y=132)
entry_wifi.place(x=80, y=162)

window.mainloop()