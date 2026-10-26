
# Import the tools for the HTML to function
from pyscript import document

# Volleyball club members of Sta. Ana
def candidate_checker(e):
    club_members = {
        'SIMRAT KAUR', 'ANTOINETTE FAUSTINO', 'ERIN AMERICA',
        'ELEANOR OSEA', 'ISHMEEN SEKHON', 'DHIA LAL', 'ZOE JARLEGO',
        'MIKAELA CUEVAS', 'ROUX PAREDES', 'BIANCA DE PAZ',
        'CHRISTAL DEL ROSARIO', 'MAIA FABRIGAS', 'ABBY LEVINE',
        'DAPHNE CASTRO', 'LILY GAMBOL', 'ALTHENA MATIENZO',
        'FRANCHESCA MONTEROLA', 'EKNOOR VIRK'
    }

    # Get the first and last name
    first_name = document.getElementById("first_name").value.strip().upper()
    last_name = document.getElementById("last_name").value.strip().upper()
    # Combine the first and last names
    candidate = first_name + ' ' + last_name
    # Check if the candidate is a club member
    member_checker = candidate in club_members

    # Display the members status
    messages = (
        f'Sorry {candidate}, your name is not on the list. You are not a member of the Volleyball Club varsity.🥺',
        f'Congratulations {candidate}!, your name is on the list. You are now a member of the Volleyball Club varsity! 🎉'
    )

    document.getElementById('output').innerHTML = messages[member_checker]
