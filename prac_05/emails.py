def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = determine_name_from_email(email)
        confirmation = input(f"Is your name {name}")
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    for email, name in email_to_name.items():
        print(f"{name} {email}")


def determine_name_from_email(email):
    """Returns assumed name from email entered."""
    base_extracted_name = email.split('@')[0]
    name_in_parts = base_extracted_name.split('.')
    name = " ".join(name_in_parts).title()
    return name


main()
