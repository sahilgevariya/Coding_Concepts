from sources import Diamond, Room, Castle, Player
from CustomExceptions import InvalidRoomStateException

class Game:
    """
    Object of this class represent whole Magical castle game.
    """

    def __init__(self) -> None:
        """
        creates and returns a Game object.
        """

        self.castle = Castle.Castle()
        self.players = []
        self.finished = None
        self.turn = 0
        self.endpoints = {}

    def initialize_from_file(self, filename):
        """
        Reads castle map file and creates whole castle from it.
        """
        total_rooms = 0

        with open(filename) as file_obj:
            total_rooms = int(file_obj.readline())
            self.castle.set_total_rooms(total_rooms)

            entrance,entrance_data = file_obj.readline().split(":")
            exit,exit_data = file_obj.readline().split(":")

            self.endpoints[entrance] = list(map(str.strip, entrance_data.split(",")))
            self.endpoints[exit] = list(map(str.strip, exit_data.split(",")))

            self.castle.set_entrance_id(self.endpoints[entrance][0])
            self.castle.set_exit_id(self.endpoints[exit][0])

            # setting initial/start room for all the players 
            for player in self.players:
                player.set_init_room(self.endpoints[entrance][0])

            for room_data in file_obj.readlines():
                room_id, room_meta_data = room_data.split(":")

                north, south, east, west, magic_word = map(str.strip, room_meta_data.split(","))
                
                have_portal, have_wormhole, no_of_diamonds = False, False, 0
                
                if magic_word == "P":
                    have_portal = True
                elif magic_word == "W":
                    have_wormhole = True
                elif magic_word.count("D") == len(magic_word):
                    no_of_diamonds = len(magic_word)
                elif magic_word != "":
                    raise InvalidRoomStateException()

                diamond = Diamond.Diamond()
                diamond.set_diamonds(no_of_diamonds)

                if north in ["E","X"]:
                    north = self.endpoints[north][0]
                if south in ["E","X"]:
                    south = self.endpoints[south][0]
                if east in ["E","X"]:
                    east = self.endpoints[east][0]
                if west in ["E","X"]:
                    west = self.endpoints[west][0]

                room = self.build_room(room_id, north, south, east, west, diamond, have_portal, have_wormhole)

                self.castle.add_room(room)
        # for _,room in self.castle.rooms.items():
        #     print(room)

    def get_turn(self):
        return self.turn
    def set_turn(self, turn):
        self.turn = turn

    def get_player(self):
        return self.players[self.get_turn()]
    def add_player(self, player: Player):
        self.players.append(player)
    def get_players(self):
        return self.players

    def build_room(self, room_id, north, south, east, west, diamond, portal, wormhole):
        room = Room.Room(room_id, north, south, east, west, portal, wormhole, diamond)
        return room

    def move(self):
        current_player = self.get_player()
        self.update_diamonds()

        next_turn = ((self.get_turn() + 1) % len(self.players))
        self.set_turn(next_turn)

        if current_player.is_completed() == False:
            # shows which player's turn to get input
            print(current_player)
            current_room_id = current_player.get_position()

            self.castle.next_possible_directions(current_room_id)
            next_direction = input().strip()

            if next_direction == "exit" or (current_room_id, next_direction) == tuple(self.endpoints["X"]):
                current_player.is_finished = True
                return

            next_room = self.castle.get_next_room(current_room_id, next_direction)
            current_player.add_to_path(current_room_id, next_direction)
            current_player.move(next_room.get_id())

    def is_finished(self):
        for player in self.players:
            if not player.is_completed():
                return False

        return True

    def update_diamonds(self):
        """
        Updates diamonds of current player with newly collected diamonds.
        """
        current_player = self.get_player()
        current_room_id = str(current_player.get_position())
        current_room = self.castle.get_room(current_room_id)

        diamond = current_room.get_diamond()
        current_player.set_diamonds(diamond.get_diamonds())
        diamond.set_diamonds(0)


