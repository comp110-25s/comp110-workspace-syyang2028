"""# of Teabags, Treats & Cost of Holding a Tea Party for X People"""

__author__: str = "730746714"


def main_planner(guests: int) -> None:
    """The Entry Point of My Program"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """ "How Many Teabags Needed for X Number of People"""
    return people * 2


def treats(people: int) -> int:
    """How Many Treats Needed for X Number of Teabags"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """The Cost for X Number of Teabags & X Number of Treats"""
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
