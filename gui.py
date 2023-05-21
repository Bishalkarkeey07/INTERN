import random
import threading
import time
import tkinter as tk
from tkinter import font

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
        self.car = CarFactory.create_car(car_type)

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
        self.root = tk.Tk()
        self.root.title("Race Car Game")
        self.root.geometry("600x400")
        self.create_widgets()

    def create_widgets(self):
        self.intro_label = tk.Label(self.root, text="Welcome to the Race Car Game!", font=("Arial", 24))
        self.intro_label.pack(pady=20)

        self.name_label = tk.Label(self.root, text="Enter your name in the car race game:", font=("Arial", 14))
        self.name_label.pack()

        self.name_entry = tk.Entry(self.root, font=("Arial", 14))
        self.name_entry.pack(pady=10)

        self.start_button = tk.Button(self.root, text="Start Game", font=("Arial", 16), command=self.initialize_game)
        self.start_button.pack(pady=20)

    def initialize_game(self):
        player_name = self.name_entry.get()
        self.player = Player(player_name)
        self.create_car_selection()

    def create_car_selection(self):
        self.clear_widgets()

        self.car_label = tk.Label(self.root, text="Select a car type:", font=("Arial", 18))
        self.car_label.pack()

        car_types = ["sports", "sedan", "SUV"]
        self.car_var = tk.StringVar()
        self.car_var.set(car_types[0])

        for car_type in car_types:
            radio_button = tk.Radiobutton(self.root, text=car_type.capitalize(), variable=self.car_var, value=car_type, font=("Arial", 14))
            radio_button.pack()

        self.car_button = tk.Button(self.root, text="Choose Car", font=("Arial", 16), command=self.customize_car)
        self.car_button.pack(pady=20)

    def customize_car(self):
        self.player.choose_car(self.car_var.get())
        self.clear_widgets()

        self.decoration_label = tk.Label(self.root, text="Customize your car:", font=("Arial", 18))
        self.decoration_label.pack()

        decorations = ["Red paint", "Spoiler", "Alloy rims", "Neon lights"]
        self.selected_decorations = []

        for decoration in decorations:
            checkbox = tk.Checkbutton(self.root, text=decoration, font=("Arial", 12), command=lambda decoration=decoration: self.toggle_decoration(decoration))
            checkbox.pack()

        self.done_button = tk.Button(self.root, text="Done", font=("Arial", 16), command=self.generate_track)
        self.done_button.pack(pady=20)

    def toggle_decoration(self, decoration):
        if decoration in self.selected_decorations:
            self.selected_decorations.remove(decoration)
        else:
            self.selected_decorations.append(decoration)

    def generate_track(self):
        self.player.customize_car(self.selected_decorations)
        self.clear_widgets()

        self.track = Track(5)
        track_details = self.track.generate_track()

        self.track_label = tk.Label(self.root, text="Track Details:", font=("Arial", 18))
        self.track_label.pack()

        for i, (obstacle, power_up) in enumerate(track_details, start=1):
            segment_label = tk.Label(self.root, text=f"Segment {i}: Obstacle - {obstacle}, Power-up - {power_up}", font=("Arial", 12))
            segment_label.pack()

        self.start_race()

    def start_race(self):
        self.race_label = tk.Label(self.root, text="Race started!", font=("Arial", 20))
        self.race_label.pack()

        self.is_race_over = False
        race_thread = threading.Thread(target=self.wait_for_race_to_finish)
        race_thread.start()

    def wait_for_race_to_finish(self):
        time.sleep(5)
        self.is_race_over = True
        self.end_game()

    def end_game(self):
        self.clear_widgets()

        if self.is_race_over:
            winner_label = tk.Label(self.root, text=f"Congratulations, {self.player.name}! You are the winner!", font=("Arial", 24))
            winner_label.pack()

    def clear_widgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    game = Game()
    game.start_game()
    game.root.mainloop()
