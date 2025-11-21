# Work done by: Mohammad Al-Refaie

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from tkinter import ttk
from ttkthemes import ThemedTk

# Function to calculate the predicted grade
def calculate_grade():
    attendance_val = float(attendance_entry.get())
    study_hours_val = float(study_hours_entry.get())
    previous_exam_grade_val = float(previous_exam_grade_entry.get())

    # Set input values
    grade_system.input['attendance'] = attendance_val
    grade_system.input['study_hours'] = study_hours_val
    grade_system.input['previous_exam_grade'] = previous_exam_grade_val

    # Compute the predicted grade
    grade_system.compute()
    # Display the predicted grade
    result_label.config(text=f"Predicted Grade: {grade_system.output['predicted_grade'].round(2)}")

# Fuzzy system setup
attendance = ctrl.Antecedent(np.arange(0, 29, 0.1), 'attendance')
study_hours = ctrl.Antecedent(np.arange(0, 9, 0.1), 'study_hours')
previous_exam_grade = ctrl.Antecedent(np.arange(0, 31, 0.1), 'previous_exam_grade')
predicted_grade = ctrl.Consequent(np.arange(0, 51, 0.1), 'predicted_grade')

# Define membership functions
attendance['low'] = fuzz.trimf(attendance.universe, [0, 0, 14])
attendance['medium'] = fuzz.trimf(attendance.universe, [15, 24, 25])
attendance['high'] = fuzz.trimf(attendance.universe, [25, 28, 28])

study_hours['low'] = fuzz.trimf(study_hours.universe, [0, 1, 2])
study_hours['medium'] = fuzz.trimf(study_hours.universe, [2, 4, 5])
study_hours['good'] = fuzz.trimf(study_hours.universe, [5, 8, 8])

previous_exam_grade['poor'] = fuzz.trimf(previous_exam_grade.universe, [0, 0, 12])
previous_exam_grade['good'] = fuzz.trimf(previous_exam_grade.universe, [13, 20, 21])
previous_exam_grade['excellent'] = fuzz.trimf(previous_exam_grade.universe, [21, 30, 30])

predicted_grade['low'] = fuzz.trimf(predicted_grade.universe, [0, 0, 21])
predicted_grade['medium'] = fuzz.trimf(predicted_grade.universe, [22, 35, 36])
predicted_grade['high'] = fuzz.trimf(predicted_grade.universe, [36, 50, 50])

# Define rules
rule1 = ctrl.Rule(attendance['low'] & study_hours['low'] & previous_exam_grade['poor'], predicted_grade['low'])
rule2 = ctrl.Rule(attendance['low'] & study_hours['low'] & previous_exam_grade['good'], predicted_grade['low'])
rule3 = ctrl.Rule(attendance['low'] & study_hours['low'] & previous_exam_grade['excellent'], predicted_grade['low'])

rule4 = ctrl.Rule(attendance['low'] & study_hours['medium'] & previous_exam_grade['poor'], predicted_grade['low'])
rule5 = ctrl.Rule(attendance['low'] & study_hours['medium'] & previous_exam_grade['good'], predicted_grade['low'])
rule6 = ctrl.Rule(attendance['low'] & study_hours['medium'] & previous_exam_grade['excellent'], predicted_grade['medium'])
rule7 = ctrl.Rule(attendance['low'] & study_hours['good'] & previous_exam_grade['poor'], predicted_grade['medium'])
rule8 = ctrl.Rule(attendance['low'] & study_hours['good'] & previous_exam_grade['good'], predicted_grade['medium'])
rule9 = ctrl.Rule(attendance['low'] & study_hours['good'] & previous_exam_grade['excellent'], predicted_grade['high'])
rule10 = ctrl.Rule(attendance['medium'] & study_hours['low'] & previous_exam_grade['poor'], predicted_grade['low'])
rule11 = ctrl.Rule(attendance['medium'] & study_hours['low'] & previous_exam_grade['good'], predicted_grade['medium'])
rule12 = ctrl.Rule(attendance['medium'] & study_hours['low'] & previous_exam_grade['excellent'], predicted_grade['high'])
rule13 = ctrl.Rule(attendance['medium'] & study_hours['medium'] & previous_exam_grade['poor'], predicted_grade['medium'])
rule14 = ctrl.Rule(attendance['medium'] & study_hours['medium'] & previous_exam_grade['good'], predicted_grade['medium'])
rule15 = ctrl.Rule(attendance['medium'] & study_hours['medium'] & previous_exam_grade['excellent'], predicted_grade['high'])
rule16 = ctrl.Rule(attendance['medium'] & study_hours['good'] & previous_exam_grade['poor'], predicted_grade['medium'])
rule17 = ctrl.Rule(attendance['medium'] & study_hours['good'] & previous_exam_grade['good'], predicted_grade['high'])
rule18 = ctrl.Rule(attendance['medium'] & study_hours['good'] & previous_exam_grade['excellent'], predicted_grade['high'])
rule19 = ctrl.Rule(attendance['high'] & study_hours['low'] & previous_exam_grade['poor'], predicted_grade['medium'])
rule20 = ctrl.Rule(attendance['high'] & study_hours['low'] & previous_exam_grade['good'], predicted_grade['medium'])
rule21 = ctrl.Rule(attendance['high'] & study_hours['low'] & previous_exam_grade['excellent'], predicted_grade['high'])
rule22 = ctrl.Rule(attendance['high'] & study_hours['medium'] & previous_exam_grade['poor'], predicted_grade['medium'])
rule23 = ctrl.Rule(attendance['high'] & study_hours['medium'] & previous_exam_grade['good'], predicted_grade['high'])
rule24 = ctrl.Rule(attendance['high'] & study_hours['medium'] & previous_exam_grade['excellent'], predicted_grade['high'])
rule25 = ctrl.Rule(attendance['high'] & study_hours['good'] & previous_exam_grade['poor'], predicted_grade['high'])
rule26 = ctrl.Rule(attendance['high'] & study_hours['good'] & previous_exam_grade['good'], predicted_grade['high'])
rule27 = ctrl.Rule(attendance['high'] & study_hours['good'] & previous_exam_grade['excellent'], predicted_grade['high'])


# Control system setup
grade_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6,
rule7, rule8, rule9, rule10, rule11, rule12,
rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20, rule21,
rule22, rule23, rule24, rule25, rule26, rule27])

grade_system = ctrl.ControlSystemSimulation(grade_ctrl)

# GUI setup
root = ThemedTk()
root.get_themes()
root.set_theme("equilux")
root.title("Grade Prediction System")

# Centering the GUI on the screen
window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()
position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
position_down = int(root.winfo_screenheight() / 2 - window_height / 2)
root.geometry(f'+{position_right}+{position_down}')

# Styling
style = ttk.Style()
style.configure("TLabel", padding=10, font=('Helvetica', 16), background='#4CAF50', foreground='white')
style.configure("TButton", padding=10, font=('Helvetica', 16), background='#008CBA', foreground='white')
style.configure("TEntry", padding=10, font=('Helvetica', 16), background='lightgray')
style.configure("TFrame", background='#2C3E50')

# Frame to contain all widgets
frame = ttk.Frame(root)
frame.pack(expand=True, fill='both')

# Attendance input
attendance_label = ttk.Label(frame, text="Attendance: (28 lectures in total)")
attendance_label.grid(row=0, column=0, padx=20, pady=10)
attendance_entry = ttk.Entry(frame)
attendance_entry.grid(row=0, column=1, padx=20, pady=10)

# Study hours input
study_hours_label = ttk.Label(frame, text="Study Hours/Week:")
study_hours_label.grid(row=1, column=0, padx=20, pady=10)
study_hours_entry = ttk.Entry(frame)
study_hours_entry.grid(row=1, column=1, padx=20, pady=10)

# Previous exam grade input
previous_exam_grade_label = ttk.Label(frame, text="Previous Exam Grade:")
previous_exam_grade_label.grid(row=2, column=0, padx=20, pady=10)
previous_exam_grade_entry = ttk.Entry(frame)
previous_exam_grade_entry.grid(row=2, column=1, padx=20, pady=10)

# Button to calculate grade
calculate_button = ttk.Button(frame, text="Calculate Grade", command=calculate_grade)
calculate_button.grid(row=3, column=0, columnspan=2, pady=20)
# Display predicted grade
result_label = ttk.Label(frame, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=20)

root.mainloop()
