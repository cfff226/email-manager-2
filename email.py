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
        print(f"\n------------------- This email has been read --------------------\n")


# Function which creates the email inbox.
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


# Function which prints the email’s subject_line, along with a corresponding number.
def list_emails(inbox):
    inbox_emails = [email for email in inbox]
    print("\n--------------------- Emails in your inbox ---------------------\n")
    for i, email in enumerate(inbox_emails, 1):
        print(f"\n{i}: {email.subject_line}")


# Create a function which displays a selected email.
def read_email(inbox, index):
    print(f"\n------------------------- Email {index} -------------------------\n")
    index = int(index)
    selected_email = inbox[index - 1]
    print(
        f"\n\nFrom: {selected_email.email_address}\n\nTitle: {selected_email.subject_line}\n\nEmail: {selected_email.email_content}\n\n"
    )
    # Once displayed, call the class method to set its 'has_been_read' variable to True.
    selected_email.mark_as_read()


# Display the menu.
menu = True

inbox = populate_inbox()
while True:
    try:
        user_choice = int(
            input(
                """\nWould you like to:\n
        1. Read an email
        2. View unread emails
        3. Quit application

        Enter selection: """
            )
        )
        if user_choice == 1:
            # Logic to read an email.
            while True:
                list_emails(inbox)
                try:
                    index = input(
                        "\n\nPlease select an email from the list that you would like to read: "
                    )
                    # Check if the index number is higher than inbox length.
                    if int(index) > len(inbox):
                        print(
                            "\n\n--------------- This number isn't in your inbox ----------------\n"
                        )
                        continue
                    # Check if index number is less than or equal to 0.
                    if int(index) <= 0:
                        print(
                            "\n\n--------------- This number isn't in your inbox ----------------\n"
                        )
                        continue
                # Show a value error if a number isn't entered.
                except ValueError:
                    print(
                        "\n-------------------- Please enter a number ---------------------\n"
                    )
                    continue
                else:
                    read_email(inbox, index)
                    break
        elif user_choice == 2:
            # Logic to view unread emails.
            unread_emails = [email for email in inbox if not email.has_been_read]
            print("\n------------------------- Unread Emails -------------------------\n")
            if len(unread_emails) == 0:
                print(
                    "\n------------------ There are no unread emails ------------------\n"
                )
            else:
                for i, email in enumerate(unread_emails, 1):
                    print(f"\n{i}: {email.subject_line}")
                print("\n")
                continue
        elif user_choice == 3:
            # Logic to quit appplication.
            print("\n-------------- Thanks for using the Email Manager ---------------\n")
            exit()
            # Check if choice is greater than or less than or equal to 0.
        elif user_choice > 3 or user_choice >= 0:
            print(
                "\n--------------------- Oops! Incorrect input --------------------\n"
            )
            continue
    # Show a value error if an incorrect value is entered.
    except ValueError:
        print("\n--------------------- Oops! Incorrect input --------------------\n")
        continue
