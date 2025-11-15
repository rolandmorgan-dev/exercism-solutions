"""Functions to automate Conda airlines ticketing system."""

seats = ("A", "B", "C", "D")

def generate_seat_letters(number: int) -> str:
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    for seats_num in range(number):
        yield seats[seats_num % 4]

def generate_seats(number: int) -> str:
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    num = 1
    for index, seat in enumerate((generate_seat_letters(number))):
        if num == 13:
            num += 1
        yield f"{num}{seat}"
        if (index+1) % 4 == 0:
            num += 1

def assign_seats(passengers: list[str]) -> dict[str, str]:
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    assigned_seats = dict()
    count = 0
    for passenger_seat in generate_seats(len(passengers)):
        assigned_seats[passengers[count]] = passenger_seat
        count += 1
    return assigned_seats

def generate_codes(seat_numbers: list[str], flight_id: str) -> str:
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    for seat in seat_numbers:
        yield str(seat+flight_id).ljust(12, "0")
