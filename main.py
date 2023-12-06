import time
from building import Building

building = Building(num_elevators=3, num_floors=20)

# Simulate an elevator moving from floor 3 to floor 15
elevator1 = building.elevators[0]
elevator1.move_to_floor(3)
elevator1.move_to_floor(15)

while True:
    print(building)
    time.sleep(1)
    building.update_elevators()

    user_input = input("Enter 'current_floor,target_floor' to request an elevator or 'q' to quit: ").strip()
    if user_input.lower() == 'q':
        break

    try:
        current_floor, target_floor = map(int, user_input.split(','))
        elevator = building.request_elevator(current_floor, target_floor)
        print("Selected elevator:", elevator)
    except ValueError:
        print("Invalid input. Please enter 'current_floor,target_floor' or 'q' to quit.")