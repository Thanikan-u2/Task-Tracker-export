import requests
import csv

# Simulated API endpoint (this could be replaced with a real one)
def get_mock_tickets():
    return [
        {"id": 1, "title": "Fix login bug", "status": "Open", "priority": "High", "owner": "Alice"},
        {"id": 2, "title": "Add unit tests", "status": "In Progress", "priority": "Medium", "owner": "Bob"},
        {"id": 3, "title": "Update README", "status": "Done", "priority": "Low", "owner": "Charlie"}
    ]

# Export to CSV
def export_tickets_to_csv(tickets, filename="tickets_export.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=tickets[0].keys())
        writer.writeheader()
        writer.writerows(tickets)

if __name__ == "__main__":
    print("Fetching ticket data...")
    tickets = get_mock_tickets()
    export_tickets_to_csv(tickets)
    print(f"Exported {len(tickets)} tickets to 'tickets_export.csv'")
