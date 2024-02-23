import requests

def fetch_deskpro_tickets(api_key):
    url = "https://your-deskpro-instance.com/api/v2/tickets"
    headers = {
        "Authorization": f"Basic {api_key}"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        return None

def structure_ticket_data(tickets):
    structured_data = []
    if tickets:
        for ticket in tickets:
            ticket_data = {
                "id": ticket["id"],
                "subject": ticket["subject"],
                "status": ticket["status"],
            }
            structured_data.append(ticket_data)
    return structured_data

def main():
    api_key = "your_api_key_here"
    tickets = fetch_deskpro_tickets(api_key)
    if tickets:
        structured_data = structure_ticket_data(tickets)
        for ticket_data in structured_data:
            print(ticket_data)

if __name__ == "__main__":
    main()
