from classes.data_manager import DataManager
import datetime

def is_str(word):
    if not word.strip():
        return False
    return True


def next_booking_id():
    data = DataManager()
    loads = data.load_bookings()
    if not loads:
        return "R001"
    last_one = loads[-1]
    last_digits = last_one["booking_id"][3:]
    last_digits = int(last_digits)
    next_digit = last_digits + 1
    if next_digit < 10:
        return "B00" + str(next_digit)
    elif 10 < next_digit < 100:
        return "B0" + str(next_digit)
    else:
        return "B" + str(next_digit)

def is_room_id_exist(room_id):
    exist = False
    rooms = DataManager()
    loads = rooms.load_rooms()
    if not loads:
        return "Can't create order there's no rooms exist!!!"
    for room in loads:
        if room["room_id"] == room_id:
            exist = True
    if exist:
        return True
    return False

def check_booking_date(booking_date):
    today = datetime.date.today()
    if today < booking_date:
        return False
    return True

def check_start_time(date_and_time, rooms, bookings_list, room_id):
    duration = 0
    now = datetime.datetime.now()
    if date_and_time < now:
        return False
    for one_room in rooms:
        if room_id == one_room.room_id:
            duration = one_room.duration
    for order in bookings_list:
        if room_id == order.room_id:
                if order.booking_date == date_and_time.date():
                    duration += 15
                    current_start_time = date_and_time
                    current_room_duration = datetime.timedelta(minutes=duration)
                    current_room_finish = current_start_time + current_room_duration
                    other_start_time = datetime.datetime.combine(order.booking_date, order.start_time)
                    







