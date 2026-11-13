
def parse_ticket_id(ticket_id):
    """
    Parse a ticket ID in the format PREFIX-YEAR-SERIAL.
    Return a safe default for invalid input.
    """
    if not isinstance(ticket_id, str):
        return ("", 0, 0)

    parts = ticket_id.strip().split("-")

    if len(parts) != 3:
        return ("", 0, 0)

    prefix, year, serial = parts

    if not prefix or not year.isdigit() or not serial.isdigit():
        return ("", 0, 0)

    return prefix.upper(), int(year), int(serial)


def total_fines(amounts_csv):
    """
    Calculate total fines, with a maximum of 10000.
    Return 0 for invalid input.
    """
    if not isinstance(amounts_csv, str) or not amounts_csv.strip():
        return 0

    try:
        amounts = [int(a.strip()) for a in amounts_csv.split(",")]

        if any(amount < 0 for amount in amounts):
            return 0

        total = sum(amounts)

        return min(total, 10000)

    except (ValueError, TypeError):
        return 0


def speed_excess(reading):
    """
    Calculate percentage speed excess.
    Return 0 for invalid input or a zero speed limit.
    """
    if not isinstance(reading, str):
        return 0

    parts = reading.strip().split("/")

    if len(parts) != 2:
        return 0

    try:
        speed = int(parts[0].strip())
        limit = int(parts[1].strip())

        if speed < 0 or limit <= 0:
            return 0

        return (speed - limit) * 100 // limit

    except (ValueError, TypeError):
        return 0


def main():
    print("==== Running parse_ticket_id ====")
    user_input = input("Enter a ticket ID (e.g. TF-2024-0456): ")
    result = parse_ticket_id(user_input)
    print("Ticket Prefix, Year and Serial:", result)

    print("\n==== Running total_fines ====")
    user_input = input("Enter fine amounts as CSV (e.g. 500,1200,300): ")
    result = total_fines(user_input)
    print("Total Fines:", result)

    print("\n==== Running speed_excess ====")
    user_input = input("Enter speed/limit (e.g. 72/60): ")
    result = speed_excess(user_input)
    print("Percent Over Limit:", result)


if __name__ == "__main__":
    main()
