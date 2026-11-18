import json
from pathlib import *
from classes.room import Room
from classes.booking import Booking
rooms_path = Path(__file__).parent.parent /"jsons"/"rooms.json"
booking_path = Path(__file__).parent.parent /"jsons"/"bookings.json"

book = Booking
room = Room
class DataManager:
    def load_rooms(self):
        with open(rooms_path, "r") as file:
            loads = json.load(file)
        return loads


    def load_bookings(self):
        with open(booking_path, "r") as file:
            loads = json.load(file)
        return loads


    def save_rooms(self, room_objects):
        new_json = []
        for room in room_objects:
            room = room.to_dict()
            new_json.append(room)
        with open(rooms_path, "w") as file:
            json.dump(new_json, file, indent=2)
        return "File updated new json"

    def save_bookings(self, booking_objects):
        new_json = []
        for order in booking_objects:
            order = order.to_dict()
            new_json.append(order)
        with open(booking_path, "w") as file:
            json.dump(new_json, file, indent=2)
        return "File updated new json"



