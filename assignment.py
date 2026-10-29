def replace_value(values, index, new_value):
    values[index] = new_value

def find_first(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i    
    return -1  

def summarize(values):
    return (min(values), max(values), sum(values))     

days = int(input("Enter the number of days: "))
original = []
for _ in range(days):
    emails = int(input("Enter the number of emails received: "))
    original.append(emails) 
    
    updated = original[:]

    index_to_correct = int(input("Enter the index to correct: "))
new_emails = int(input("Enter the new number of emails: "))
replace_value(updated, index_to_correct, new_emails)

target = int(input("Enter the number of emails to search for: "))

found_index = find_first(updated, target)
target_count = updated.count(target)
minimum, maximum, total = summarize(updated)
sorted_list = sorted(updated)

print()
print(f"Original list: {original}")
print(f"Updated list: {updated}")
print(f"Sorted list: {sorted_list}")
print(f"Smallest: {minimum}, Largest: {maximum}, Total: {total}")

if found_index == -1:
    print("Target index: Target not found")
else:
    print(f"Target index: {found_index}")

print(f"Target count: {target_count}")
