import csv
import random
from datetime import datetime, timedelta

def random_date(start, end):
    return start + timedelta(days=random.randint(0, int((end - start).days)))

def main():
    # 1. Suppliers
    suppliers = [
        {"Supplier Name": "Apex Metal Fabricators", "Type": "Metal fabricator", "Contact Name": "John Smith", "Email": "john@apexmetals.com", "Phone": "555-0101"},
        {"Supplier Name": "Global Extrusion Partners", "Type": "Extrusion partner", "Contact Name": "Sarah Lee", "Email": "sarah@globalextrusion.com", "Phone": "555-0102"},
        {"Supplier Name": "Prime Hardware Dist", "Type": "Hardware distributor", "Contact Name": "Mike Johnson", "Email": "mike@primehw.com", "Phone": "555-0103"},
        {"Supplier Name": "SolarWorks Supply", "Type": "Hardware distributor", "Contact Name": "Emma Davis", "Email": "emma@solarworkssupply.com", "Phone": "555-0104"}
    ]
    with open('/Users/janasirajput/.gemini/antigravity/scratch/solar_dummy_data/suppliers.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["Supplier Name", "Type", "Contact Name", "Email", "Phone"])
        writer.writeheader()
        writer.writerows(suppliers)

    # 2. Inventory
    inventory_items = [
        "L-foot Bracket", "Aluminum Rail 10ft", "Mid Clamp", "End Clamp", "Rail Splice", 
        "Roof Attachment", "Ground Mount Post", "Wire Clip", "Grounding Lug"
    ]
    inventory = []
    for item in inventory_items:
        inventory.append({
            "Item Name": item,
            "Description": f"Standard {item.lower()} for solar racking",
            "Supplier Name": random.choice(suppliers)["Supplier Name"],
            "Quantity on Hand": random.randint(20, 200),
            "Critical Threshold": 50,
            "Unit Cost": round(random.uniform(5.0, 50.0), 2)
        })
    with open('/Users/janasirajput/.gemini/antigravity/scratch/solar_dummy_data/inventory.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["Item Name", "Description", "Supplier Name", "Quantity on Hand", "Critical Threshold", "Unit Cost"])
        writer.writeheader()
        writer.writerows(inventory)

    # 3. Projects
    statuses = ["Permitting", "Engineering", "Construction", "Completed"]
    projects = []
    now = datetime.now()
    for i in range(1, 11):
        start = random_date(now - timedelta(days=30), now + timedelta(days=30))
        end = start + timedelta(days=random.randint(14, 60))
        projects.append({
            "Project Name": f"Solar Install {['Roof', 'Ground'][random.randint(0,1)]}-{i}00",
            "Status": random.choice(statuses),
            "Location": f"{random.randint(100, 999)} Main St, Cityville",
            "Expected Start Date": start.strftime("%Y-%m-%d"),
            "Expected End Date": end.strftime("%Y-%m-%d"),
            "Manager": random.choice(["Alice Wong", "Bob Builder", "Charlie Davis"])
        })
    with open('/Users/janasirajput/.gemini/antigravity/scratch/solar_dummy_data/projects.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["Project Name", "Status", "Location", "Expected Start Date", "Expected End Date", "Manager"])
        writer.writeheader()
        writer.writerows(projects)

    # 4. Tasks
    task_types = ["Site Assessment", "Permitting", "Racking Assembly", "Panel Mounting", "Wiring & Grounding"]
    tasks = []
    for proj in projects:
        num_tasks = random.randint(2, 5)
        for _ in range(num_tasks):
            due = datetime.strptime(proj["Expected Start Date"], "%Y-%m-%d") + timedelta(days=random.randint(1, 10))
            tasks.append({
                "Task Name": random.choice(task_types),
                "Project Name": proj["Project Name"],
                "Status": random.choice(["Not Started", "In Progress", "Completed"]),
                "Assigned To": random.choice(["Tech 1", "Tech 2", "Tech 3"]),
                "Due Date": due.strftime("%Y-%m-%d")
            })
    with open('/Users/janasirajput/.gemini/antigravity/scratch/solar_dummy_data/tasks.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["Task Name", "Project Name", "Status", "Assigned To", "Due Date"])
        writer.writeheader()
        writer.writerows(tasks)
        
    # 5. Installations (optional if they use Tasks & Installations interchangeably, but I'll make a separate one just in case)
    installations = []
    for proj in projects:
        if proj["Status"] in ["Construction", "Completed"]:
            installations.append({
                "Installation ID": f"INST-{random.randint(1000, 9999)}",
                "Project Name": proj["Project Name"],
                "Install Date": proj["Expected Start Date"],
                "Installer Team": random.choice(["Alpha Team", "Bravo Team"]),
                "Status": "Completed" if proj["Status"] == "Completed" else "In Progress"
            })
    with open('/Users/janasirajput/.gemini/antigravity/scratch/solar_dummy_data/installations.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["Installation ID", "Project Name", "Install Date", "Installer Team", "Status"])
        writer.writeheader()
        writer.writerows(installations)

if __name__ == "__main__":
    main()
