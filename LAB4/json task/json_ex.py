import json
with open("sample-data.json") as file:
    data = json.load(file)
print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<7} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 50 + " " + "-" * 20 + " " + "-" * 7 + " " + "-" * 6)
for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes.get("dn", "N/A")
    description = attributes.get("descr", "") 
    speed = attributes.get("speed", "inherit")  
    mtu = attributes.get("mtu", "N/A")
    print("{:<50} {:<20} {:<7} {:<6}".format(dn, description, speed, mtu))

