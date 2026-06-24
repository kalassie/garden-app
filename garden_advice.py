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

month = 6  # Hardcoded month - January=1, December=12

if month in [12, 1, 2]:
    season = "Summer"
    advice = (
        "Water your plants early in the morning to reduce evaporation. "
        "Watch out for pests like aphids and spider mites in the heat. "
        "Mulch garden beds to retain moisture."
    )
elif month in [3, 4, 5]:
    season = "Autumn"
    advice = (
        "Plant garlic, onions, and broad beans now. "
        "Collect fallen leaves for composting. "
        "Begin preparing beds for winter crops."
    )
elif month in [6, 7, 8]:
    season = "Winter"
    advice = (
        "Prune roses and fruit trees while they are dormant. "
        "Protect tender plants from frost with fleece or cloches. "
        "Plan your spring garden and order seeds."
    )
else:
    season = "Spring"
    advice = (
        "Start sowing seeds indoors for tomatoes, peppers, and eggplant. "
        "Begin weeding beds as the soil warms up. "
        "Apply a balanced fertiliser to lawns and garden beds."
    )

print(f"Month: {month}")
print(f"Season: {season}")
print(f"Gardening Advice: {advice}")
