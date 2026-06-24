# Garden Advice App
# Provides gardening tips and advice based on the current month and season.

# TODO: Replace the hardcoded month number below with input() so the user
#       can enter the month themselves at runtime.

# TODO: Refactor the advice logic into a function called get_gardening_advice(month)
#       that takes a month number (1-12) and returns the appropriate advice string.

# TODO: Add a docstring to the script (and to any functions you create) explaining
#       what the program does, its inputs, and its outputs.

# TODO: Replace the hardcoded season strings with a helper function
#       called get_season(month) that returns the correct season for
#       Southern Hemisphere gardeners (South Africa, Australia, etc.).
"""
Garden Advice App
Provides gardening tips and advice based on the current month and season.
Southern Hemisphere seasons are used (e.g. South Africa, Australia).
"""


def get_season(month):
    """Return the season name for a given month (Southern Hemisphere)."""
    if month in [12, 1, 2]:
        return "Summer"
    elif month in [3, 4, 5]:
        return "Autumn"
    elif month in [6, 7, 8]:
        return "Winter"
    else:
        return "Spring"


def get_gardening_advice(month):
    """
    Return gardening advice for the given month number (1-12).
    Advice is tailored to the Southern Hemisphere growing calendar.
    """
    season = get_season(month)

    if season == "Summer":
        advice = (
            "Water your plants early in the morning to reduce evaporation. "
            "Watch out for pests like aphids and spider mites in the heat. "
            "Mulch garden beds to retain moisture."
        )
    elif season == "Autumn":
        advice = (
            "Plant garlic, onions, and broad beans now. "
            "Collect fallen leaves for composting. "
            "Begin preparing beds for winter crops."
        )
    elif season == "Winter":
        advice = (
            "Prune roses and fruit trees while they are dormant. "
            "Protect tender plants from frost with fleece or cloches. "
            "Plan your spring garden and order seeds."
        )
    else:
        advice = (
            "Start sowing seeds indoors for tomatoes, peppers, and eggplant. "
            "Begin weeding beds as the soil warms up. "
            "Apply a balanced fertiliser to lawns and garden beds."
        )

    return season, advice


while True:
    try:
        month = int(input("Enter the month number (1-12): "))
        if 1 <= month <= 12:
            break
        else:
            print("Please enter a number between 1 and 12.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")
season, advice = get_gardening_advice(month)

print(f"Month: {month}")
print(f"Season: {season}")
print(f"Gardening Advice: {advice}")
