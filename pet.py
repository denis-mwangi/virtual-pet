class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5      # 0 = full, 10 = very hungry
        self.energy = 5      # 0 = tired, 10 = fully rested
        self.happiness = 5   # 0–10 scale
        self.tricks = []     # bonus: learned tricks

    def eat(self):
        """Reduce hunger by 3 (min 0) and increase happiness by 1 (max 10)."""
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} enjoyed the meal! 🍽️")

    def sleep(self):
        """Increase energy by 5 (max 10)."""
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} had a nice nap! 😴")

    def play(self):
        """
        Decrease energy by 2, increase happiness by 2,
        increase hunger by 1. If too tired, refuse.
        """
        if self.energy < 2:
            print(f"{self.name} is too tired to play. Let them rest!")
            return
        self.energy -= 2
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} had fun playing! 🎾")

    def train(self, trick):
        """Teach a new trick and boost happiness by 1."""
        self.tricks.append(trick)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} learned a new trick: {trick}! 🎉")

    def show_tricks(self):
        """List all learned tricks."""
        if not self.tricks:
            print(f"{self.name} hasn't learned any tricks yet.")
        else:
            print(f"{self.name} knows: {', '.join(self.tricks)}")

    def get_status(self):
        """Print current stats for hunger, energy, and happiness."""
        print(f"\n🐾 {self.name}'s Status 🐾")
        print(f"  Hunger:    {self.hunger}/10")
        print(f"  Energy:    {self.energy}/10")
        print(f"  Happiness: {self.happiness}/10")
        print("-" * 25)
