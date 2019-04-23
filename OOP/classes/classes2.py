class Flight:

    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration

    def print_info(self):
        print(f"Flight origin: {self.origin}")
        print(f"Flight destination: {self.destination}")
        print(f"Flight duration: {self.duration}")
        print()


def main():

    # Create flight.
    f1 = Flight(origin="New York", destination="Paris", duration=540)
    f2 = Flight(origin="Tokyo", destination="Shanghai", duration=185)

    # Print details about flight.
    f1.print_info()
    f2.print_info()

if __name__ == "__main__":
    main()
