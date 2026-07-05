from app.config import (
    APP_NAME,
    VERSION,
    TOTAL_PARKING_SPACES,
    OCCUPIED_SPACES,
)

from app.parking import calculate_available_spaces
from app.parking_manager import ParkingManager


AVAILABLE_SPACES = calculate_available_spaces(
    TOTAL_PARKING_SPACES,
    OCCUPIED_SPACES,
)


def display_system_info():
    print("=" * 40)
    print(APP_NAME)
    print("=" * 40)
    print(f"Version            : {VERSION}")
    print(f"Total Spaces       : {TOTAL_PARKING_SPACES}")
    print(f"Occupied Spaces    : {OCCUPIED_SPACES}")
    print(f"Available Spaces   : {AVAILABLE_SPACES}")
    print("=" * 40)


display_system_info()

print()

manager = ParkingManager()
manager.create_demo_spaces()

print(f"Available Demo Spaces: {manager.count_available_spaces()}")

print()

manager.display_all_spaces()