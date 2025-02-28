
#### main.py

```python
#!/usr/bin/env python3
import random

events = [
    "A binary star collision creates a luminous gamma-ray burst.",
    "A rogue planet enters a new star system, disrupting planetary orbits.",
    "A black hole devours a nearby neutron star, producing gravitational waves.",
    "A distant quasar erupts with the energy of a trillion stars.",
    "A supernova explosion ejects heavy elements into interstellar space."
]

def get_random_event():
    return random.choice(events)

def main():
    print("Welcome to Helios Celestial Events!")
    print("Here's a random cosmic event:")
    print(get_random_event())

if __name__ == "__main__":
    main()
