import tkinter as tk

def calculate_needed_grade():
    current_grade = float(current_grade_entry.get())
    final_exam_weight = float(final_exam_weight_entry.get()) / 100  # Convert to decimal
    desired_final_grade = float(desired_final_grade_entry.get())
    needed_grade = (desired_final_grade - current_grade * (1 - final_exam_weight)) / final_exam_weight
    result_label.config(text=f"Grade needed on final exam: {needed_grade:.2f}%")

app = tk.Tk()
app.title("Final Grade Calculator")

# Creating labels
tk.Label(app, text="Current Grade (%)").grid(row=0, column=0)
tk.Label(app, text="Final Exam Weight (%)").grid(row=1, column=0)
tk.Label(app, text="Desired Final Grade (%)").grid(row=2, column=0)

# Entry widgets to accept user input
current_grade_entry = tk.Entry(app)
final_exam_weight_entry = tk.Entry(app)
desired_final_grade_entry = tk.Entry(app)

current_grade_entry.grid(row=0, column=1)
final_exam_weight_entry.grid(row=1, column=1)
desired_final_grade_entry.grid(row=2, column=1)

# Button to calculate the needed grade
calculate_button = tk.Button(app, text="Calculate", command=calculate_needed_grade)
calculate_button.grid(row=3, column=0, columnspan=2)

# Label to display the result
result_label = tk.Label(app, text="Enter your grades to see what you need on the final exam!")
result_label.grid(row=4, column=0, columnspan=2)

app.mainloop()