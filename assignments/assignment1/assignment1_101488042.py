# Kiana Nezafat Yazdi 101488042
#Assignment: #1

#String(str)
gym_member = "Alex Alliton"
#float
preferred_weight_kg = 20.5
#int
highest_reps = 25
#bool
membership_active = True

#Dictionary
#key : String , Values: Tuple containing three int for yoga , running , weight lifting
workout_stats={
    "Alex" : (30, 80, 20) , #yoga : 30 , running :80 , weightlifting: 20
    "Jamie" : (20, 50, 10) , #yoga : 20 , running :50 , weightlifting: 10
    "Taylor" : (45, 10, 15) } #yoga : 45 , running :10 , weightlifting: 15

# Calculate total workout minutes for each friend and add new key-value pairs
total_workout_minutes = {}
for friend, activities in workout_stats.items():
    total_minutes = sum(activities)
    total_workout_minutes[f"{friend}_Total"] = total_minutes



# nested list: each row represents a friend, each column an activity
#List of lists
workout_list = [
    list(workout_stats[friend]) for friend in workout_stats.keys()
]
print("Workout List:" ,workout_list)

# Extract and print the minutes for yoga and running for all friends
yoga_running_minutes = [row[:2] for row in workout_list]
print("Yoga and Running Minutes for All Friends:", yoga_running_minutes)

# Extract and print the minutes for weightlifting for the last two friends
weightlifting_last_two = [row[2] for row in workout_list[-2:]]
print("Weightlifting Minutes for Last Two Friends:", weightlifting_last_two)


# Use an if-statement within a loop to check for total workout minutes >= 120
for friend, total in total_workout_minutes.items():
    if total >= 120:
        friend_name = friend.replace("_Total", "")
        print(f"Great job staying active, {friend_name}!")

# Allow user to input a friend's name and display workout information
friend_name_input = input("Enter a friend's name to check their workout records: ")
friend_name_input =friend_name_input.capitalize()
if friend_name_input in workout_stats:
    activities = workout_stats[friend_name_input]
    total_minutes = total_workout_minutes.get(f"{friend_name_input}_Total", 0)
    print(f"""{friend_name_input}'s workout minutes:
Yoga: {activities[0]}
Running: {activities[1]}
Weightlifting: {activities[2]}""")
    print(f"Total workout minutes: {total_minutes}")
else:
    print(f"Friend {friend_name_input} not found in the records.")

# Find the friend with the highest and lowest total workout minutes
max_friend = max(total_workout_minutes, key=total_workout_minutes.get)
min_friend = min(total_workout_minutes, key=total_workout_minutes.get)

print(f"Friend with the highest total workout minutes: {max_friend} ({total_workout_minutes[max_friend]} minutes)")
print(f"Friend with the lowest total workout minutes: {min_friend} ({total_workout_minutes[min_friend]} minutes)")