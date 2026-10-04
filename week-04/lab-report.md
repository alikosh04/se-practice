## 1. Setup

| Field | Value |
| --- | --- |
| Name | Kanatbek Alizhan |
| Group | Monday 16:00-19:00 |
| AI assistant | ChatGPT |
| Exact model | GPT-5.6 Sol |
| Renderer | PlantUML web server |
| Behaviour diagram | sequence |
| Stories used | the reference set from README §3 |

## 2. Prompts as sent

Paste every prompt **exactly as you sent it**, in the order you sent it, one code block each.

### 2.1 Task 1 — use-case prompt

```text
Using the supplied scenario and approved stories, generate PlantUML for a use-case diagram. Include Student and Administrator outside a named system boundary. Model their goals, show justified associations, and list assumptions. Use include or extend only with a clear reason.
```

### 2.2 Task 2 — class prompt

```text
Create a UML domain class diagram in PlantUML for Smart Campus. Start with Student, Room, and Booking. Add attributes, appropriate operations, and association multiplicities. Add other classes only when requirements justify them. Explain each relationship and list assumptions. Avoid unjustified inheritance or composition.
```

### 2.3 Task 3 — behaviour prompt (3A sequence or 3B activity)

```text
Generate PlantUML for Book room. Use Student, BookingService, and BookingRepository lifelines. Validate the supplied rules, then attempt the reservation. Show a successful confirmation and an unavailable-room alternative using alt. Label messages and replies. Explain new design components and all assumptions.
```

### 2.4 Focused correction prompts (if you sent any)

```text
none
```

### 2.5 Critique prompt

```text
Compare my diagrams with the requirements. Identify missing rules, inconsistent names, and unjustified elements.
Cite each issue and propose a specific correction.
```
## 3. Task 1 — use-case review

**Assumptions the AI listed:**
- A student can cancel only their own booking.
- Administrators do not book rooms.
- Confirmation is produced only after a successful booking.
- User registration and authentication are out of scope.

| # | Element | Problem | Rule or story | Fix |
| --- | --- | --- | --- | --- |
| 1 | Receive booking confirmation | The AI modeled confirmation as a separate use case, but confirmation is an outcome of a successful booking, not a separate user goal. | R4 / US-01 | Removed the separate confirmation use case and represented R4 as a rule attached to Book room. |
| 2 | Book room | The original diagram did not visibly show the booking constraints R1–R3. | R1, R2, R3 / US-01 | Added a note to Book room showing R1, R2, R3 and R4. |

---

## 4. Task 2 — class diagram review

### 4.1 Relationships, read both ways

| Association | Read left → right | Read right → left | Multiplicities |
| --- | --- | --- | --- |
| Student — Booking | One student can have 0..* bookings. | Each booking belongs to exactly 1 student. | 1 / 0..* |
| Room — Booking | One room can have 0..* bookings. | Each booking is for exactly 1 room. | 1 / 0..* |

### 4.2 Constraints the multiplicities cannot show

- R2: A note on `Booking` states that active bookings for the same room cannot overlap.
- R3: A note on `Room` states that a blocked room cannot accept a new booking.

### 4.3 Assumptions

- A1: Blocking a room prevents new bookings, but the requirements do not specify that existing bookings are cancelled.
- A2: Touching bookings, for example one ending at 12:00 and another starting at 12:00, are assumed not to overlap.

### 4.4 Findings

| # | Element | Problem | Rule or story | Fix |
| --- | --- | --- | --- | --- |
| 1 | Student — Booking multiplicity | The AI used `1..*` for Booking, which means every student must already have at least one booking. | US-01 / US-03 | Changed the Booking end to `0..*`. |
| 2 | Room — Booking multiplicity | The AI used `1..*`, which means every room must already have at least one booking. | Scenario / US-01 | Changed the Booking end to `0..*`. |
| 3 | R2 overlap constraint | The original class diagram did not show that active bookings for the same room cannot overlap. | R2 | Added an R2 note to Booking. |

---

## 5. Task 3 — behaviour diagram review

**Option chosen and why:** 3A sequence diagram, because it clearly shows the order of validation, repository checks, booking creation and the response to the student.

**Design components added beyond the domain model:**
- `BookingService` — coordinates validation and the booking process.
- `BookingRepository` — checks room state and existing bookings and saves a successful booking.

| # | Element | Problem | Rule or story | Fix |
| --- | --- | --- | --- | --- |
| 1 | checkAvailability / saveBooking | The original sequence attempted saving without showing separate validation of R1, R2 and R3. | R1, R2, R3 / US-01 | Added time validation, blocked-room check and overlapping-booking check before saveBooking. |
| 2 | room unavailable branch | The original unavailable branch was placed after the successful save flow, making the order unclear. | R2, R3 | Moved all failure alternatives before booking creation so nothing is saved when a rule fails. |
| 3 | booking confirmation | The original confirmation was not explicitly tied to R4. | R4 / US-01 | Labeled the successful response `booking confirmation (R4)` after the booking is saved. |

## 6. AI critique

| # | Issue the AI raised | Element it cited | Verdict | Why |
| --- | --- | --- | --- | --- |
| 1 | R2 and R3 were not explicitly traced in the sequence | isRoomBlocked and hasOverlappingBooking | reject | My current revised sequence already labels the checks with R3 and R2, so this referred to an older version. |
| 2 | The two undecided assumptions were missing | Class diagram assumptions | accept | The requirements say these cases must be declared. I added assumptions for touching bookings and existing bookings when a room is blocked. |
| 3 | bookRoom() had inconsistent ownership | Student.bookRoom() and BookingService | accept | Booking coordination belongs to BookingService in the sequence, so I removed bookRoom() from the Student domain class. |
| 4 | Room.capacity was not justified | Room.capacity | accept | The supplied scenario does not mention capacity, so I removed the attribute. |
| 5 | Administrator was unnecessary in the domain class diagram | Administrator class | accept | Administrator is needed as a use-case actor, but it was not required as a persistent domain class. |

## 7. Consistency table

| Requirement / story | Use-case diagram | Class diagram | Sequence diagram |
| --- | --- | --- | --- |
| US-01 Book room | Book room | Student, Room, Booking | bookRoom flow |
| US-02 View room availability | View room availability | Room | — |
| US-03 Cancel own booking | Cancel own booking | Booking.cancel() | — |
| US-04 Block room | Block room | Room.blocked | isRoomBlocked() |
| US-05 Unblock room | Unblock room | Room.blocked | — |
| US-06 Review room usage | Review room usage | — | — |
| R1 Future start and duration <= 2 hours | Note on Book room | Booking start/end time | validate time range (R1) |
| R2 No overlapping active bookings | Note on Book room | R2 note on Booking | hasOverlappingBooking() (R2) |
| R3 Blocked room cannot accept booking | Note on Book room | R3 note on Room | isRoomBlocked() (R3) |
| R4 Successful booking gives confirmation | Note on Book room | — | booking confirmation (R4) |

---

## 8. Change log

| Diagram | Original problem | Change made |
| --- | --- | --- |
| Use-case | Booking confirmation was modeled as a separate user goal. | Removed the separate confirmation use case and represented R4 as a booking outcome. |
| Class | Student and Room used `1..*` Booking multiplicities. | Changed both Booking ends to `0..*` and added R2/R3 constraint notes. |
| Sequence | The original flow saved a booking before clearly validating R1, R2 and R3. | Added validation in order R1 → R3 → R2 and moved saveBooking after all checks. |
| Class | `Student.bookRoom()` conflicted with BookingService ownership in the sequence. | Removed `bookRoom()` from Student. |
| Class | `Room.capacity` was not supported by the supplied requirements. | Removed the capacity attribute. |
| Class | The Administrator class was isolated and unnecessary in the domain model. | Removed Administrator from the class diagram. |
| Class | The two undecided booking assumptions were not declared. | Added assumptions about touching bookings and existing bookings when a room is blocked. |

## 9. Checker output

```text
Week 04 structural check - shape only, never quality

UC1  PASS  Student and Administrator declared
UC2  PASS  named system boundary: "Smart Campus System"
UC3  PASS  all actors declared outside the boundary
UC4  PASS  all scenario goals present (6 use cases)
UC5  PASS  no actor is associated with a confirmation use case
UC6  PASS  actor responsibilities match the scenario
UC7  PASS  use cases are goals, not screens or components
UC8  PASS  every include / extend / generalization carries a ' why: comment (or there are none)
UC9  PASS  revised diagram differs from the AI's original
CL1  PASS  Student, Room and Booking present
CL2  PASS  Booking is associated with Student and with Room
CL3  PASS  every association has multiplicities at both ends
CL4  PASS  1 student / 1 room per booking, 0..* bookings per student and per room
CL5  PASS  every inheritance / composition / aggregation carries a ' why: comment (or there are none)
CL6  PASS  only domain concepts in the class diagram
CL7  PASS  attributes needed by R1-R3 are present
CL8  PASS  a note states R2 (no overlapping active bookings)
SQ1  PASS  Student, BookingService and BookingRepository lifelines present
SQ2  PASS  alt block with a guard on every branch (6 branches)
SQ3  PASS  validation happens before creation
SQ4  PASS  nothing is saved on a failure branch
SQ5  PASS  every message is labelled
SQ6  PASS  R1 (time range) is visible - checked or stated as a precondition
SQ7  PASS  R3 (blocked room) is visible
FI1  PASS  the AI's original output is kept for every diagram
FI2  PASS  a rendered image for every diagram
LR1  PASS  §1 setup filled (tool and model recorded)
LR2  PASS  5 prompts pasted in §2
LR3  PASS  2 use-case findings in §3
LR4  PASS  §4 relationships read both ways, 2 assumption(s) declared
LR5  PASS  3 behaviour-diagram findings in §5
LR6  PASS  5 critique issues with a verdict
LR7  PASS  7 change-log rows covering all three diagrams
CS1  PASS  6 approved stories
CS2  PASS  §7 traces R1-R4 into the diagrams
CS3  PASS  every use case traces to an approved story
CS4  PASS  every lifeline is a domain class or an explained design component

SUMMARY pass=37 fail=0 error=0
A FAIL you report and explain in lab-report.md §9 costs you nothing. One you hide costs the criterion.

## 10. Conclusion (120–180 words)

The class diagram was the diagram where the AI made the most important mistakes. In the original version, the Booking end of the Student–Booking and Room–Booking associations used `1..*`, which would mean that every student and every room must already have at least one booking. I corrected both multiplicities to `0..*`. I also added the R2 constraint as a note because overlapping bookings cannot be represented by multiplicity.

The sequence diagram also needed revision because the original flow did not clearly validate R1, R2 and R3 before saving a booking. I changed the order so that the system checks the time range, blocked-room status and overlapping bookings before `saveBooking()`.

The critique also helped identify unjustified elements such as `Room.capacity` and inconsistent ownership of `bookRoom()`. It also showed that AI feedback must be checked carefully, because one critique point referred to an older version of the sequence diagram. Overall, AI was useful for drafting, but human review was necessary to make the diagrams consistent and correct.