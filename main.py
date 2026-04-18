import tracker

print("Initializing...")
tracker.create_library()

test_book1 = {
         "id": 1,
         "name": "Oregairu"
    }

tracker.add_to_library(test_book1)

test_book2 = {
         "id": 2,
         "name": "Oshi no Ko"
    }

tracker.add_to_library(test_book2)