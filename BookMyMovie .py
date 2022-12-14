import time
import mysql.connector as conn

def BookMyMovie():
    print('\n______  BookMyMovie ______\n ')
    location()
def location():    
    time.sleep(0.7)
    print('Where You want to watch movie? :\n 1.Pune\n 2.Mumbai\n 3.Chennai')
    global city_name
    city = int(input('Choose your option:'))
    
    if city ==1:
        city_name = 'Pune'
        print(f'Your Location : {city_name}')
        movie()
    elif city == 2: 
        city_name = 'Mumbai'
        print(f'Your Location : {city_name}')
        movie()
    elif city == 3:
        city_name = 'Chennai'
        print(f'Your Location : {city_name}')
        movie()
    else:
        print('!!  -- Enter correct City !!')
        location() 
    

def movie():
    print('which movie do you want to watch ?\n\t1.Vikram Vedha\n\t2.Black Panther\n\t3.Spiderman\n\t4.back')
    mov = int(input('Choose your option:'))
    global movie_name
    if mov ==1:
        movie_name = 'Vikram Vedha'
        print(f'Select Screen for: {movie_name}')
        screen()
    elif mov == 2: 
        movie_name = 'Black Panther'
        print(f'Select Screen for: {movie_name}')
        screen()
    elif mov == 3:
        movie_name = 'Spiderman'
        print(f'Select Screen for: {movie_name}')
        screen()
    elif mov == 4:
        location()
    else:
        print('!!  -- Enter correct Movie !!')
        movie()
    
     

def screen():
    print('Which Screen do you want to watch ?\n\t1.English IMAX 3D\n\t2.Hindi 3D\n\t3.Hindi 2D')
    sc = int(input('Choose your option:'))  
    global screen_type
    if sc == 1 :
        screen_type = 'English IMAX 3D'
        theatre()
    elif sc == 2 :
        screen_type = 'Hindi 3D'
        theatre()
    elif sc == 3:
        screen_type = 'Hindi 2D'        
        theatre()
    else:
        print('!!  -- Enter correct Screen !!')
        screen()

def theatre():
    print(f'which theatre do you wish to see {movie_name}?\n\t1.INOX\n\t2.Cinepolis City Mall\n\t3.PVR \n\t4.back')
    global theatre_code, theatre_name
    theatre_code = int(input('Choose your option:'))
    if theatre_code ==1:
        theatre_name = 'INOX'
        print(f'Select Timing in {theatre_name} theatre')
        timing()
    elif theatre_code == 2: 
        theatre_name = 'Cinepolis City Mall'
        print(f'Select Timing in {theatre_name} theatre')
        timing()
    elif theatre_code == 3:
        theatre_name = 'PVR'
        print(f'Select Timing in {theatre_name} theatre')
        timing()
    elif theatre_code == 4:
        screen()
    else:
        print('!!  -- Enter correct Theatre Name !!')
        theatre()


def timing():
    # Time Slots are depend Upon Theatre(theatre codes)
    global time_slots
    time_slots = {  1:  ['11:00-1:30', '1:45-4:15','4:30-7:00','7:30-10:00'], # INOX
                    2: ['10:00-12:30','12:45-3:15',' 3:30-6:00','6:30-9:00'], # Cinepolis City Mall
                    3:  ['12:00-2:30', '2:45-5:15','5:30-7:00','7:30-10:30']  # PVR
                    }

    for i, k in enumerate(time_slots[theatre_code]):
            print(f'{i+1}. {k}')
    global sloted_time
    sloted_time = int(input('Select Your Time :'))
    print(f'Selected time :{time_slots[theatre_code][sloted_time-1]}')
    global total_tickets 
    total_tickets= int(input('How many seats?'))

    print(f'''````````````````  TICKET DETAILS ````````\n 
            Location: {theatre_name}, {city_name}\n\tMovie: {movie_name} \t\t  [ {screen_type}] Show \n
            Total seats:{total_tickets}\n ENJOY YOUR SHOW AT {time_slots[theatre_code][sloted_time-1]}''')
    
    
def mysql_update():
    mydb = conn.connect(host = 'localhost',user = 'root' ,passwd = "8899" )
    cursor = mydb.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS bookmymovie ;")
    cursor.execute('use bookmymovie;')
    create_T = '''CREATE TABLE IF NOT EXISTS bookings (
    booking_id int primary key AUTO_INCREMENT,
    location varchar(20),
    movie varchar(40),
    screen varchar(30),
    theatre varchar(30),
    timing varchar(10),
    seats TINYINT
    );'''
    cursor.execute(create_T)
    # Inserting data into table
    values = f'''insert into bookings values(NULL,"{city_name}", "{movie_name}", "{screen_type}","{theatre_name}", "{time_slots[theatre_code][sloted_time-1]}", {total_tickets})'''
    cursor.execute(values)
    mydb.commit()
    print('SQL Updated')



BookMyMovie()
mysql_update()