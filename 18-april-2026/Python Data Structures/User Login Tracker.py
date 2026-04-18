logins = [("Rahul", "10:00"), ("Sneha", "10:10"), ("Rahul", "11:00"), ("Arjun", "11:15"), ("Sneha", "11:30")]
tracker = {}

for name, time in logins:
    tracker[name] = tracker.get(name, 0) + 1

print(tracker)