from sources import Room
from CustomExceptions import RoomAlreadyExistsException, RoomNotFoundException, IdOutOfRangeException
import random

class Castle:
    """
     Object of this class represent whole castle.
    """
    def __init__(self) -> None:
        """
        creates and returns a Castle object.
        """

        self.rooms = {}
        self.total_rooms = 0
        self.entrance_id = 0
        self.exit_id = 0

    def get_total_rooms(self):
        return self.total_rooms
    def set_total_rooms(self, num):
        self.total_rooms = num

    def isValidID(self, ID):
        """
        Validates if ID is valid otherwise throws exception.
        """
        if not (1 <= ID <= self.get_total_rooms()):
            raise IdOutOfRangeException

        return True

    def add_room(self, room: Room):
        """
        Adds new room to castle.
        """
        if self.rooms.get(room.get_id(), None):
            raise RoomAlreadyExistsException

        self.rooms[room.get_id()] = room

    def get_room(self, ID):
        ID = str(ID)
        if not self.rooms.get(ID, None):
            raise RoomNotFoundException

        return self.rooms.get(ID)

    def change_room(self, ID, new_room):
        if self.isValidID(ID):
            self.rooms[ID] = new_room

    def get_entrance_id(self):
        return self.entrance_id
    def set_entrance_id(self, ID):
        if self.isValidID(int(ID)):
            self.entrance_id = ID

    def get_exit_id(self):
        return self.exit_id
    def set_exit_id(self, ID):
        if self.isValidID(int(ID)):
            self.exit_id = ID

    def get_next_room(self, room_id, door):
        """
        Based on possibility of next rooms sends nest room to user to be moved.
        """
        room = self.get_room(room_id)
        # next_room_id = 0
        if door == "north":
            next_room_id = room.north
        elif door == "south":
            next_room_id = room.south
        elif door == "east":
            next_room_id = room.east
        elif door == "west":
            next_room_id = room.west
        elif door == "exit":
            return None

        next_room = self.get_room(next_room_id)
        if next_room.get_portal():
            return self.get_room(self.get_entrance_id())
        elif next_room.get_wormhole():
            while next_room.get_wormhole():
                next_random_room_id = random.randint(1,self.get_total_rooms())
                next_room = self.get_room(next_random_room_id)

        return next_room

    def next_possible_directions(self, room_id):
        """
        Shows next possible directions where player can move, except from blocked doors.
        """
        possible_directions = []

        if room_id == self.get_exit_id():
            possible_directions.append("exit")
        room = self.get_room(room_id)

        if room.north:
            possible_directions.append("north : {}".format(room.north))
        if room.south:
            possible_directions.append("south : {}".format(room.south))
        if room.east:
            possible_directions.append("east : {}".format(room.east))
        if room.west:
            possible_directions.append("west : {}".format(room.west))

        self.print_next_direction(possible_directions)
        
    def print_next_direction(self, possible_directions):
        index = 1
        for direction in possible_directions:
            print(index," ", direction)
