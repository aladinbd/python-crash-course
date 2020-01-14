guest_name = ['aladin', 'noyon', 'mukta']
print(guest_name)

print(f"Our invited guests name: {guest_name[0].title()}, {guest_name[1].title()} and {guest_name[2].title()}.")
print(f"{guest_name[-1].title()} can't make the dinner.")

# replacing new name
guest_name[-1] = 'imran'
print(f"This is our new list of guest: {guest_name[0].title()}, {guest_name[1].title()} and {guest_name[2].title()}")

# adding new guest to the beginning by inser() method
guest_name.insert(0, 'alamin')
print(guest_name)

# adding new guest to the middle by insert() method
guest_name.insert(1, 'rajon')
print(guest_name)

# Appending new geest
guest_name.append('hridoy')
print(guest_name)

print(f"{guest_name[0].title()}, {guest_name[1].title()}, {guest_name[2].title()}, {guest_name[3].title()}, {guest_name[4].title()}, {guest_name[5].title()},")
