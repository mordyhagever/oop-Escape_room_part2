import json
from pathlib import *
from classes.room import Room
from classes.booking import Booking
rooms_path = Path(__file__).parent.parent /"jsons"/"rooms.json"
booking_path = Path(__file__).parent.parent /"jsons"/"bookings.json"

class DataManager:
    def load_rooms(self):
        with open(rooms_path, "r") as file:
            loads = json.load(file)
        return loads


    def load_bookings(self):
        with open(booking_path, "r") as file:
            loads = json.load(file)
        return loads

    def save_rooms(self, room_object):
        rooms = Room.to_dict(room_object)
        with open(rooms_path, "w") as file:
            json.dump(rooms, file, indent=2)
        return "File updated new json"

    def save_bookings(self, booking_object):
        new_json = Booking.to_dict(booking_object)
        with open(booking_path, "w") as file:
            json.dump(new_json, file, indent=2)
        return "File updated new json"
    


