import tracker

print("Initializing...")
tracker.create_library()

while True:
    choice = tracker.menu()
    match choice:
        case "1":
            tracker.display_library()
        case "2":
            tracker.add_book()
        case "3":
            tracker.update_book()
        case "4":
            tracker.delete_book()
        case "5":
            print("\nExiting...")
            break
        case _:
            print("Invalid option, please try again")