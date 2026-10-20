from pyscript import document
 
club_members = ["Luisito Balajadia", "Sascha Yellow", "Paul Blackwood", "Madilyn Pink", "Dave Blue", "Luis Balajadia", "Denie Manuntag"]
 

messages = {
    True: "Congratulations {name}! You are now part of the Communication Arts club.",
    False: "Sorry {name}, your name is not on the list.",
}
 
 
def get_full_name():
    """Get the first and last name from the page and combine them."""
    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()
 
  
    return f"{first_name} {last_name}".title()
 
 
def is_club_member(full_name):
    """Return True if the full name is in the club members list."""
    return full_name in club_members
 
 
def show_message(full_name, is_member):
    """Display the matching message in the result area."""
    message = messages[is_member].format(name=full_name)
    document.getElementById("message").innerHTML = message
 
 
def check_candidate(event):
    """Respond to the button click: get name, check list, show result."""

    full_name = get_full_name()
    is_member = is_club_member(full_name)
 
    show_message(full_name, is_member)