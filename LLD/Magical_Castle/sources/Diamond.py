from CustomExceptions import NegativeDiamondsException

class Diamond:
    """
     Object of this class represent Diamond in room.
    """
    def __init__(self) -> None:
        """
        creates and returns a Diamond object.
        """

        self.no_of_diamonds = 1

    def set_diamonds(self, diamonds):
        if diamonds < 0:
            raise NegativeDiamondsException
        else:
            self.no_of_diamonds = diamonds

    def get_diamonds(self):
        return self.no_of_diamonds

    def __str__(self) -> str:
        return "Number of Diamonds : {}".format(self.no_of_diamonds)
    
