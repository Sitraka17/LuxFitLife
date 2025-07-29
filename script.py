import json
import os

class WeightSportTracker:
    def __init__(self, data_file='tracker_data.json'):
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                return json.load(file)
        return {'weights': [], 'sports': []}

    def save_data(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.data, file, indent=4)

    def add_weight_entry(self, weight, date):
        self.data['weights'].append({'date': date, 'weight': weight})
        self.save_data()

    def add_sport_entry(self, sport, duration, date):
        self.data['sports'].append({'date': date, 'sport': sport, 'duration': duration})
        self.save_data()

    def view_entries(self, entry_type):
        return self.data.get(entry_type, [])

def main():
    tracker = WeightSportTracker()

    while True:
        print("\nWeight and Sport Tracking App")
        print("1. Add Weight Entry")
        print("2. Add Sport Entry")
        print("3. View Weight Entries")
        print("4. View Sport Entries")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            weight = float(input("Enter your weight: "))
            date = input("Enter the date (YYYY-MM-DD): ")
            tracker.add_weight_entry(weight, date)
        elif choice == '2':
            sport = input("Enter the sport activity: ")
            duration = int(input("Enter the duration in minutes: "))
            date = input("Enter the date (YYYY-MM-DD): ")
            tracker.add_sport_entry(sport, duration, date)
        elif choice == '3':
            print("\nWeight Entries:")
            for entry in tracker.view_entries('weights'):
                print(f"Date: {entry['date']}, Weight: {entry['weight']}")
        elif choice == '4':
            print("\nSport Entries:")
            for entry in tracker.view_entries('sports'):
                print(f"Date: {entry['date']}, Sport: {entry['sport']}, Duration: {entry['duration']} minutes")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
