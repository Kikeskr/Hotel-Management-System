import sqlite3
conn = sqlite3.connect('Hotel_demo_info.db')
c = conn.cursor()

def create_Table():
    c.execute('''CREATE TABLE IF NOT EXISTS hotel_demo_info(
    reg_no INTEGER PRIMARY KEY, first_name TEXT,
     middle_name TEXT, last_name TEXT, street_address TEXT, city TEXT,
      state TEXT, country_code TEXT, phone_number TEXT,
       email TEXT, date_1_mm_dd_yy TEXT, time_1_hh_mm TEXT, 
    date_2_mm_dd_yy TEXT, time_2_hh_mm TEXT,
     no_of_adults INTEGER, no_of_kids INTEGER, 
     room_number INTEGER)''')
    return "Table succesfully created"
def personal_details(reg_no, first_name, middle_name, last_name, street_address, city,
                     state, country_code,phone_number, email
                     , date_1_mm_dd_yy, time_1_hh_mm, date_2_mm_dd_yy, time_2_hh_mm,
                     no_of_adults, no_of_kids, room_number
                     ):
    c.execute(f'''INSERT INTO hotel_demo_info VALUES(
    {reg_no}, '{first_name}', '{middle_name}', '{last_name}', '{street_address}', '{city}',
     '{state}', '{country_code}', '{phone_number}', '{email}'
      , '{date_1_mm_dd_yy}', '{time_1_hh_mm}', '{date_2_mm_dd_yy}',
     '{time_2_hh_mm}', {no_of_adults}, {no_of_kids}, {room_number})''')
    conn.commit()
    return "Data succesfully added into the database"
# print(personal_details(1, 'Kenneth', 'Ogbonna', 'Ikechukwu', 'New GRA', 'Makurdi', 'Benue', '+234', '8133746085',
#                        'parablez69@gmail.com', '04-23-2023', '12:00pm', '04-26-2023', '07:00am', '1', '0', '1'))
def view_guest_details():
    c.execute("SELECT * FROM hotel_demo_info")
    return c.fetchall()

def get_reg_no():
    c.execute("SELECT reg_no FROM hotel_demo_info ORDER BY reg_no DESC" )
    result = c.fetchone()
    if len(result)==0:
        return 1
    else:
        return result[0]+1
def dd(id):
    c.execute(f"DELETE FROM hotel_demo_info WHERE reg_no ={id}")
    conn.commit()
    return f"Data with ID {id} has been deleted"
# print(view_guest_details())

