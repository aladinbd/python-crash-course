alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original Position: {alien_0['x_position']}")

# Move the alien to the right
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increament = 1
elif alien_0['speed'] == 'medium':
    x_increament = 2
else:
    # This must be fast alien
    x_increament = 3

# The new Position is the old position plus the increament
alien_0['x_position'] = alien_0['x_position'] + x_increament

print(f"New position: {alien_0['x_position']}")
