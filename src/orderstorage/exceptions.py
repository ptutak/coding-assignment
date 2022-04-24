class OrderNotFoundException(Exception):
    """Raised in case order is not found."""


class OrderAlreadyPresentException(Exception):
    """Raised in case order is already present."""
