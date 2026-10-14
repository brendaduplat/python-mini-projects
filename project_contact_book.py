import unicodedata

MENU = (
    "\n1. View contact list.\n"
    "2. Search for a contact by name.\n"
    "3. Add a new phone number.\n"
    "4. Count contacts with more than one phone number.\n"
    "5. Exit."
)

def normalize(text):
    text = text.lower()
    text = unicodedata.normalize("NFD", text)
    text = text.encode("ascii", "ignore")
    text = text.decode("ascii")
    return text

def print_contact(contact):
    print(f"\nName: {contact['name']}")
    print(f"Phone(s): {', '.join(contact['phones'])}")
    print(f"Email(s): {', '.join(contact['emails'])}")

contacts = [
    {
        "name": "Ana Silva",
        "phones": ["71 99999-1111", "71 98888-2222"],
        "emails": ["ana@gmail.com", "ana.silva@empresa.com"],
    },
    {
        "name": "Bruno Costa",
        "phones": ["71 97777-3333"],
        "emails": ["bruno@gmail.com"],
    },
    {
        "name": "Carla Souza",
        "phones": ["71 96666-4444", "71 95555-5555"],
        "emails": ["carla@gmail.com", "carla.souza@hotmail.com"],
    },
    {
        "name": "Daniel Oliveira",
        "phones": ["71 94444-6666"],
        "emails": ["daniel@gmail.com"],
    },
    {
        "name": "Eduarda Santos",
        "phones": ["71 93333-7777", "71 92222-8888", "71 91111-9999"],
        "emails": ["eduarda@gmail.com"],
    },
    {
        "name": "Felipe Lima",
        "phones": ["71 90000-1234"],
        "emails": ["felipe@gmail.com", "felipe.lima@yahoo.com"],
    },
    {
        "name": "Gabriela Rocha",
        "phones": ["71 98888-5678"],
        "emails": ["gabriela@gmail.com"],
    },
    {
        "name": "Henrique Alves",
        "phones": ["71 97777-8765", "71 96666-4321"],
        "emails": ["henrique@gmail.com"],
    },
]

while True:
    print(MENU)
    option = input("Enter the desired option: ")

    if option == "1":
        for contact in contacts:
            print_contact(contact)

    elif option == "2":
        search = normalize(input("Enter the name you want to search for: ").strip())
        found = False
        for contact in contacts:
            if search in normalize(contact["name"]):
                print_contact(contact)
                found = True
        if not found:
            print("Name not found.")

    elif option == "3":
        name = normalize(input("Enter the contact's full name: ").strip())
        phone = input("Enter the phone number to add: ").strip()
        if not phone:
            print("Phone number cannot be empty.")
            continue
        found = False
        for contact in contacts:
            if name == normalize(contact["name"]):
                contact["phones"].append(phone)
                print(f"Phone number added to {contact['name']}.")
                found = True
                break
        if not found:
            print("Name not found.")

    elif option == "4":
        multiple_phones = [c for c in contacts if len(c["phones"]) > 1]
        print(f"\nContacts with more than one phone number: {len(multiple_phones)}")
        for contact in multiple_phones:
            print(f"- {contact['name']}")

    elif option == "5":
        break

    else:
        print("Invalid option.")