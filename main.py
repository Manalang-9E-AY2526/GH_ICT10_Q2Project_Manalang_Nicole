
# shared python functions for nicole's student showcase
from pyscript import document

# dictionary containing non-metal elements
# each symbol stores the name, atomic number, and atomic mass
non_metals = {
    "H": ("Hydrogen", 1, 1.008),
    "He": ("Helium", 2, 4.0026),
    "C": ("Carbon", 6, 12.011),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "F": ("Fluorine", 9, 18.998),
    "Ne": ("Neon", 10, 20.180),
    "P": ("Phosphorus", 15, 30.974),
    "S": ("Sulfur", 16, 32.06),
    "Cl": ("Chlorine", 17, 35.45),
    "Ar": ("Argon", 18, 39.948),
    "Se": ("Selenium", 34, 78.971),
    "Br": ("Bromine", 35, 79.904),
    "Kr": ("Krypton", 36, 83.798),
    "I": ("Iodine", 53, 126.90),
    "Xe": ("Xenon", 54, 131.29),
    "Rn": ("Radon", 86, 222)
}


# function for checking the element symbol
def element_checker(e):
    # get the user's input
    element_symbol = document.getElementById("element_name").value.strip().title()

    if not element_symbol:
        document.getElementById("result").innerHTML = (
            "Please enter an element symbol."
        )
        return

    # retrieve element information using .get()
    result = non_metals.get(
        element_symbol,
        ("Not found in the non-metals list", "-", "-")
    )

    # display the element information
    document.getElementById("result").innerHTML = f"""
        <b>Element Symbol:</b> {element_symbol}<br>
        <b>Element Name:</b> {result[0]}<br>
        <b>Atomic Number:</b> {result[1]}<br>
        <b>Atomic Mass:</b> {result[2]}
    """


# function for checking theater club membership
def verify_candidate(e):
    # list of theater club members
    club_members = [
        "nicole manalang",
        "alyanna barlisan",
        "shiloh briones",
        "sheirhalyn gaddi",
        "cady bower",
        "maryam ledesma",
        "josua ortiz",
        "mocha manalang"
    ]

    # get and combine the entered names
    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()
    candidate_name = f"{first_name} {last_name}".strip()

    if not first_name or not last_name:
        document.getElementById("result").innerHTML = (
            "Please enter both your first and last name."
        )
        return

    # check if the name is on the list
    member_checker = candidate_name.lower() in club_members

    # choose a message using the boolean result
    messages = (
        f"Sorry {candidate_name}, your name is not on the list.",
        f"Congratulations {candidate_name}! You are now part of the Theater Club."
    )

    # show the result
    document.getElementById("result").innerHTML = messages[member_checker]


# function for the second quarter drill 2 student club directory
def add_member(e):
    # predefined theater club members
    club_members1 = {'Nicole Manalang', 'Alyanna Barlisan', 'Mae Kutosha'}
    club_members2 = {'Shiloh Briones', 'Sheirhalyn Gaddi', 'Ada dy'}
    club_members3 = {'Mel Avisala', 'Josua Ortiz', 'Alice Guo'}
    club_members4 = {'Mocha Manalang', 'Kemmy Ruth', 'Marygrace Piattos'}

    # get the entered first and last names
    first_name = document.getElementById('first_name').value.strip()
    last_name = document.getElementById('last_name').value.strip()

    if not first_name or not last_name:
        document.getElementById("output").innerHTML = (
            "Please enter both your first and last name."
        )
        return

    # combine the names into one new member
    new_member = first_name + " " + last_name
    new_member_set = {new_member}

    # combine all club members and the new member
    all_members = (
        club_members1 | club_members2 | club_members3 |
        club_members4 | new_member_set
    )

    # count the total number of unique members
    total_members = len(all_members)

    # arrange the names alphabetically
    members_list = "<br>".join(sorted(all_members))

    # display the member directory and total count
    document.getElementById('output').innerHTML = f'''
        <h3>Registered Members</h3>
        <p>{members_list}</p>
        <hr>
        <p>Total Members: {total_members}</p>
    '''
