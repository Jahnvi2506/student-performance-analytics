# Student Performance Analytics System

## 1. Project Title
**Student Performance Analytics System**

- **Student Name:** _<your name here>_
- **Program:** EWB Courses – Python with AI (Internship Project)
- **Submission Date:** 15 October 2026

## 2. Objective
Schools and colleges collect marks for many students across many subjects, but raw marks alone do not tell us who is doing well, which subjects are weak, or who needs help. This project reads student data from a CSV file and automatically calculates totals, averages, grades and pass/fail status, and then produces a class-level, subject-level and department-level analysis, including the list of top performers. It turns a plain marks sheet into clear, usable insights.

## 3. Technologies Used
- **Python 3** – core language (variables, data types, loops, conditions, functions)
- **NumPy** – numerical calculations (sum, mean, max, min, standard deviation, `np.where`, `np.all`)
- **Pandas** – loading the CSV, DataFrame operations, filtering, `groupby`, sorting

## 4. Dataset Description
File: `students.csv` – **20 student records**, 4 departments (Computer Science, Electronics, Mechanical, Civil), 5 students each.

| Column | Description |
|---|---|
| Student_ID | Unique ID (S001 – S020) |
| Name | Student name |
| Department | Department of the student |
| Maths, Physics, Chemistry, English, Computer | Subject marks out of 100 |
| Attendance | Attendance percentage |

The data is a sample dataset created for this project. It has no missing values.

## 5. Implementation (Step by Step)

1. **Load data** – `load_data()` reads `students.csv` into a Pandas DataFrame. The program prints the shape, column names, first 5 rows and a missing-value check.
2. **Total & Average** – `calculate_total_and_average()` converts the subject columns to a 2D NumPy array and uses `np.sum` and `np.mean` along `axis=1` to get each student's total and average.
3. **Grades** – `add_grades()` loops through every average and calls `assign_grade()`.

   | Average | Grade |
   |---|---|
   | 90 and above | A+ |
   | 80 – 89.99 | A |
   | 70 – 79.99 | B |
   | 60 – 69.99 | C |
   | 50 – 59.99 | D |
   | Below 50 | F |

4. **Pass / Fail** – `add_pass_fail()` loops through each student. A student **passes only if marks are at least 40 in every subject** (checked with `np.all`). Attendance below **75%** is flagged as "Low Attendance" using `np.where`.
5. **Overall statistics** – `overall_statistics()` finds the class average, highest and lowest performer, number of students passed/failed and the pass percentage.
6. **Subject-wise analysis** – `subject_analysis()` loops over each subject and computes average, highest, lowest, standard deviation, subject topper and number of students failing that subject.
7. **Grade distribution & department analysis** – `grade_distribution()` counts students per grade; `department_analysis()` uses `groupby` to compare departments.
8. **Top performers** – `top_performers()` sorts by average and returns the top 5 students.
9. **Output** – `main.py` prints everything in clearly labelled sections and saves the processed table to `student_results.csv`.

## 6. Key Features
- Reusable functions kept in `functions.py`
- NumPy used for all numerical calculations
- Pandas used for loading, filtering, grouping and sorting
- Loops used for grading, pass/fail checking and subject analysis
- Clearly defined grading rule and pass/fail rule
- Subject-wise, department-wise and grade-wise analysis
- Top-5 performers, failed students and low-attendance list
- Results exported to `student_results.csv`

## 7. Project Structure
```
student-performance-analytics/
├── main.py              # runs the project and prints the final analysis
├── functions.py         # reusable calculation / processing functions
├── students.csv         # input dataset (20 students)
├── student_results.csv  # generated output with totals, grades and results
├── output.txt           # saved console output of a full run
├── requirements.txt     # dependencies
└── README.md            # documentation
```

## 8. How to Run
```bash
pip install -r requirements.txt
python main.py
```

## 9. Output / Results
Key results from a run of `main.py` (full output is in `output.txt`):

```
OVERALL CLASS PERFORMANCE
Total students      : 20
Class average       : 71.25
Highest average     : 93.0 (Ananya Singh)
Lowest average      : 42.4 (Deepak Saini)
Students passed     : 17
Students failed     : 3
Pass percentage     : 85.0%

SUBJECT-WISE ANALYSIS
  Subject  Average  Highest  Lowest  Std_Dev         Topper  Students_Failed
    Maths    70.60       95      34    18.05   Ananya Singh                1
  Physics    70.05       94      36    16.74     Kavya Iyer                1
Chemistry    70.00       94      38    16.34 Tanvi Kulkarni                1
  English    73.75       93      50    13.00   Ananya Singh                0
 Computer    71.85       97      42    15.71   Ananya Singh                0

GRADE DISTRIBUTION
A+: 2   A: 5   B: 5   C: 4   D: 1   F: 3

DEPARTMENT-WISE ANALYSIS
                  Students  Average_Marks  Avg_Attendance  Passed
Computer Science         5          77.16            85.2       5
Civil                    5          70.20            82.6       4
Mechanical               5          68.88            80.0       4
Electronics              5          68.76            82.2       4

TOP 5 PERFORMERS
S004  Ananya Singh    Computer Science  465  93.0  A+
S020  Tanvi Kulkarni  Civil             452  90.4  A+
S014  Kavya Iyer      Mechanical        445  89.0  A
S001  Aarav Sharma    Computer Science  438  87.6  A
S002  Priya Verma     Computer Science  425  85.0  A
```

_(Add screenshots of your terminal output in a `screenshots/` folder if you wish – this section is optional.)_

## 10. Final Outcome
The project successfully reads the student dataset, calculates totals, averages, grades and pass/fail status for all 20 students, and produces a complete analysis:

- The class average is **71.25** and **17 of 20 students (85%)** passed.
- **Ananya Singh** (Computer Science) is the top performer with an average of 93.0.
- **English** is the best-performing subject (average 73.75); **Chemistry** has the lowest average (70.0).
- **Computer Science** is the best-performing department (average 77.16).
- All 3 failed students also have attendance below 75%, which suggests a link between low attendance and poor results.

## 11. Challenges & Learning
- **Defining the pass rule:** Using only the average would let a student pass despite failing a subject. I used "at least 40 in every subject" with `np.all` to handle this correctly.
- **Choosing between loops and vectorised operations:** I learned that NumPy/Pandas handle whole columns at once (totals, means), while loops are useful where row-by-row logic is needed (grading, pass/fail).
- **Organising code:** Splitting the logic into `functions.py` and keeping `main.py` only for output made the code easier to read, test and reuse.
- **Learning:** I practised NumPy array operations, Pandas `groupby`/`agg`, function design, and publishing a project with documentation on GitHub.

## 12. GitHub Repository
🔗 _<paste your final GitHub repository link here>_
