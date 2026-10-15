"""
main.py
Student Performance Analytics System
Runs the complete analysis and prints the final report.
"""

import pandas as pd
import functions as fn

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 20)


def line(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def main():
    # Step 1 & 2: Load and inspect the data
    df = fn.load_data("students.csv")

    line("1. DATASET OVERVIEW")
    print(f"Records : {df.shape[0]}")
    print(f"Columns : {list(df.columns)}")
    print("\nFirst 5 records:")
    print(df.head())
    print("\nMissing values per column:")
    print(df.isnull().sum().to_string())

    # Step 3: Process the data
    df = fn.calculate_total_and_average(df)
    df = fn.add_grades(df)
    df = fn.add_pass_fail(df)

    line("2. STUDENT RESULTS (Total, Average, Grade, Result)")
    print(df[["Student_ID", "Name", "Department", "Total", "Average",
              "Grade", "Result", "Attendance_Status"]].to_string(index=False))

    # Step 4: Analysis
    stats = fn.overall_statistics(df)
    line("3. OVERALL CLASS PERFORMANCE")
    print(f"Total students      : {stats['total_students']}")
    print(f"Class average       : {stats['class_average']}")
    print(f"Highest average     : {stats['highest_average']} ({stats['highest_student']})")
    print(f"Lowest average      : {stats['lowest_average']} ({stats['lowest_student']})")
    print(f"Students passed     : {stats['passed']}")
    print(f"Students failed     : {stats['failed']}")
    print(f"Pass percentage     : {stats['pass_percentage']}%")

    line("4. SUBJECT-WISE ANALYSIS")
    subject_df = fn.subject_analysis(df)
    print(subject_df.to_string(index=False))
    best = subject_df.loc[subject_df["Average"].idxmax()]
    weak = subject_df.loc[subject_df["Average"].idxmin()]
    print(f"\nBest performing subject  : {best['Subject']} (avg {best['Average']})")
    print(f"Weakest subject          : {weak['Subject']} (avg {weak['Average']})")

    line("5. GRADE DISTRIBUTION")
    print(fn.grade_distribution(df).to_string())

    line("6. DEPARTMENT-WISE ANALYSIS")
    print(fn.department_analysis(df))

    line("7. TOP 5 PERFORMERS")
    print(fn.top_performers(df, 5).to_string(index=False))

    line("8. FAILED STUDENTS / LOW ATTENDANCE")
    failed = df[df["Result"] == "Fail"][["Student_ID", "Name", "Average", "Attendance"]]
    print("Failed students:")
    print(failed.to_string(index=False) if not failed.empty else "None")
    low_att = df[df["Attendance_Status"] == "Low Attendance"][["Student_ID", "Name", "Attendance"]]
    print("\nStudents with attendance below 75%:")
    print(low_att.to_string(index=False) if not low_att.empty else "None")

    # Save processed results
    df.to_csv("student_results.csv", index=False)
    print("\nProcessed results saved to student_results.csv")


if __name__ == "__main__":
    main()
