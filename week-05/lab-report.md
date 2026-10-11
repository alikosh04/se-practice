# Week 05 — Lab report

**Name:** Kanatbek Alizhan
**Group:** Monday 16:00-19:00
**Date:** 11.10.2026

Fill in every section. **Do not delete, rename or renumber the headings** — the checker and the
grader find your answers by them. Add rows to any table; never remove its header.

---

## 1. Setup

| | |
| --- | --- |
| Assistant (tool) | ChatGPT |
| **Exact** model name | GPT-6 |
| Language and version | Python 3 |
| Path | A |
| My Week 04 declaration for touching bookings | allowed |

<!-- If your Week 04 model said touching bookings are NOT allowed: AC4 now says they are.
     One sentence here on what that changes in your Week 04 diagrams. This is a finding, not a penalty. -->

---

## 2. Task 1 — the plan

**The assistant's plan, pasted unedited:**

```text
1. Check that 0 <= start < end <= 1440 and start > now.
   Return False if the requested time is invalid (AC1).

2. Check that the duration end - start is at most 120 minutes.
   Return False if it is longer (AC2).

3. Check whether the room is blocked.
   Return False if blocked is True (AC3).

4. Check every existing booking (a, b).
   If start < b and end > a, the intervals overlap.
   Return False if any overlap is found (AC4).

5. Return True if all checks pass.
   Do not modify the existing bookings list (AC5).

Assumptions:
- now is valid.
- blocked is Boolean.
- existing contains valid booking intervals.

Boundary cases:
- A booking starts exactly at now.
- A booking lasts exactly 120 minutes.
- A booking lasts 121 minutes.
- Two bookings touch at their endpoints.
- A booking overlaps another booking.
- A booking has zero or negative duration.
- A booking ends exactly at minute 1440.
- A booking starts before minute 0.
- The room is blocked.
- The existing bookings list is empty.
- The existing bookings list remains unchanged. ```

**What the plan invented or changed.** One row for every rule in the plan that is not in the
contract or in AC1–AC5, or that says something different from them. If you found none, write one
row saying which lines of the plan you checked against which AC.

| # | What the plan said | What the contract or the AC says | What I did |
| --- | --- | --- | --- |
| 1 | No additional rules were introduced. | Checked steps 1–5 against AC1–AC5. | Kept the plan unchanged. |

**Boundary cases the assistant suggested that I kept as tests:**

- Touching endpoints, exactly 120 minutes, 121 minutes, starts now, zero-length interval, day bounds, blocked room, empty existing bookings, and unchanged input.

---

## 3. Task 2 — the first version (v1), read before it was run

v1 is saved as `code/original/booking_v1.<ext>`, exactly as the assistant returned it: yes

**AC map.** One row per condition in v1. Quote the line.

| # | Line in v1 | AC it implements | Correct as written? If not, why |
| --- | --- | --- | --- |
| 1 | `if not (0 <= start < end <= 1440):` | AC1 | Yes, checks valid time boundaries. |
| 2 | `if start <= now:` | AC1 | Yes, booking must start after now. |
| 3 | `if end - start > 120:` | AC2 | Yes, rejects bookings longer than 120 minutes. |
| 4 | `if blocked:` | AC3 | Yes, rejects blocked rooms. |
| 5 | `if start < b and end > a:` | AC4 | Yes, rejects overlapping bookings and allows touching endpoints. |
| 6 | `return True` | AC5 | Yes, only after all checks pass. |

**Anything in v1 that no AC asks for** (extra validation, a buffer between bookings, logging,
saving the booking, a different return type):

- None. The function follows AC1–AC5 without adding extra rules.

---

## 4. Task 3 — my tests

Base input for every row unless the row says otherwise: `now=540, blocked=False, existing=[(600, 660)]`.

| # | Test name | Request (start, end) | What differs from the base input | Expected | AC | Result on v1 | Result on final |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | test_touching_end_is_allowed | (660, 720) | None | True | AC4 | PASS | PASS |
| 2 | test_overlap_is_rejected | (630, 690) | None | False | AC4 | PASS | PASS |
| 3 | test_blocked_room_is_rejected | (660, 720) | blocked=True | False | AC3 | PASS | PASS |
| 4 | test_exactly_two_hours_allowed | (720, 840) | None | True | AC2 | PASS | PASS |
| 5 | test_over_two_hours_rejected | (720, 841) | None | False | AC2 | PASS | PASS |
| 6 | test_starts_now_rejected | (540, 570) | None | False | AC1 | PASS | PASS |
| 7 | test_zero_length_rejected | (700, 700) | existing=[] | False | AC1 | PASS | PASS |
| 8 | test_reversed_times_rejected | (750, 700) | existing=[] | False | AC1 | PASS | PASS |
| 9 | test_negative_start_rejected | (-1, 60) | now=0, existing=[] | False | AC1 | PASS | PASS |
| 10 | test_end_of_day_allowed | (1380, 1440) | existing=[] | True | AC1 | PASS | PASS |
| 11 | test_after_end_of_day_rejected | (1400, 1441) | existing=[] | False | AC1 | PASS | PASS |
| 12 | test_empty_existing_allowed | (700, 760) | existing=[] | True | AC4 | PASS | PASS |
| 13 | test_multiple_existing_bookings | (740, 800) | existing has 3 bookings | False | AC4 | PASS | PASS |
| 14 | test_existing_is_unchanged | (660, 720) | Checks list after call | True | AC5 | PASS | PASS |
| 15 | test_inside_existing_rejected | (615, 645) | None | False | AC4 | PASS | PASS |
| 16 | test_contains_existing_rejected | (570, 690) | None | False | AC4 | PASS | PASS |
| 17 | test_touching_start_allowed | (570, 600) | None | True | AC4 | PASS | PASS |
| 18 | test_returns_real_boolean | (700, 760) | existing=[], checks type | bool | AC5 | PASS | PASS |
| 19 | test_rejected_result_is_real_boolean | (630, 690) | Checks exact False | False | AC5 | PASS | PASS |
| 20 | test_blocked_result_is_real_boolean | (700, 760) | blocked=True, existing=[] | False | AC5 | PASS | PASS |
| 21 | test_existing_unchanged_after_rejection | (630, 690) | existing has 2 bookings | False | AC5 | PASS | PASS |
| 22 | test_existing_unchanged_with_multiple_bookings | (800, 860) | existing has 3 bookings | True | AC5 | PASS | PASS |
| 23 | test_empty_existing_remains_empty | (700, 760) | existing=[] | True | AC5 | PASS | PASS |
| 24 | test_rejected_result_has_bool_type | (630, 690) | Checks exact type | bool | AC5 | PASS | PASS |

---

## 5. Task 4 — debugging with evidence

One row per defect you found — in v1, in a later version, or in your own tests. If v1 passed
everything, the row is the **new edge case you added**, with expected and actual equal, and the
cause column says why no change was needed.

| # | Input (the full call) | Expected | Actual | Cause (quote the line) | Fix | Who proposed the fix |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `can_book(700, 760, 540, False, [])` | `True` | `True` | No bug found; the original code passed this case. | No fix needed | No fix proposed |
**The debug prompt I sent, and the assistant's answer** (leave the block empty if you did not use it):

```text
```

---

## 6. Task 5 — the critique

**The assistant's critique, pasted unedited:**

```text
1. No functional defects found under the stated input contract. The implementation correctly checks time boundaries, future start, maximum duration, blocked rooms, and booking overlaps.

2. The condition `start < b and end > a` correctly allows bookings that touch at their endpoints. No change is needed under AC4.

3. The function does not explicitly check input types. However, the contract guarantees integer times and valid existing bookings, so this is not a violation of AC1–AC5.
```

| # | Suggestion | accept / reject | Reason — cite the AC or the contract line | Suite after the change |
| --- | --- | --- | --- | --- |
| 1 | Keep the implementation because no functional defects were found | accept | AC1–AC5 are satisfied; F1–F10 passed. | 24 tests OK; M10 FAIL |
| 2 | Keep the strict overlap condition | accept | AC4 allows touching endpoints without overlap. | 24 tests OK; M10 FAIL |
| 3 | Add explicit input type validation | reject | The contract guarantees integer times, so this is outside the required scope. | 24 tests OK; M10 FAIL |

---

## 7. Change log — v1 to final

| # | What changed (the line, before → after) | Why | Evidence: the test or check that moved |
| --- | --- | --- | --- |
| 1 | No changes to booking.py | The first AI-generated version passed all F1–F10 functional checks. I kept the original implementation and added more tests instead. | AC1–AC5 |
---

## 8. Evidence — real output

### 8.1 My suite, final run

Paste the **complete** terminal output. For Python: everything `python -m unittest -v` printed.

```text
test_after_end_of_day_rejected (test_booking.BookingTests.test_after_end_of_day_rejected) ... ok
test_blocked_result_is_real_boolean (test_booking.BookingTests.test_blocked_result_is_real_boolean) ... ok
test_blocked_room_is_rejected (test_booking.BookingTests.test_blocked_room_is_rejected) ... ok
test_contains_existing_rejected (test_booking.BookingTests.test_contains_existing_rejected) ... ok
test_empty_existing_allowed (test_booking.BookingTests.test_empty_existing_allowed) ... ok
test_empty_existing_remains_empty (test_booking.BookingTests.test_empty_existing_remains_empty) ... ok
test_end_of_day_allowed (test_booking.BookingTests.test_end_of_day_allowed) ... ok
test_exactly_two_hours_allowed (test_booking.BookingTests.test_exactly_two_hours_allowed) ... ok
test_existing_is_unchanged (test_booking.BookingTests.test_existing_is_unchanged) ... ok
test_existing_unchanged_after_rejection (test_booking.BookingTests.test_existing_unchanged_after_rejection) ... ok
test_existing_unchanged_with_multiple_bookings (test_booking.BookingTests.test_existing_unchanged_with_multiple_bookings) ... ok
test_inside_existing_rejected (test_booking.BookingTests.test_inside_existing_rejected) ... ok
test_multiple_existing_bookings (test_booking.BookingTests.test_multiple_existing_bookings) ... ok
test_negative_start_rejected (test_booking.BookingTests.test_negative_start_rejected) ... ok
test_over_two_hours_rejected (test_booking.BookingTests.test_over_two_hours_rejected) ... ok
test_overlap_is_rejected (test_booking.BookingTests.test_overlap_is_rejected) ... ok
test_rejected_result_has_bool_type (test_booking.BookingTests.test_rejected_result_has_bool_type) ... ok
test_rejected_result_is_real_boolean (test_booking.BookingTests.test_rejected_result_is_real_boolean) ... ok
test_returns_real_boolean (test_booking.BookingTests.test_returns_real_boolean) ... ok
test_reversed_times_rejected (test_booking.BookingTests.test_reversed_times_rejected) ... ok
test_starts_now_rejected (test_booking.BookingTests.test_starts_now_rejected) ... ok
test_touching_end_is_allowed (test_booking.BookingTests.test_touching_end_is_allowed) ... ok
test_touching_start_allowed (test_booking.BookingTests.test_touching_start_allowed) ... ok
test_zero_length_rejected (test_booking.BookingTests.test_zero_length_rejected) ... ok

----------------------------------------------------------------------
Ran 24 tests in 0.000s

OK
```

### 8.2 The checker, final run

Paste the **complete** output of `python tests/check_booking.py`. Paste it **last**: if you edit
this file afterwards, run the checker again and paste again.

```text
(paste here)
```

### 8.3 Path B only — three faults I planted myself

Break your own function on purpose, one line at a time, run your suite, restore the line.

| # | Line I changed (before → after) | AC it breaks | Test that failed |
| --- | --- | --- | --- |
| 1 | | | |
| 2 | | | |
| 3 | | | |

The three failing runs (Path A students leave this block empty):

```text
```

---

## 9. What still fails, and what the contract does not say

### 9.1 Checks I am keeping as FAIL or ERROR

The same IDs as `known_fails` in `submission.yml`. Write `none` if the run is clean.

| Check | Why it stays |
| --- | --- |
| | |

### 9.2 Outside the contract

The contract says times are integers. It does not say what `can_book` does when one is not —
`600.5`, or the string `"600"`. What does **your** function do, and why is that the right call?

-

### 9.3 A bound that never decides

One of the bounds written in AC1 can never be the *only* reason a request is rejected. Which one,
and why?

-

---

## 10. Conclusion (120–180 words)

<!-- Answer all three, in your own words, without the assistant:
     (a) Explain the overlap condition in your final code — why those two comparisons, and why
         they let touching bookings through.
     (b) Which fault did your tests miss the longest, and what did the missing test have in common
         with the ones you already had?
     (c) What did you have to decide that neither the contract nor the assistant decided for you?
     Worthless: "the AI made a mistake and I fixed it."
     Worth everything: "F7 failed on can_book(570, 600, ...): v1 compared with <= on the start
     side, so a booking that ends exactly when another begins was rejected." -->

<!-- Write your conclusion below this line -->
In this practice, I used ChatGPT to create a Python function called `can_book`. The function checks if a student can book a study room. It checks the start and end time, the maximum booking duration of 120 minutes, whether the room is blocked, and whether the new booking overlaps with an existing one.

I learned how to check overlapping bookings using the condition `start < b and end > a`. This condition allows two bookings to touch at their endpoints without overlapping. For example, one booking can end at 600 and another can start at 600.

I created 24 unit tests, and all of them passed. The checker detected nine faulty implementations, but M10 was not detected by my tests. I tried adding more tests for Boolean results and unchanged input lists. This practice showed me that AI can help write code, but I still need to check its suggestions, choose useful test cases, and understand the results myself.