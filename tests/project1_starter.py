"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Your Name Here]
Date: [Date]

AI Usage: I used Ai in order to help me implement os.path and import os as well as "utf"
Example: AI helped with file I/O error handling logic in save_character function
"""

# Function to create a new character with initial stats
def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    
    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """

    # Initialize starting level
    level = 1

    # Calculate stats based on class and level using helper function
    strength, magic, health = calculate_stats(character_class, level)

    # Create dictionary representing the character
    character = {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": 100  # Default starting gold
    }

    # Return the created character dictionary
    return character

    # TODO: Implement this function
    # Remember to use calculate_stats() function for stat calculation
    pass


# Function to calculate a character's stats depending on their class and level
def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    
    Design your own formulas! Ideas:
    - Warriors: High strength, low magic, high health
    - Mages: Low strength, high magic, medium health  
    - Rogues: Medium strength, medium magic, low health
    - Clerics: Medium strength, high magic, high health
    """

    # Assign stat growth depending on the character's class
    if character_class == "warrior":
        strength = 10 + level * 3
        magic = 2 + level
        health = 100 + level * 10
    elif character_class == "mage":
        strength = 5 + level
        magic = 15 + level * 4
        health = 80 + level * 8
    elif character_class == "rogue":
        strength = 8 + level * 2
        magic = 8 + level * 2
        health = 70 + level * 7
    elif character_class == "cleric":
        strength = 7 + level * 2
        magic = 12 + level * 3
        health = 90 + level * 9
    else:
        # Return False if an unrecognized class is entered
        return False

    # Return the calculated stats as a tuple
    return (strength, magic, health)

    # TODO: Implement this function
    # Return a tuple: (strength, magic, health)
    pass


# Import the os module for file and path handling
import os

# Function to save a character to a text file
def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """

    # Get the directory part of the filename
    directory = os.path.dirname(filename)

    # If a directory is specified and does not exist, return False
    if directory and not os.path.exists(directory):
        return False
    
    # Open the file in write mode using UTF-8 encoding
    with open(filename, "w", encoding="utf-8") as f:
        # Write each character attribute to a new line
        f.write(f"Character Name: {character['name']}\n")
        f.write(f"Class: {character['class']}\n")
        f.write(f"Level: {character['level']}\n")
        f.write(f"Strength: {character['strength']}\n")
        f.write(f"Magic: {character['magic']}\n")
        f.write(f"Health: {character['health']}\n")
        f.write(f"Gold: {character['gold']}\n")

    # Return True if file was successfully written
    return True

    # TODO: Implement this function
    # Remember to handle file errors gracefully
    pass


# Function to load a character from a saved text file
def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """

    # Check if the file exists before reading
    if not os.path.exists(filename):
        return None

    # Open the file safely with UTF-8 encoding and read all lines
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()        

    # Temporary dictionary to hold parsed character data
    char = {}

    # Loop through each line to extract key-value pairs
    for line in lines:
        if ": " in line:
            key, value = line.strip().split(": ", 1)
            # Convert key to lowercase and replace spaces with underscores
            key = key.lower().replace(" ", "_")

            # Convert numeric values from strings to integers
            if key in ["level", "strength", "magic", "health", "gold"]:
                value = int(value)
            char[key] = value

    # Return a properly structured dictionary for the character
    return {
        "name": char.get("character_name"),
        "class": char.get("class"),
        "level": char.get("level"),
        "strength": char.get("strength"),
        "magic": char.get("magic"),
        "health": char.get("health"),
        "gold": char.get("gold")
    }

    # TODO: Implement this function
    # Remember to handle file not found errors
    pass


# Function to print a formatted character sheet to the console
def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """

    # Display the formatted character details
    print("\n=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")
    print("=======================")

    # TODO: Implement this function
    pass


# Function to increase a character's level and recalculate their stats
def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """

    # Increment the character's level
    character["level"] += 1

    # Recalculate stats using the updated level
    strength, magic, health = calculate_stats(character["class"], character["level"])

    # Update the character's stats in the dictionary
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health

    # TODO: Implement this function
    # Remember to recalculate stats for the new level
    pass


# Main program for testing functions
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
    # Example usage (uncomment to test):
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
