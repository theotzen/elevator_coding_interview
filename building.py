from elevator import Elevator

class Building:
    def __init__(self, num_elevators=2, num_floors=10):
        self.num_elevators = num_elevators
        self.num_floors = num_floors
        self.elevators = [Elevator(current_floor=0, total_floors=num_floors) for _ in range(num_elevators)]

    def __str__(self):
        elevator_statuses = "\n".join([f"Elevator {i}: {str(elevator)}" for i, elevator in enumerate(self.elevators)])
        return f"Building with {self.num_floors} floors and {self.num_elevators} elevators:\n{elevator_statuses}"

    def request_elevator(self, current_floor, target_floor):
        # Find the closest elevator that can serve the request
        closest_elevator = None
        closest_distance = float("inf")

        for elevator in self.elevators:
            distance = abs(elevator.current_floor - current_floor)

            # Check if the elevator is static or moving in the same direction and the distance is more than 5 floors
            if (elevator.is_static() or
                (elevator.direction == "up" and current_floor > elevator.current_floor and target_floor > current_floor) or
                (elevator.direction == "down" and current_floor < elevator.current_floor and target_floor < current_floor)) and distance > 5:
                if distance < closest_distance:
                    closest_distance = distance
                    closest_elevator = elevator

        if closest_elevator is not None:
            closest_elevator.move_to_floor(current_floor)
            closest_elevator.move_to_floor(target_floor)
            return closest_elevator
        else:
            print("No available elevators.")
            return None

    def update_elevators(self):
        for elevator in self.elevators:
            elevator.update()