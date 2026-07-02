class Court:
    def __init__(self, court_id, name, price_per_hour):
        self.court_id = court_id
        self.name = name
        self.price_per_hour = price_per_hour
        self.is_available = True

    def book(self):
        if self.is_available:
            self.is_available = False
            return True
        return False


courts_system = {
    'C01': Court('C01', 'Court No. 1', 300000),
    'C02': Court('C02', 'Court No. 2', 200000),
    'C03': Court('C03', 'Court No. 3', 300000),
}


def show_menu():
    print('\n=== BASKETBALL COURT BOOKING SYSTEM ===')
    print('1. View Available Courts')
    print('2. Book a Court')
    print('3. Exit')


def show_available_courts():
    print('\nAvailable Courts:')
    found = False
    for court_id, court in courts_system.items():
        if court.is_available:
            print(
                f'{court_id}. {court.name} - {court.price_per_hour} VND/hour')
            found = True
    if not found:
        print('No courts are available right now.')


def book_court():
    court_id = input(
        'Enter court ID to book (for example C01): ').strip().upper()
    court = courts_system.get(court_id)

    if court is None:
        print('Court not found.')
        return

    if court.book():
        print(f'{court.name} has been booked successfully.')
    else:
        print(f'{court.name} is already booked.')


def main():
    while True:
        show_menu()
        choice = input('Enter your choice (1-3): ').strip()

        if choice == '1':
            show_available_courts()
        elif choice == '2':
            book_court()
        elif choice == '3':
            print('Thank you for using the system. Goodbye!')
            break
        else:
            print('Invalid choice. Please try again.')


if __name__ == '__main__':
    main()
