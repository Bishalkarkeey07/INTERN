import random
import threading
import time
class Car:
    def __init__(self, name):
        self.name = name
        self.decorations = []

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def get_details(self):
        return f"Car: {self.name}\nDecorations: {', '.join(self.decorations)}"

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

class Track:
    def __init__(self, length):
        self.length = length
        self.obstacles = ["Rock", "Tree", "Puddle"]
        self.power_ups = ["Nitro Boost", "Oil Slick", "Boost_UP"]

    def generate_track(self):
        
        obstacles = random.choices(self.obstacles, k=self.length)
        power_ups = random.choices(self.power_ups, k=self.length)
        return list(zip(obstacles, power_ups))

class Player:
    def __init__(self, name):
        self.name = name
        self.car = None

    def choose_car(self, car_type):
        self.car = CarFactory.create_car(car_type)  #player can chhose and the customize car

    def customize_car(self, decorations):
        for decoration in decorations:
            self.car.add_decoration(decoration)

    def get_car_details(self):
        return self.car.get_details()

class Game:
    def __init__(self):
        self.player = None
        self.track = None
        self.is_race_over = False

    def start_game(self):
        print("Welcome to the Race Car Game!")
        player_name = input("Enter your name in car race game: ")
        self.player = Player(player_name)
        self.show_car_selection()
        self.show_customize_menu()
        self.generate_track()

        race_thread = threading.Thread(target=self.start_race)
        race_thread.start()
        race_thread.join()
        self.wait_for_race_to_finish()
        self.end_game()

    def wait_for_race_to_finish(self):  #thread in each race
        while not self.is_race_over:
            time.sleep(1)

    def show_car_selection(self):
        car_types = ["sports", "sedan", "SUV"]
        print("Select a car type:")
        for i, car_type in enumerate(car_types, start=1):
            print(f"{i}. {car_type.capitalize()}")

        while True:
            try:
                car_choice = int(input("Enter your choice: "))
                if car_choice in range(1, len(car_types) + 1):
                    selected_car_type = car_types[car_choice - 1]    #Exception Handling is used
                    self.player.choose_car(selected_car_type)
                    break
                else:
                    print("Invalid choice. Please enter a valid option.")
            except ValueError:
                print("Invalid input. Please enter a numeric choice.")

    def show_customize_menu(self):
        decorations = ["Red paint", "Spoiler", "Alloy rims", "Neon lights"]
        print("Customize your car:")
        print("Available decorations:")
        for i, decoration in enumerate(decorations, start=1):
            print(f"{i}. {decoration}")
        print("Enter the numbers of decorations you want to add : ")

        while True:
            try:
                decoration_choices = input("Enter your choices: ").split(",")
                selected_decorations = [decorations[int(choice) - 1] for choice in decoration_choices if int(choice) in range(1, len(decorations) + 1)]
                if len(selected_decorations) == len(decoration_choices):
                    self.player.customize_car(selected_decorations)
                    break
                else:
                    print("Invalid choices. Please enter valid decoration numbers.")
            except ValueError:
                print("Invalid input. Please enter numeric choices .")

    def generate_track(self):
        self.track = Track(5)
        track_details = self.track.generate_track()
        print("Track Details:")
        for i, (obstacle, power_up) in enumerate(track_details, start=1):
            print(f"Segment {i}: Obstacle - {obstacle}, Power-up - {power_up}")

    def start_race(self):
        print("\nRace started!")
        time.sleep(5)  
        print("Race ended!")
        self.is_race_over = True

    def end_game(self):
        if self.is_race_over:
            print(f"\nCongratulations, {self.player.name}! You are the winner!")
# this is main program
if __name__ == "__main__":
    game = Game()
    game.start_game()
