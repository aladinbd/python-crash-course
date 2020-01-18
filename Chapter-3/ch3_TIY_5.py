guest_name = ['aladin', 'noyon', 'mukta']
print(guest_name)

print(f"Our invited guests name: {guest_name[0].title()}, {guest_name[1].title()} and {guest_name[2].title()}.")
print(f"{guest_name[-1].title()} can't make the dinner.")

# replacing new name
guest_name[-1] = 'imran'
print(f"This is our new list of guest: {guest_name[0].title()}, {guest_name[1].title()} and {guest_name[2].title()}")
