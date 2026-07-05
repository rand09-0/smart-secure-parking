class ParkingSpace:

    def __init__(self, space_id, occupied=False):
        self.space_id = space_id
        self.occupied = occupied

    def display_status(self):
        status = "Occupied" if self.occupied else "Available"
        print(f"Space {self.space_id}: {status}")