### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
class Email:
    def __init__(self, email_address, subject_line, email_content):
        self.has_been_read = False
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    # Create the method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        self.has_been_read = True
        print(f"\n------------------ This email has been read -------------------\n")

# --- Lists --- #
# Initialise an empty list to store the email objects.

# --- Functions --- #
# Build out the required functions for your program.

def populate_inbox():
    # Create 3 sample emails and add it to the Inbox list. 
    inbox = [
        Email(
            "caroline.fox21@outlook.com",
            "Submitting Task 18",
            "Hello, This is my submission for my task 18",
        ),
        Email(
            "jonathan.doe@outlook.com",
            "Requesting extension",
            "Hi, can I please have an extension on task 18",
        ),
        Email(
            "kelly.smith@outlook.com",
            "Submitting Task 20",
            "Hi, this is my submission for my task 20",
        ),
    ]
    return inbox

def list_emails():
    
    # Create a function which prints the email’s subject_line, along with a corresponding number.

def read_email(index):

    # Create a function which displays a selected email. 
    # Once displayed, call the class method to set its 'has_been_read' variable to True.

# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.

# Fill in the logic for the various menu operations.
menu = True

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
       
    if user_choice == 1:
        # add logic here to read an email
        
    elif user_choice == 2:
        # add logic here to view unread emails
            
    elif user_choice == 3:
        # add logic here to quit appplication

    else:
        print("Oops - incorrect input.")
