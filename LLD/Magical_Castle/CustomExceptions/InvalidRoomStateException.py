class InvalidRoomStateException(Exception):
    """
    InvalidRoomStateException raised when room is not in below states
        1. Empty
        2. Containing Diamonds
        3. Containing Portal
        4. Containing Wormhole
    """
    pass