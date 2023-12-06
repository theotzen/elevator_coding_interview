class Elevator:
    def __init__(self, current_floor=0, total_floors=10):
        self.current_floor = current_floor
        self.total_floors = total_floors
        self.target_floor = None
        self.direction = "static"

    def __str__(self):
        return f"Elevator is on floor {self.current_floor}, moving {self.direction}."

    def move_to_floor(self, target_floor):
        if target_floor < 0 or target_floor >= self.total_floors:
            print("Invalid floor.")
            return

        self.target_floor = target_floor

        if self.target_floor > self.current_floor:
            self.direction = "up"
        elif self.target_floor < self.current_floor:
            self.direction = "down"
        else:
            self.direction = "static"

    def update(self):
        if self.direction == "up":
            self.current_floor += 1
            if self.current_floor == self.target_floor:
                self.direction = "static"
                self.target_floor = None
        elif self.direction == "down":
            self.current_floor -= 1
            if self.current_floor == self.target_floor:
                self.direction = "static"
                self.target_floor = None

    def is_static(self):
        return self.direction == "static"

    def is_moving_up(self):
        return self.direction == "up"

    def is_moving_down(self):
        return self.direction == "down"