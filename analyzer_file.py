import time
from collections import deque

def get_wireless_level(n_values):
    levels = deque(maxlen=n_values)  # This deque will automatically remove old elements when new ones are added
    while True:  # This creates an infinite loop
        try:
            with open("/proc/net/wireless", "r") as file:
                lines = file.readlines()
                for line in lines[2:]:  # The first two lines are headers
                    data = line.split()
                    level = float(data[3])  # Signal level is typically the 4th item
                    levels.append(level)
                    # Wait for the first n_values input values to always start with valid values
                    if len(levels) == n_values:
                        average = sum(levels) / len(levels)
                        print(f"Average wireless signal level: {average}")
        except FileNotFoundError:
            print("The file '/proc/net/wireless' does not exist on this system.")
        except Exception as e:
            print(f"An error occurred: {e}")

        time.sleep(0.05)  # Wait for 0.05 second before the next iteration

if __name__ == "__main__":
    get_wireless_level(3)  # Change average value amount
