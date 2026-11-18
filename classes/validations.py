
from classes.data_manager import DataManager
import datetime

from classes.room import Room


class Validations:
    def is_str(self, word):
        if not word.strip():
            return False
        return True


    def next_booking_id(self):
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

    def is_room_id_exist(self, room_id):
        exist = False
        rooms = DataManager()
        loads = rooms.load_rooms()
        if not loads:
            return False
        for room in loads:
            if room["room_id"] == room_id:
                return True
        return False

    def is_booking_id_exist(self, booking_id):
        exist = False
        bookings = DataManager()
        loads = bookings.load_bookings()
        if not loads:
            return False
        for order in loads:
            if order["booking_id"] == booking_id:
                return True
        return False

    def check_booking_date(self, booking_date):
        today = datetime.date.today()
        if today > booking_date:
            return False
        return True

    def check_start_time(self, date_and_time, rooms, bookings_list, room_id, exclude_booking_id=None):
        duration = 0
        now = datetime.datetime.now()
        if date_and_time < now:
            return False
        if date_and_time.time() < datetime.time(10, 0) or date_and_time.time() > datetime.time(22,0):
            return False
        for one_room in rooms:
            if room_id == one_room.room_id:
                duration = one_room.duration
        for order in bookings_list:
            if room_id == order.room_id:
                if exclude_booking_id is not None and order.booking_id == exclude_booking_id:
                    continue
                booking_date = datetime.date.strptime(order.booking_date, "%Y-%m-%d")
                booking_time = datetime.time.strptime(order.start_time, "%H:%M")
                if booking_date == date_and_time.date():
                    duration += 15
                    current_start_time = date_and_time
                    current_room_duration = datetime.timedelta(minutes=duration)
                    current_room_finish = current_start_time + current_room_duration
                    other_room_start = datetime.datetime.combine(booking_date, booking_time)
                    other_room_finish = other_room_start + current_room_duration
                    if current_room_finish > other_room_start and current_start_time < other_room_finish:
                        return False
        return True

    def check_players(self, number, room_id, rooms):
        for room in rooms:
            if room.room_id == room_id:
                if number > room.max_players or number < room.min_players:
                    return False
        return True

    def find_room_by_id(self, room_id):
        all_jsons = DataManager()
        all_rooms = all_jsons.load_rooms()
        for room in all_rooms:
            if room["room_id"] == room_id:
                return room
        return None










