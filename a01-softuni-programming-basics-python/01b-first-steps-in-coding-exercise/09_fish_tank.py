tank_lenght_in_cm = int(input())
tank_width_in_cm = int(input())
tank_height_in_cm = int(input())
filled_percentage = float(input())

tank_lenght_in_dm = 0.1 * tank_lenght_in_cm
tank_width_in_dm = 0.1 * tank_width_in_cm
tank_height_in_dm = 0.1 * tank_height_in_cm
percentage_s = 0.01 * filled_percentage

volume_tank = tank_lenght_in_dm * tank_width_in_dm * tank_height_in_dm
volume_watter = volume_tank - percentage_s * volume_tank

print(volume_watter)
