from collections import Counter

with open('logins.txt', 'r') as f:
    logins = [line.strip() for line in f]

print("All names:", logins)
print("Total records:", len(logins))
counts = Counter(logins)
print("Logins per user:", dict(counts))

most_frequent = counts.most_common(1)[0][0]
print("User with most logins:", most_frequent)


print("Unique users:", list(set(logins)))