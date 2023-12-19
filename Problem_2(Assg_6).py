#Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.
import json

# Dictionary of Indian states and capitals
indian_states = {
    "Maharashtra": "Mumbai",
    "Tamil Nadu": "Chennai",
    "Uttar Pradesh": "Lucknow",
    "Karnataka": "Bengaluru",
    "Gujarat": "Gandhinagar",
    "West Bengal": "Kolkata",
    "Rajasthan": "Jaipur"
}

with open("indian_states.json", "w") as file_write:
    json.dump(indian_states, file_write)

print("Data has been written to indian_states.json file.")
