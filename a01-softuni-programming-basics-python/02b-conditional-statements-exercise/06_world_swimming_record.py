current_record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds = float(input())

delay = distance_in_meters // 15 * 12.5

new_record_in_seconds = distance_in_meters * time_in_seconds + delay

if new_record_in_seconds < current_record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {new_record_in_seconds:.2f} seconds.")

else:
    print(f"No, he failed! He was {new_record_in_seconds-current_record_in_seconds:.2f} seconds slower.")
