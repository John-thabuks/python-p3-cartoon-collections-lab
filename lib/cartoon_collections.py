def roll_call_dwarves(names):
    for index, name in enumerate(names, 1):
        print(f"{index}. {name}")

def summon_captain_planet(planeteer):
    planeteer_calls = []
    for planet in planeteer:
        planeteer_calls.append(planet.capitalize() +"!") 
    return planeteer_calls

def long_planeteer_calls(short_words):
    for words in short_words:
        if len(words) > 4:
            return True
    return False

def find_the_cheese(cheese_type):
    cheese = ["cheddar", "gouda", "camembert"]
    for cheese_availabe in cheese_type:
        if cheese_availabe in cheese:        
            return cheese_availabe
    return None
