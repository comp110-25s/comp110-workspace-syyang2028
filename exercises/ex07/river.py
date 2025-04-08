"""File to define River class."""

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []

        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        # Checking for Fish
        living_fish: list[Fish] = []
        idx: int = 0
        while idx < len(self.fish):
            if self.fish[idx].age <= 3:
                living_fish.append(self.fish[idx])
            idx += 1
        self.fish = living_fish

        # Checking for Bears
        living_bears: list[Bear] = []
        idx = 0
        while idx < len(self.bears):
            if self.bears[idx].age <= 5:
                living_bears.append(self.bears[idx])
            idx += 1
        self.bears = living_bears

        return None

    def remove_fish(self, amount: int):
        count: int = 0
        while count < amount:
            self.fish.pop(0)
            count += 1
        return None

    def bears_eating(self):
        idx: int = 0
        while idx < len(self.bears):
            if len(self.fish) > 5:
                self.remove_fish(3)
                self.bears[idx].eat(3)
                idx += 1
            else:
                idx += len(self.bears)

        return None

    def check_hunger(self):
        living_bears: list[Bear] = []
        idx: int = 0
        while idx < len(self.bears):
            if self.bears[idx].hunger_score >= 0:
                living_bears.append(self.bears[idx])
            idx += 1
        self.bears = living_bears
        return None

    def repopulate_fish(self):
        fry: int = (len(self.fish) // 2) * 4
        for _ in range(0, fry):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        cubs: int = len(self.bears) // 2
        for _ in range(0, cubs):
            self.bears.append(Bear())

        return None

    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        day_idx: int = 1
        while day_idx <= 7:
            self.one_river_day()
            day_idx += 1
        return None
