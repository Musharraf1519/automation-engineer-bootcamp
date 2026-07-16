"""
=========================================================
Script : create_solution_templates.py
Purpose: Generate solution template files (Q01.py, Q02.py...)
=========================================================
"""

from pathlib import Path

# =========================================================
# USER CONFIGURATION
# =========================================================

MODULE = "01-Python"
CHAPTER = "05-Input-and-Output"
TOTAL_QUESTIONS = 30

# =========================================================
# BUILD DESTINATION PATH
# =========================================================

destination = (
    Path.cwd()
    / MODULE
    / "05-Input-and-Output"
    / CHAPTER
)

destination.mkdir(parents=True, exist_ok=True)

# =========================================================
# TEMPLATE
# =========================================================

template = '''"""
========================================================
Module   : {module}
Chapter  : {chapter}
Question : {question}
========================================================

Question:



--------------------------------------------------------
Solution
--------------------------------------------------------
"""



# Write your solution below




'''

# =========================================================
# GENERATE FILES
# =========================================================

print("=" * 60)
print("Generating Solution Templates")
print("=" * 60)

created = 0
skipped = 0

for i in range(1, TOTAL_QUESTIONS + 1):

    question = f"Q{i:02}"

    file_path = destination / f"{question}.py"

    if file_path.exists():
        print(f"[SKIPPED] {question}.py already exists")
        skipped += 1
        continue

    file_path.write_text(
        template.format(
            module=MODULE,
            chapter=CHAPTER,
            question=question
        ),
        encoding="utf-8"
    )

    print(f"[CREATED] {question}.py")
    created += 1

print("\n" + "=" * 60)
print("Generation Complete")
print("=" * 60)

print(f"Location : {destination}")
print(f"Created  : {created}")
print(f"Skipped  : {skipped}")