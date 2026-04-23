import tracker

print("Initializing...")
tracker.create_library()

while True:
    print("\n---Menu---")
    print("1. Display Library")
    print("2. Adds a Book")
    print("3. Update a Book")
    print("4. Quit")

    choice = input("\nChoose an option: ")
    if choice == "1":
        print("\n---Library---")
        tracker.display_library()
    elif choice == "2":
        print("\n---Add a Book---")
        tracker.new_book()
    elif choice == "3":
        print("\n---Update a Book---")
        tracker.update_book()
    elif choice == "4":
        print("\nExiting...")
        break