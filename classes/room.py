
class Room:
    def __init__(self, room_id, name, difficulty, duration, min_players, max_players, price_per_player, is_active):
        self.room_id = room_id
        self.name = name
        self.difficulty = difficulty
        self.duration = duration
        self.min_players = min_players
        self.max_players = max_players
        self.price_per_player = price_per_player
        self.is_active = is_active


    def activate(self):
        self.is_active = "Active"
    def deactivate(self):
        self.is_active = "Cancelled"
    def is_valid_player(self, players):
        if players > self.max_players:
            return False
        elif players < self.min_players:
            return False
        return True
    def to_dict(self):
        room = {}
        room["room_id"] = self.room_id
        room["name"] = self.name
        room["difficulty"] = self.difficulty
        room["duration"] = self.duration
        room["min_players"] = self.min_players
        room["max_players"] = self.max_players
        room["price_per_player"] = self.price_per_player
        room["is_active"] = self.is_active
        return room

    @classmethod
    def from_dict(cls, data):
        return cls(data["room_id"], data["name"], data["difficulty"], data["duration"], data["min_players"], data["max_players"], data["price_per_player"], data["is_active"])




