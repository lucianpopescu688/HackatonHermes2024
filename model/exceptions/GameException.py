class GameException(Exception):
    """
    A custom exception class for game-related errors.
    """
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"GameException: {self.message}"
