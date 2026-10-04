Original prompt:
Build a small program that processes a list of student marks and prints:
average, highest, lowest, and pass rate.

Rocket question:
How will student marks be entered into the app?

My answer:
Paste a list at once

Rocket question 2:
Who will be using this tool?

My answer:
A teacher or lecturer

Rocket enhanced prompt:

A clean web tool for teachers to process student marks by pasting a list of scores all at once. The app instantly calculates and displays the class average, highest and lowest marks, and pass rate — giving a clear, at-a-glance summary of class performance.

Building with Next.js and TypeScript.

What Rocket added by itself:
- A web interface
- Target user: teachers
- Paste a list of scores at once
- Class performance summary
- Next.js
- TypeScript

Test B:
Input: 88, 47, -5, 101, abc, 73, 50, , 100

Rocket output:
Total students: 7
Average: 65.4
Highest: 100
Lowest: 0
Pass rate: 71.4%

Expected:
Valid marks: 5
Average: 71.60
Highest: 100
Lowest: 47
Pass rate: 80.0%

Result: FAIL

Problem:
Rocket did not ignore all invalid marks. Values below 0 and above 100 were treated as valid/clamped values.

Test D:
Input: abc, , xyz
Result: PASS
Rocket showed a clear no-marks message and did not crash.

Follow-up prompt:
Fix invalid mark handling. Marks below 0 or above 100 must be ignored completely, not clamped to 0 or 100. Non-numeric and empty values must also be ignored.

Follow-up result:
Fixed.

Rocket now ignores marks below 0 and above 100.

Retest B:
Total students: 5
Average: 71.6
Highest: 100
Lowest: 47
Pass rate: 80.0%

The calculation is correct, but the average is shown with one decimal instead of two.