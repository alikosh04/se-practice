# SIS #01 — Software Engineering Fundamentals, With an AI in the Loop

<!--
  This is the only file you write your report in. README.md tells you what goes where.

  Rules the checker relies on:
  - Do not delete, rename or renumber the ## headings, the ### headings, or the **Label:** words.
  - Replace every "(write here)" and "(paste here)". None may be left when you submit.
  - Comments like this one are ignored by the word counter. Delete them or leave them.
-->

**Topic:** 1.7

<!-- Exactly one of 1.1 … 1.10, e.g.  **Topic:** 1.4  -->

---

## 1. Scenario

<!-- 100–150 words, labels included. One small scenario, used in every prompt and in your
     whole answer. Anything fictional is labelled in Assumptions. -->

**Question:** (How can a small student development team work together effectively using GitHub?)

**Users:** (Four university students who are developing a study room booking application.)

**Problem:** (The students work on different parts of the application. Sometimes they change the same files, which can cause conflicts and mistakes. They need a simple way to organize teamwork.)

**Constraints:** (1. The team has only four weeks to finish the project.
2.All team members have limited experience with GitHub and software development.)

**Risk:** (Two students may change the same code and accidentally introduce errors when merging their work.)

**Assumptions:** (This is a fictional university project. The team consists of four students. They use GitHub and VS Code. They communicate through Telegram and have one meeting every week. The application allows students to view available rooms and book them.)

## 2. Analysis

Connected development teams use online tools to work together on software projects. In our scenario, four university students need to develop a study room booking application. GitHub can help them organize their work, share code, and track changes. However, using GitHub alone does not guarantee successful teamwork. Students also need clear responsibilities, communication, and testing.

The first important engineering decision is to divide the project into smaller tasks. One student can work on the user interface, another on room information, another on booking functionality, and the fourth on testing and integration. This approach gives every student a clear responsibility. However, the tasks may depend on each other. For example, the booking feature needs room information. Therefore, the team should agree on the basic data structure before starting development.

The second decision is to use separate Git branches. Each student can create a branch for their task instead of changing the main branch directly. After finishing a feature, the student can create a Pull Request. Another team member should review the changes before merging them. This process can help identify mistakes and explain how the code works. The disadvantage is that reviewing changes takes time. Since the team has only four weeks, reviews should be simple and focused on important problems.

Communication is another important part of connected development. The students can use Telegram for daily questions and organize one meeting every week. During meetings, they can discuss progress, problems, and upcoming tasks. However, Telegram messages can become difficult to find. Important decisions should also be written in GitHub issues or project documentation.

Testing is necessary because different parts of the application must work together. The team should check whether students can view available rooms, create bookings, and avoid overlapping reservations. They should also test the application after merging changes. Testing requires additional effort, but finding problems before submission is better than discovering them during the demonstration.

There is also a trade-off between speed and quality. Working independently may help students finish individual tasks faster, but it increases the need for integration. Too many rules can slow down inexperienced developers. A simple workflow with small tasks, branches, Pull Requests, and basic testing is more appropriate for this project.

Overall, connected development tools can support teamwork when students use them consistently. The team should focus on simple processes rather than complicated tools.


## 3. Review

<!-- 250–300 words. What Prompt B's critique said and what you did with it; your two source
     checks and your two substantive revisions, each with a reason. Point at the rows of the
     tables in section 9 ("verification row 2", "change-log row 1"). -->

The AI critique identified seven issues in the original draft. I reviewed each point and decided whether to accept or qualify it based on the fictional project's requirements.

First, I accepted the task coordination criticism because the booking feature depends on room information. The team should agree on shared interfaces before development. Second, I accepted the warning about Git branches. Separate branches support independent work, but they do not guarantee successful integration.

Third, I qualified the claim about Pull Request reviews. Reviews allow students to discuss code and suggest improvements, but inexperienced reviewers may still miss bugs. Fourth, I accepted the communication criticism because important technical decisions should be documented in GitHub rather than stored only in Telegram.

Fifth, I accepted the testing criticism and added specific cases for successful bookings, overlapping reservations, and invalid requests. Sixth, I accepted the deadline concern because complicated processes could waste time during a four-week project. Seventh, I accepted the need for external verification instead of relying only on AI explanations.

For verification row 1, the official Git documentation explains how branches support separate development histories. This supports the basic claim but does not prove that merging always succeeds. For verification row 2, GitHub documentation describes comments, approvals, and requests for changes during Pull Request reviews. However, these features do not guarantee better software quality.

I made two important revisions. Change-log row 1 adds shared interfaces before coding to reduce integration problems. Change-log row 2 adds a review checklist and concrete booking tests because the original recommendations were too general.

I also challenged the idea that code reviews automatically improve quality. Their usefulness depends on the reviewers' knowledge and the team's practices. The final approach is therefore simple, practical, and suitable for students with limited experience.

## 4. Conclusion

For this fictional student project, I recommend using GitHub as the main development platform. The four students should divide responsibilities, create separate branches, review Pull Requests, and test important functions before merging changes. Telegram can support communication, while GitHub can store technical decisions and project tasks.

This approach is suitable because the team has limited time and limited experience. It does not require complicated software or expensive tools. The students can learn how professional development teams cooperate while completing their application.

The main limitation is that teamwork still depends on the students. GitHub cannot prevent every mistake or solve communication problems automatically. Team members must follow their agreed process and help each other when difficulties appear. Simple rules and regular communication are more useful than unnecessary complexity.


## 5. Reflection

<!-- 150–200 words. NOT part of the main total. Written by you, not by the assistant:
     what helped, what you changed, what you learned. Specific beats flattering. -->

During this assignment, I learned more about how software development teams can work together using GitHub and AI tools. At first, I thought that dividing tasks and using separate branches would be enough for successful teamwork. However, after reviewing the AI responses, I understood that communication and integration are also important.

I created the sis-01 branch in my GitHub repository and made commits before working with AI. This helped me understand why version control is useful for tracking changes. I also learned that Git branches allow developers to work separately, but they do not prevent every integration problem.

Prompt B was especially useful because it identified weaknesses in the first draft. For example, the original explanation did not include enough details about testing and Pull Request reviews. I decided to add specific booking test cases and a simple review checklist.

I also learned that AI-generated information should not be accepted without checking reliable sources. In the future, I will use AI to generate ideas and review my work, but I will make the final decisions myself.

## 6. References

<!-- Full references, one per line, each starting with "- ". Only sources you actually opened.
     Every URL used in the verification table must also appear here. Example:
     - Sommerville, I. (2016). Software Engineering, 10th ed., Global Edition. Pearson. Ch. 1.
-->

- Chacon, S., & Straub, B. *Pro Git*, 2nd edition. Section 3.1, "Git Branching — Branches in a Nutshell." https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell (accessed 2026-10-11).

- GitHub Docs. "Pull request reviews." https://docs.github.com/en/pull-requests/reference/pull-request-reviews (accessed 2026-10-11).

## 7. Appendix A — Initial outline

<!-- Written BEFORE you run Prompt A. Five points, your own words, numbered. These are the
     "five points" you paste into Prompt A. -->

1. (Each student should have their own tasks in the project.)
2. (We should use GitHub to save and share our code.)
3. (Each student should work in a separate Git branch.)
4. (The team should communicate through Telegram and discuss problems)
5. (We should test the application before finishing the project)

## 8. Appendix B — AI exchanges

<!-- Complete prompts and complete responses, as text — never screenshots. Paste each inside
     the fenced block that follows its label. If a response itself contains ``` lines, open
     and close that block with ~~~~ instead. You may add B4, B5 … after B3 if you ran more. -->

### B1 — Draft (Prompt A)

- **Tool:** ChatGPT
- **Model:** GPT-6
- **Date:** 2026-10-11
- **Purpose:** contextual draft

<!-- Model: the exact model with its version, as the tool shows it (e.g. "GPT-5 Thinking",
     "Claude Sonnet 4.5"). If the tool does not show it, write: not displayed
     Date: YYYY-MM-DD -->

**Prompt:**

```text
Act as a software engineering tutor. Help me analyze topic 1.7 — Connected Development Teams: How can a small student development team work together effectively using GitHub? for a first-year-level university assignment.

My scenario is four university students developing a study room booking application. They sometimes change the same files, causing conflicts and mistakes. They have four weeks to finish the project and limited experience with GitHub and software development. The main risk is introducing errors when merging code. This is a fictional university project. My initial ideas are 1. Each student should have their own tasks in the project. 2. We should use GitHub to save and share our code. 3. Each student should work in a separate Git branch. 4. The team should communicate through Telegram and discuss problems. 5. We should test the application before finishing the project. Draft a 400–500 word explanation using these details.

Separate facts from assumptions. Explain trade-offs and identify claims I should verify. Do not invent quotations, references or page numbers.
```

**Response:**

```text
Prompt A — Response: Connected Development Teams
Introduction
Connected development teams use online tools to collaborate, share code, and manage software projects. For a small student team, GitHub can make development more organized and efficient. However, successful teamwork also requires communication, planning, and testing.
In this fictional scenario, four university students are developing a study room booking application. They have four weeks to complete the project and limited experience with GitHub. Their main challenge is working on different features without creating conflicts or introducing errors.
Task Distribution
The first important decision is to divide responsibilities between team members. One student can develop the user interface, another can manage room information, the third can implement booking functionality, and the fourth can focus on testing and integration.
This approach helps students understand their responsibilities and reduces confusion. However, some tasks depend on others. For example, the booking functionality needs information about available rooms. Therefore, the team should discuss requirements and agree on basic interfaces before starting development.
GitHub and Branches
The second engineering decision is to use GitHub with separate branches. Each student should create a branch for their feature instead of editing the main branch directly.
After completing a task, the student can create a Pull Request. Another team member should review the changes before merging them. This process can help identify mistakes and improve code quality.
The main advantage is better control over changes. The disadvantage is that code reviews require additional time. Since the project lasts only four weeks, the team should use short reviews and avoid unnecessary complexity.
Communication
The students can use Telegram to communicate about daily problems and project progress. They can also organize one meeting every week to discuss completed tasks and future plans.
However, important technical decisions may get lost in Telegram messages. Therefore, the team should record important requirements and decisions in GitHub issues or documentation.
Clear communication can help students avoid misunderstandings and coordinate dependent tasks.
Testing and Risk Management
Testing is important because different parts of the application must work together correctly. The students should test important functions, such as viewing available rooms, creating bookings, and preventing overlapping reservations.
They should also test the application after merging changes into the main branch. This can help detect integration problems before the final submission.
Testing takes time, but it reduces the risk of discovering serious errors during the project demonstration.
Facts, Assumptions, and Verification
The use of branches, Pull Requests, and code reviews is a common software development practice. However, their effectiveness depends on how the team uses them.
The four students, four-week deadline, Telegram communication, and application requirements are fictional assumptions, not verified facts.
Two claims that should be checked using reliable sources are:
1. Git branches allow developers to work on separate changes without directly modifying the main branch.
2. Pull Request reviews help teams discuss changes and identify potential problems before merging.
Conclusion
For this project, a simple workflow using task distribution, Git branches, Pull Requests, communication, and testing is appropriate. The team should balance development speed with software quality. GitHub provides useful collaboration tools, but students must use them consistently to achieve successful teamwork.
```

### B2 — Critique (Prompt B)

- **Tool:** ChatGPT
- **Model:** GPT-6
- **Date:** 2026-10-11
- **Purpose:** critical review of the draft

**Prompt:**

```text
Review the draft below against my chosen question and scenario. Identify inaccuracies, missing reasoning, vague claims and unsupported assumptions.
For each concern, explain why it matters and how I could check it. Include a counterexample or alternative interpretation. Do not rewrite the answer yet.
Question: How can a small student development team work together effectively using GitHub? Scenario: Four university students are developing a fictional study room booking application. They have four weeks, limited GitHub experience, and a risk of merge errors. They use Telegram and weekly meetings. Draft: Prompt A — Response: Connected Development Teams
Introduction
Connected development teams use online tools to collaborate, share code, and manage software projects. For a small student team, GitHub can make development more organized and efficient. However, successful teamwork also requires communication, planning, and testing.
In this fictional scenario, four university students are developing a study room booking application. They have four weeks to complete the project and limited experience with GitHub. Their main challenge is working on different features without creating conflicts or introducing errors.
Task Distribution
The first important decision is to divide responsibilities between team members. One student can develop the user interface, another can manage room information, the third can implement booking functionality, and the fourth can focus on testing and integration.
This approach helps students understand their responsibilities and reduces confusion. However, some tasks depend on others. For example, the booking functionality needs information about available rooms. Therefore, the team should discuss requirements and agree on basic interfaces before starting development.
GitHub and Branches
The second engineering decision is to use GitHub with separate branches. Each student should create a branch for their feature instead of editing the main branch directly.
After completing a task, the student can create a Pull Request. Another team member should review the changes before merging them. This process can help identify mistakes and improve code quality.
The main advantage is better control over changes. The disadvantage is that code reviews require additional time. Since the project lasts only four weeks, the team should use short reviews and avoid unnecessary complexity.
Communication
The students can use Telegram to communicate about daily problems and project progress. They can also organize one meeting every week to discuss completed tasks and future plans.
However, important technical decisions may get lost in Telegram messages. Therefore, the team should record important requirements and decisions in GitHub issues or documentation.
Clear communication can help students avoid misunderstandings and coordinate dependent tasks.
Testing and Risk Management
Testing is important because different parts of the application must work together correctly. The students should test important functions, such as viewing available rooms, creating bookings, and preventing overlapping reservations.
They should also test the application after merging changes into the main branch. This can help detect integration problems before the final submission.
Testing takes time, but it reduces the risk of discovering serious errors during the project demonstration.
Facts, Assumptions, and Verification
The use of branches, Pull Requests, and code reviews is a common software development practice. However, their effectiveness depends on how the team uses them.
The four students, four-week deadline, Telegram communication, and application requirements are fictional assumptions, not verified facts.
Two claims that should be checked using reliable sources are:
1. Git branches allow developers to work on separate changes without directly modifying the main branch.
2. Pull Request reviews help teams discuss changes and identify potential problems before merging.
Conclusion
For this project, a simple workflow using task distribution, Git branches, Pull Requests, communication, and testing is appropriate. The team should balance development speed with software quality. GitHub provides useful collaboration tools, but students must use them consistently to achieve successful teamwork.
```

**Response:**

```text
B2 — Response (Prompt B: Critical Review)
1. Task distribution is too simple
Concern: The draft suggests giving each student one responsibility, but it does not explain how dependent tasks will be coordinated.
Why it matters: The booking functionality depends on room information. If students develop these features without agreeing on a shared data structure, integration problems may appear.
How to check: Create a task dependency list and review the required data for each feature before development.
Recommendation: Define shared interfaces and responsibilities before students start coding.
2. Git branches do not prevent all conflicts
Concern: The draft suggests that separate branches help students avoid conflicts, but branches do not completely prevent merge conflicts.
Why it matters: Two students can change the same lines in different branches. Problems may appear when their changes are merged.
How to check: Read the official Git documentation about branching and merging.
Recommendation: Use small branches, update them regularly, and review changes before merging.
3. Pull Request reviews have limitations
Concern: The draft claims that Pull Request reviews can improve code quality, but this is not guaranteed.
Why it matters: Students with limited programming experience may fail to identify important mistakes during code review.
How to check: Read GitHub documentation about Pull Request reviews and compare the documented features with the claimed benefits.
Recommendation: Use a simple checklist for reviews, including functionality, readability, and testing.
4. Communication rules are unclear
Concern: The draft recommends Telegram and weekly meetings but does not explain how important decisions will be recorded.
Why it matters: Technical information may become difficult to find in long conversations.
How to check: Examine whether team members can find previous decisions and understand why they were made.
Recommendation: Use Telegram for quick communication and GitHub issues or documentation for important technical decisions.
5. Testing needs more specific examples
Concern: The draft recommends testing but does not describe enough test cases.
Why it matters: A booking application may appear functional while still allowing incorrect or overlapping reservations.
How to check: Create test cases for successful bookings, unavailable rooms, overlapping bookings, and invalid requests.
Recommendation: Test the most important functions before and after merging changes.
6. The four-week deadline needs more attention
Concern: The draft recommends several development practices without fully considering their time costs.
Why it matters: Too many meetings, reviews, and complicated procedures may slow down a small student team.
How to check: Estimate the time required for development, testing, meetings, and reviews.
Recommendation: Use short Pull Requests, simple documentation, and focused weekly meetings.
7. Some claims require external verification
Concern: The draft presents Git branches and Pull Request reviews as useful practices without providing supporting sources.
Why it matters: The assignment requires factual claims to be verified rather than accepted only because an AI assistant suggested them.
How to check: Consult official Git and GitHub documentation.
Recommendation: Verify these two claims:
1. Git branches allow developers to work on separate changes without directly modifying the main branch.
2. Pull Requests allow team members to review and discuss proposed changes before merging.
Counterexample
Imagine that two students work on different branches. One changes how room availability is calculated, while another changes the booking process. Both branches may merge without a textual conflict, but the combined application could still allow overlapping reservations.
This demonstrates that Git branches cannot guarantee correct software behavior. Integration testing is still necessary.
Alternative interpretation
Instead of assigning one fixed component to each student, the team could use pair programming for complicated features. Two students could work together on booking functionality while the others develop the interface and tests.
Pair programming may help students share knowledge and identify mistakes earlier. However, it may reduce the number of features developed simultaneously.
Overall assessment
The original draft provides a reasonable starting point, but it needs more specific engineering decisions, clearer risk management, and verified factual claims.
The strongest improvements would be defining shared interfaces, introducing a simple Pull Request checklist, adding concrete booking test cases, and balancing collaboration practices with the four-week deadline.
```

### B3 — Revision (Prompt C)

- **Tool:** ChatGPT
- **Model:** GPT-6
- **Date:** 2026-10-11
- **Purpose:** revision using my decisions and verified evidence

**Prompt:**

```text
Revise the draft using my review decisions and source notes below. Keep the answer relevant to my scenario and preserve uncertainty where evidence is limited.

My decisions:

1. Accept task coordination feedback because booking functionality depends on room information.
2. Accept the branch limitation because separate branches do not guarantee conflict-free merging.
3. Qualify the Pull Request feedback because reviews support checking changes but do not guarantee code quality.
4. Accept communication feedback because important decisions should be recorded in GitHub.
5. Accept testing feedback because booking conflicts and invalid requests need specific tests.
6. Accept deadline feedback because a four-week project needs a simple workflow.
7. Accept verification feedback because factual claims require reliable sources.

Verified evidence:

1. Git documentation, "Git Branching — Branches in a Nutshell," accessed 2026-10-11. Git branches allow separate lines of development. Decision: keep. However, branches do not guarantee correct integration.
2. GitHub Docs, "About pull request reviews," accessed 2026-10-11. Pull Request reviews allow developers to comment on changes, suggest improvements, and approve or request changes. Decision: qualify. Reviews do not guarantee that all bugs will be detected.

Draft: Prompt A — Response: Connected Development Teams

Introduction

Connected development teams use online tools to collaborate, share code, and manage software projects. For a small student team, GitHub can make development more organized and efficient. However, successful teamwork also requires communication, planning, and testing.

In this fictional scenario, four university students are developing a study room booking application. They have four weeks to complete the project and limited experience with GitHub. Their main challenge is working on different features without creating conflicts or introducing errors.

Task Distribution

The first important decision is to divide responsibilities between team members. One student can develop the user interface, another can manage room information, the third can implement booking functionality, and the fourth can focus on testing and integration.

This approach helps students understand their responsibilities and reduces confusion. However, some tasks depend on others. For example, the booking functionality needs information about available rooms. Therefore, the team should discuss requirements and agree on basic interfaces before starting development.

GitHub and Branches

The second engineering decision is to use GitHub with separate branches. Each student should create a branch for their feature instead of editing the main branch directly.

After completing a task, the student can create a Pull Request. Another team member should review the changes before merging them. This process can help identify mistakes and improve code quality.

The main advantage is better control over changes. The disadvantage is that code reviews require additional time. Since the project lasts only four weeks, the team should use short reviews and avoid unnecessary complexity.

Communication

The students can use Telegram to communicate about daily problems and project progress. They can also organize one meeting every week to discuss completed tasks and future plans.

However, important technical decisions may get lost in Telegram messages. Therefore, the team should record important requirements and decisions in GitHub issues or documentation.

Clear communication can help students avoid misunderstandings and coordinate dependent tasks.

Testing and Risk Management

Testing is important because different parts of the application must work together correctly. The students should test important functions, such as viewing available rooms, creating bookings, and preventing overlapping reservations.

They should also test the application after merging changes into the main branch. This can help detect integration problems before the final submission.

Testing takes time, but it reduces the risk of discovering serious errors during the project demonstration.

Facts, Assumptions, and Verification

The use of branches, Pull Requests, and code reviews is a common software development practice. However, their effectiveness depends on how the team uses them.

The four students, four-week deadline, Telegram communication, and application requirements are fictional assumptions, not verified facts.

Two claims that should be checked using reliable sources are:

1. Git branches allow developers to work on separate changes without directly modifying the main branch.
2. Pull Request reviews help teams discuss changes and identify potential problems before merging.

Conclusion

For this project, a simple workflow using task distribution, Git branches, Pull Requests, communication, and testing is appropriate. The team should balance development speed with software quality. GitHub provides useful collaboration tools, but students must use them consistently to achieve successful teamwork.

Show what you changed and why. Use only the sources I supplied. Flag remaining gaps instead of inventing details.
```

**Response:**

```text
B3 — Response (Prompt C: Revised Draft)
Connected Development Teams — Revised Analysis
Connected development teams use online tools to share code, communicate, and organize software projects. In this fictional scenario, four university students are developing a study room booking application. They have four weeks to finish the project and limited experience with GitHub. Their main challenge is coordinating development while reducing integration errors.
Task Distribution and Coordination
The first engineering decision is to divide the project into smaller tasks. One student can develop the user interface, another can manage room information, a third can implement booking functionality, and the fourth can focus on testing and integration.
However, dividing responsibilities is not enough. The booking feature depends on room information. Therefore, the team should agree on shared data structures and interfaces before development. This can reduce misunderstandings and incompatible implementations.
For difficult features, students could also work in pairs. Pair programming may support knowledge sharing, but it reduces the number of tasks completed simultaneously.
Git Branches and Integration
The second engineering decision is to use separate Git branches. According to the supplied notes from Git Branching — Branches in a Nutshell, branches allow separate lines of development.
Each student should create a branch for a specific feature. When the feature is ready, the student can open a Pull Request.
However, separate branches do not guarantee conflict-free merging or correct integration. Two students may modify related functionality, causing problems when changes are combined.
The team should use small branches, update them regularly, and test the application after merging.
Pull Request Reviews
According to the supplied notes from GitHub Docs — About pull request reviews, developers can comment on changes, suggest improvements, approve changes, or request modifications.
For this project, each Pull Request should be checked by another student using a simple checklist:
1. Does the feature work correctly?
2. Is the code understandable?
3. Were important functions tested?
4. Could the change affect another feature?
Reviews provide an opportunity to identify problems, but they do not guarantee software quality. Inexperienced students may overlook mistakes.
Communication and Documentation
The team should use Telegram for quick communication and hold one meeting every week.
Important technical decisions should also be recorded in GitHub issues or documentation. For example, students should document how room availability works and how overlapping reservations are prevented.
This can make important information easier to find and reduce misunderstandings.
Testing and Risk Management
Testing should focus on the most important functions of the booking application.
The students should test successful bookings, unavailable rooms, overlapping reservations, and invalid requests.
For example, if one student books a room from 10:00 to 11:00, another student should not be allowed to book the same room from 10:30 to 11:30.
The team should also perform integration testing after merging changes.
Because the deadline is four weeks, the students should prioritize important risks rather than attempt to test every possible situation.
Time and Quality Trade-offs
The team must balance development speed and quality. Branches and Pull Request reviews require time, but they support organized collaboration.
Complicated rules and long meetings may slow down inexperienced students. Therefore, the team should use small tasks, short reviews, simple documentation, and focused testing.
Conclusion
A simple GitHub workflow is suitable for this fictional student project. The students should divide tasks, agree on interfaces, use separate branches, review Pull Requests, communicate regularly, and test important functionality.
However, GitHub cannot guarantee correct software or successful teamwork. The students must coordinate their activities and follow the agreed process.

Changes made and why
Change	Reason
Added shared interfaces before coding	Booking functionality depends on room information
Clarified limitations of Git branches	Independent branches do not guarantee correct integration
Added a Pull Request review checklist	Reviews cannot guarantee that all bugs will be detected
Added specific booking test cases	The original draft lacked concrete testing examples
Added documentation of important decisions	Telegram messages may be difficult to find later
Simplified the workflow	The team has only four weeks and limited GitHub experience
Remaining gaps
The supplied source notes describe Git branches and Pull Request reviews, but the original documentation pages have not been independently examined in this exchange. Their accuracy and exact locations still need confirmation.
There is no measured evidence showing how much time reviews or testing will require for this fictional team. The proposed workflow is therefore a practical recommendation, not a guarantee of improved performance.
```

## 9. Appendix C — Evidence tables

### Verification table

<!-- At least two complete rows. Source and locator: title + page / slide / section / chapter,
     or title + URL + access date (YYYY-MM-DD). Decision: keep, qualify or reject — one word. -->

| AI claim | Source and locator | Evidence found | Decision |
| --- | --- | --- | --- |
| Git branches allow separate development. | Pro Git, Section 3.1, https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell, accessed 2026-10-11 | Branches allow separate lines of development. | keep |
| Pull Request reviews improve code quality. | GitHub Docs, Pull request reviews, https://docs.github.com/en/pull-requests/reference/pull-request-reviews, accessed 2026-10-11 | Reviews allow comments, approvals, and requests for changes, but do not guarantee quality. | qualify |
### Change log

<!-- At least two substantive revisions. Your final version must differ from the AI wording,
     and the reason must say which evidence or scenario constraint made you change it. -->

| AI wording / suggestion | Your final version | Reason for change |
| --- | --- | --- |
| Divide the project into separate tasks. | Define shared interfaces and data structures before development. | The booking feature depends on room information. |
| Review Pull Requests to improve code quality. | Use a review checklist and test important booking functions. | Reviews alone cannot guarantee that all errors are detected. |
| Test the application before submission. | Test successful bookings, overlapping reservations, and invalid requests. | The original suggestion lacked specific test cases. |
