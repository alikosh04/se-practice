marks = [75, 88, 49, 100, -5, 101, "abc", "", 50]

valid_marks = []

for mark in marks:
    try:
        number = float(mark)

        if 0 <= number <= 100:
            valid_marks.append(number)

    except (ValueError, TypeError):
        pass

if len(valid_marks) == 0:
    print("No valid marks.")
else:
    count = len(valid_marks)
    average = sum(valid_marks) / count
    highest = max(valid_marks)
    lowest = min(valid_marks)

    passed = 0

    for mark in valid_marks:
        if mark >= 50:
            passed += 1

    pass_rate = passed / count * 100

    print("Valid marks:", count)
    print(f"Average: {average:.2f}")
    print("Highest:", highest)
    print("Lowest:", lowest)
    print(f"Pass rate: {pass_rate:.1f}%")