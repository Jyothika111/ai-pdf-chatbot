from llm import generate_answer

context = """
Goldman Sachs Summer Internship Program 2026 is open for applications.
Eligible students are graduating in 2027.
The internship duration is 8-10 weeks.
"""

question = "Who is eligible for the Goldman Sachs internship?"

answer = generate_answer(
    question,
    context
)

print(answer)