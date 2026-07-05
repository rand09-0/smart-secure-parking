
# ==========================================
# Parking Manager
# Responsible for creating and managing
# all parking spaces in the system.
# ==========================================

from app.parking_space import ParkingSpace


class ParkingManager:

    def __init__(self):
        self.spaces = []

    def create_demo_spaces(self):

        for space_id in range(1, 6):

            occupied = space_id in [1, 3]

            self.spaces.append(
                ParkingSpace(space_id, occupied)
            )

    def count_available_spaces(self):

        count = 0

        for space in self.spaces:

            if not space.occupied:
                count += 1

        return count

    def display_all_spaces(self):

        for space in self.spaces:
            space.display_status()