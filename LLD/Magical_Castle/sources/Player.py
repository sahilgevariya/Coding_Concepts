from CustomExceptions import IdOutOfRangeException

class Player:
    """
     Object of this class represent a Player.
    """

    def __init__(self, player_id) -> None:
        """
        creates and returns a Player object.
        """

        self.player_id = player_id
        self.init_room_id = 0
        self.position = 0
        self.collected_diamonds = 0
        self.path = []
        self.next_options = []
        self.is_finished = False

    def set_init_room(self, room_id):
        self.init_room_id = room_id
        self.position = room_id

    def get_position(self):
        return self.position

    def set_position(self, ID):
        if not (1 <= int(ID) <= 25):
            raise IdOutOfRangeException

        self.position = ID

    def get_diamonds(self):
        return self.collected_diamonds
    def set_diamonds(self, count):
        self.collected_diamonds += count

    def is_completed(self):
        """
        Checks if Player completed the game and returns boolean value.
        """
        return self.is_finished

    def print_path(self):
        """
        Prints a whole path User has taken while playing game.
        """
        for room_id, door_direction in self.path:
            print(room_id,"->",door_direction, end = ",")

    def add_to_path(self, room_id, door_id):
        """
        Adds a takes steps to current path.
        """

        self.path.append((room_id, door_id))

    def move(self, room_id):
        """
        Moves player to next room.
        """

        self.set_position(room_id)

    def __str__(self) -> str:
        return "[Turn] Player {} | Diamond count : {} | Current room : {}".format(self.player_id, self.collected_diamonds, self.get_position())