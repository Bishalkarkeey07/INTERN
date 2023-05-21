import random
import threading
# Car class
class Car:
    def __init__(self, name):
        self.name = name
        self.decorations = []

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def get_details(self):
        return f"Car: {self.name}\nDecorations: {', '.join(self.decorations)}"

# CarFactory class
class CarFactory:
    @staticmethod
    def create_car(car_type):
        if car_type == "sports":
            return Car("Sports Car")
        elif car_type == "sedan":
            return Car("Sedan")
        elif car_type == "SUV":
            return Car("SUV")
        else:
            raise ValueError("Invalid car type")

# Track class
class Track:
    def __init__(self, length):
        self.length = length
        self.obstacles = ["Rock", "Tree", "Puddle"]
        self.power_ups = ["Nitro Boost", "Oil Slick", "Shield"]

    def generate_track(self):
        obstacles = random.choices(self.obstacles, k=self.length)
        power_ups = random.choices(self.power_ups, k=self.length)
        return list(zip(obstacles, power_ups))

# Player class
class Player:
    def __init__(self):
        self.car = None

    def choose_car(self, car_type):
        self.car = CarFactory.create_car(car_type)

    def customize_car(self, decorations):
        for decoration in decorations:
            self.car.add_decoration(decoration)

    def get_car_details(self):
        return self.car.get_details()

# Game class
class Game:
    def __init__(self):
        self.player = Player()
        self.track = None
        self.is_race_over = False

    def start_game(self):
        print("Welcome to the Race Car Game!")
        self.show_car_selection()
        self.show_customize_menu()

        self.track = Track(10)
        track_details = self.track.generate_track()
        print("Track Details:")
        for i, (obstacle, power_up) in enumerate(track_details, start=1):
            print(f"Segment {i}: Obstacle - {obstacle}, Power-up - {power_up}")

        self.is_race_over = False
        self.start_race()

    def show_car_selection(self):
        car_types = ["sports", "sedan", "SUV"]
        print("Select a car type:")
        for i, car_type in enumerate(car_types, start=1):
            print(f"{i}. {car_type.capitalize()}")
        car_choice = int(input("Enter your choice: "))
        selected_car_type = car_types[car_choice - 1]
        self.player.choose_car(selected_car_type)

    def show_customize_menu(self):
        decorations = ["Red paint", "Spoiler", "Alloy rims", "Neon lights"]
        print("Customize your car:")
        print("Available decorations:")
        for i, decoration in enumerate(decorations, start=1):
            print(f"{i}. {decoration}")
        print("Enter the numbers of decorations you want to add (comma-separated): ")
        decoration_choices = input("Enter your choices: ").split(",")
        selected_decorations = [decorations[int(choice) - 1] for choice in decoration_choices]
        self.player.customize_car(selected_decorations)

    def start_race(self):
        print("\nRace started!")
        while not self.is_race_over:
            pass

        print("\nRace ended!")
        winner = "Player 1"  # Determine the actual winner based on race results
        print(f"The winner is: {winner}")

    def end_game(self):
        self.is_race_over = True

# Threading
def run_game():
    game = Game()
    game.start_game()

def run_game_thread():
    game_thread = threading.Thread(target=run_game)
    game_thread.start()


# Main program
if __name__ == "__main__":
    run_game_thread()
