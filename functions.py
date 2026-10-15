"""
functions.py
Reusable functions for the Student Performance Analytics System.
"""

import numpy as np
import pandas as pd

# Subject columns present in students.csv
SUBJECTS = ["Maths", "Physics", "Chemistry", "English", "Computer"]

# Rules used in the project
PASS_MARK_PER_SUBJECT = 40      # student must score >= 40 in EVERY subject to pass
MIN_ATTENDANCE = 75             # attendance below this is flagged


def load_data(file_path):
    """Read the student CSV file into a Pandas DataFrame."""
    return pd.read_csv(file_path)


def calculate_total_and_average(df):
    """Add Total and Average columns using NumPy on the subject marks."""
    marks = df[SUBJECTS].to_numpy()                 # 2D NumPy array
    df["Total"] = np.sum(marks, axis=1)             # row-wise total
    df["Average"] = np.round(np.mean(marks, axis=1), 2)
    return df


def assign_grade(average):
    """Grading rule based on average marks."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def add_grades(df):
    """Apply the grading rule to every student using a loop."""
    grades = []
    for avg in df["Average"]:
        grades.append(assign_grade(avg))
    df["Grade"] = grades
    return df


def add_pass_fail(df):
    """
    Pass condition: marks >= 40 in every subject.
    Also flags students whose attendance is below the minimum.
    """
    results = []
    for _, row in df.iterrows():
        marks = row[SUBJECTS].to_numpy(dtype=float)
        results.append("Pass" if np.all(marks >= PASS_MARK_PER_SUBJECT) else "Fail")
    df["Result"] = results
    df["Attendance_Status"] = np.where(
        df["Attendance"] >= MIN_ATTENDANCE, "OK", "Low Attendance"
    )
    return df


def overall_statistics(df):
    """Highest, lowest and average performance of the class."""
    best = df.loc[df["Average"].idxmax()]
    worst = df.loc[df["Average"].idxmin()]
    return {
        "total_students": len(df),
        "class_average": round(float(np.mean(df["Average"])), 2),
        "highest_average": float(best["Average"]),
        "highest_student": best["Name"],
        "lowest_average": float(worst["Average"]),
        "lowest_student": worst["Name"],
        "passed": int((df["Result"] == "Pass").sum()),
        "failed": int((df["Result"] == "Fail").sum()),
        "pass_percentage": round(float((df["Result"] == "Pass").mean() * 100), 2),
    }


def subject_analysis(df):
    """Subject-wise average, highest, lowest, std-dev and topper (uses a loop)."""
    rows = []
    for subject in SUBJECTS:
        col = df[subject].to_numpy()
        rows.append({
            "Subject": subject,
            "Average": round(float(np.mean(col)), 2),
            "Highest": int(np.max(col)),
            "Lowest": int(np.min(col)),
            "Std_Dev": round(float(np.std(col)), 2),
            "Topper": df.loc[df[subject].idxmax(), "Name"],
            "Students_Failed": int(np.sum(col < PASS_MARK_PER_SUBJECT)),
        })
    return pd.DataFrame(rows)


def grade_distribution(df):
    """Number of students in each grade."""
    order = ["A+", "A", "B", "C", "D", "F"]
    return df["Grade"].value_counts().reindex(order, fill_value=0)


def department_analysis(df):
    """Department-wise average marks and pass count."""
    summary = df.groupby("Department").agg(
        Students=("Student_ID", "count"),
        Average_Marks=("Average", "mean"),
        Avg_Attendance=("Attendance", "mean"),
        Passed=("Result", lambda r: (r == "Pass").sum()),
    ).round(2)
    return summary.sort_values("Average_Marks", ascending=False)


def top_performers(df, n=5):
    """Return the top n students by average marks."""
    return (
        df.sort_values("Average", ascending=False)
        .head(n)[["Student_ID", "Name", "Department", "Total", "Average", "Grade"]]
        .reset_index(drop=True)
    )
