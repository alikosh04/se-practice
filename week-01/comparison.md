# Week 01 — Manual vs AI: Comparison

**Name:** Kanatbek Alizhan
**Group:** Monday 16:00-19:00
**Date:** 04.10.2026

---

## 1. Facts

| | Manual (Part 1) | Rocket (Part 2) |
| --- | --- | --- |
| Language / stack used | Python | Next.js + TypeScript |
| Time to first version that ran | __ min | __ min |
| Time to all 4 test cases passing | __ min | __ min |
| Number of attempts / prompts needed | 1 main version | 1 original prompt, 2 clarification answers, 1 follow-up prompt |
| Lines of code you actually wrote | about 35 | 0 directly |
| Did it handle invalid marks (case B)? | Yes | No at first, then fixed |
| Did it handle an empty list (case D)? | Yes | Yes |
| Did it use the ≥ 50 pass threshold? | Yes | Yes |
| Output format matches the spec? | Almost, highest/lowest show .0 | Almost, average shows 71.6 instead of 71.60 |
| Can you explain every line of it? | Yes | Not every generated line |

## 2. Test results

| Case | Input | Manual output | Rocket output | Spec says | Match? |
| --- | --- | --- | --- | --- | --- |
| A | `85, 23, 45, 90, 92` | avg 67.00, high 92.0, low 23.0, pass 60.0% | avg 67.0, high 92, low 23, pass 60.0% | avg 67.00 · high 92 · low 23 · pass 60.0% | Mostly |
| B | `88, 47, -5, 101, abc, 73, 50, , 100` | avg 71.60, high 100.0, low 47.0, pass 80.0% | First: avg 65.4, low 0, pass 71.4%. After fix: avg 71.6, high 100, low 47, pass 80.0% | avg 71.60 · high 100 · low 47 · pass 80.0% | Fixed after follow-up |
| C | `10, 20, 30` | avg 20.00, high 30.0, low 10.0, pass 0.0% | avg 20.0, high 30, low 10, pass 0.0% | avg 20.00 · high 30 · low 10 · pass 0.0% | Mostly |
| D | `abc, , xyz` | No valid marks. | No marks analyzed yet | clear message, no crash | Yes |

## 3. What the AI added that I never asked for

- A full web interface using Next.js and TypeScript
- Median score, standard deviation, failed students count, score distribution and configurable pass threshold

## 4. What the AI got wrong or silently skipped

- Rocket initially clamped marks below 0 and above 100 instead of ignoring them.
- In case B it counted 7 marks instead of 5 and produced the wrong average and pass rate.
- After the fix, the calculations were correct, but the average format was still 71.6 instead of 71.60.

## 5. The defect I asked Rocket to fix

**Prompt I used:**

Fix invalid mark handling. Marks below 0 or above 100 must be ignored completely, not clamped to 0 or 100. Non-numeric and empty values must also be ignored.

**Result:** fixed

**What this tells me:**

The AI can produce a working application quickly, but it may make assumptions that are different from the specification. Testing is still necessary.

---

## 6. Reflection (200–300 words)

The AI made the development process faster because Rocket created a complete web application in a short time. It also automatically added a user interface, result cards, a pass threshold control, median, standard deviation and other statistics. I did not need to write the frontend code myself, so this saved a lot of time.

However, the AI also created a problem that looked reasonable at first. In test case B, marks below 0 and above 100 were clamped to the valid range instead of being ignored. Because of this, Rocket counted seven marks instead of five and calculated the wrong average and pass rate. I had to test the application with the provided cases to notice this problem. After I sent a follow-up prompt, Rocket fixed the invalid mark handling correctly.

I would be more confident putting my name on the manual Python version because I understand every part of it and I know why each line is there. The Rocket version looks more professional, but it contains much more generated code that I did not write myself.

This experiment showed me that a human software engineer is still responsible for checking requirements, testing edge cases, verifying AI-generated code and making sure the final result matches the specification. AI can save time, but it cannot replace careful verification.