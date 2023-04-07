class RoomNotFoundException(Exception):
    """
    RoomNotFoundException raised when there is no room found in castle with given ID.
    """
    def __init__(self, *args: object) -> None:
        super().__init__(*args)