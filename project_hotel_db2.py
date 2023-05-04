import sqlite3
conn = sqlite3.connect('Hotel_data2.db')
c = conn.cursor()

def createTable():
    c.execute('''CREATE TABLE IF NOT EXISTS hotel_details2(
    serial INTEGER PRIMARY KEY, room_number TEXT, number_of_beds INTEGER,
     ac TEXT, tv TEXT,
     wifi TEXT, price TEXT, check_in INTEGER)''')
    conn.commit()
    return "Hotel database2 successfully created"
def hotel_details(serial, room_number, number_of_beds, ac, tv, wifi, price, check_in):
    c.execute(f'''INSERT INTO hotel_details2 VALUES(
      {serial}, {room_number}, {number_of_beds}, '{ac}',  '{tv}', '{wifi}', '{price}', {check_in} )''')
    conn.commit()
    return "Hotel database2 successfully added"
def view_hotel_details():
    c.execute("SELECT * FROM hotel_details2")
    return c.fetchall()
def kirib(room_number):#, check_in):
    c.execute(f"SELECT * FROM hotel_details2 WHERE room_number={room_number} ")#and check_in={check_in}")
    return c.fetchone()
def riob(room_number, check_in):
    c.execute(f"UPDATE hotel_details2 SET "
              f" check_in={check_in} WHERE room_number={room_number}")
    conn.commit()
    return f"{room_number} updated successfully"
def book_room(number_of_beds, ac, tv, wifi):
    c.execute(f"SELECT * FROM hotel_details2 WHERE number_of_beds={number_of_beds} and ac='{ac}' and tv='{tv}' and wifi='{wifi}'")
    return c.fetchall()
def cbr(none):
    c.execute(f"SELECT * FROM hotel_details2 WHERE check_in ={none}")
    return c.fetchall()
def view_self(serial):
    c.execute(f"SELECT * FROM hotel_details2 WHERE serial ={serial}")
    return c.fetchone()
def Update_hotel_details(room_number, number_of_beds, ac, tv, wifi, price):
    c.execute(f"UPDATE hotel_details2 SET number_of_beds={number_of_beds},ac='{ac}',tv='{tv}', wifi='{wifi}', price='{price}' WHERE room_number={room_number}")
    conn.commit()

def Update_hotel(serial, room_number, number_of_beds, ac, tv, wifi, price, check_in):
    c.execute(
        f"UPDATE hotel_details2 SET room_number={room_number},number_of_beds={number_of_beds},ac='{ac}',tv='{tv}', wifi='{wifi}',"
        f" price='{price}', check_in={check_in} WHERE serial={serial}")
    conn.commit()
#print(riob('002', 0))
#print(kirib('2'))
#serial, room_number, number_of_beds, ac, tv, wifi, price, check_in
# print(Update_hotel(5, 5, 5, 'yes', 'yes', 'yes', '$80 per 24hours', 0))
#
# print(hotel_details(16, 16, 1, 'no', 'yes', 'yes', '$30 per 24hours', 0))
# print(hotel_details(17, 17, 1, 'yes', 'yes', 'yes', '$450 per 24hours', 0))
# print(hotel_details(18, 18, 1, 'yes', 'yes', 'yes', '$50 per 24hours', 0))
# print(hotel_details(19, 19, 2, 'yes', 'yes', 'yes', '$50 per 24hours', 0))
# print(hotel_details(20, 20, 2, 'no', 'yes', 'yes', '$40 per 24hours', 0))

# print(view_hotel_details())