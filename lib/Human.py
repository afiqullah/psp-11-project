import json
import random

# Read pills.json for pill information

try:
    with open('./pills.json', 'r', encoding='utf-8') as file:
        pills = json.load(file)
except FileNotFoundError:
    print("Error: The file 'pills.json' could not be found.")
except json.JSONDecodeError:
    print("Error: The file contains invalid JSON formatting.")

# Human class, which includes all functions

class Human:
    def __init__(self):
        # Initialise the class with random health information and a fixed amount of cash (100)
        self.protein = random.randint(1, 75)
        self.vitamins = random.randint(1, 75)
        self.minerals = random.randint(1, 75)
        self.cash = 100

    def viewPills(self) -> list:
        """Returns a list of the dictionaries of all available pills"""

        return pills

    def getPillInfo(self, choice: str) -> dict | None:
        """Get a pill's information as a dictionary. [Despacitone/Gigachadus/Aurafarmine]"""

        # Error handler if no choice is provided
        if not choice:
            print("Error: Please name a pill to eat.")
            return None
        
        # Error handler if choice parsed is not a string
        if not isinstance(choice, str):
            print("Error: Choice of pill must be a string.")
            return None

        match choice.lower():
            case "despacitone":
                return pills[0]
            case "gigachadus":
                return pills[1]
            case "aurafarmine":
                return pills[2]
            case _:
                print("Error: No pill found!")
                return None

    def eatPill(self, choice: str) -> str | None:
        """Purchase a certain pill and eat it, gaining its nutrition. [Despacitone/Gigachadus/Aurafarmine]"""

        # Error handler if no choice is provided
        if not choice:
            print("Error: Please name a pill to eat.")
            return None

        # Retrieve pill information
        toEat = self.getPillInfo(choice)

        if toEat != None:
            # Check if the human has enough cash to afford the pill
            if self.cash < toEat["cost"]:
                return print("You don't have enough money!")

            # Add the nutrition provided by the pill and deduct the cash
            self.protein += toEat["protein"]
            self.vitamins += toEat["vitamins"]
            self.minerals += toEat["minerals"]
            self.cash -= toEat["cost"]

            # Prevent nutrition percentages from going past 100%

            if self.protein > 100:
                self.protein = 100

            if self.vitamins > 100:
                self.vitamins = 100

            if self.minerals > 100:
                self.minerals = 100

            return "Eaten " + toEat["name"] + "!"
        else:
            print("Error: No pill is eaten.")
            return None

    def getBestPill(self) -> str:
        """Automatically determine the best pill to eat at the moment based on current health status."""

        # Despacitone: HIGH Vitamins, MEDIUM Minerals
        # Gigachadus: HIGH Protein, MEDIUM Vitamins
        # Aurafarmine: HIGH Minerals, MEDIUM Protein

        # Algorithm to determine need of each pill

        desp = 0
        giga = 0
        aura = 0

        if self.protein <= 30:
            giga += 1
        elif self.protein <= 65:
            aura += 1

        if self.vitamins <= 30:
            desp += 1
        elif self.vitamins <= 65:
            giga += 1

        if self.minerals <= 30:
            aura += 1
        elif self.minerals <= 65:
            desp += 1

        # Choosing the pills based on the points given
        if desp >= giga and desp >= aura:
            return "Despacitone"
        elif giga >= aura:
            return "Gigachadus"
        else:
            return "Aurafarmine"

    def getStats(self) -> dict:
        """Returns a dictionary of the protein, vitamins and minerals statistics and cash of the human."""

        return {
            "protein": self.protein,
            "vitamins": self.vitamins,
            "minerals": self.minerals,
            "cash": self.cash
        }
