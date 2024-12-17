import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from owlready2 import *

# Load the ontology
ontology = get_ontology("NewtonSecondLaw.owl").load()

# Define the classes from the ontology
Mass = ontology.Mass
Acceleration = ontology.Acceleration
Force = ontology.Force
Problem = ontology.Problem

# Function to update the ontology and calculate force
def update_ontology_and_calculate():
    try:
        # Get user input for mass and acceleration
        mass = float(mass_entry.get())
        acceleration = float(acceleration_entry.get())
        
        # Calculate force (F = m * a)
        force = mass * acceleration

        # Display the calculated force in the GUI
        force_result_label.config(text=f"Calculated Force: {force} N", fg="green")

        # Create new instances and set their data properties
        with ontology:
            new_mass = Mass()  # Create an instance of Mass
            new_mass.valueOfMass = [mass]  # Set the data property

            new_acceleration = Acceleration()  # Create an instance of Acceleration
            new_acceleration.valueOfAcceleration = [acceleration]  # Set the data property

            new_force = Force()  # Create an instance of Force
            new_force.valueOfForce = [force]  # Set the data property
            # Create a new problem instance without passing arguments
            new_problem = Problem()

            # Set the annotation property (e.g., difficultyLevel) separately
            new_problem.difficultyLevel = "Easy"

            # Now, associate the other properties
            new_problem.hasMass = [new_mass]
            new_problem.hasAcceleration = [new_acceleration]
            new_problem.hasForce = [new_force]


        # Save the updated ontology
        ontology.save(file="Updated_NewtonSecondLaw.owl")

        # Provide feedback to the user
        messagebox.showinfo("Success", "Problem added and force calculated successfully!")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values for mass and acceleration.")


# Function to clear the input fields
def clear_fields():
    mass_entry.delete(0, tk.END)
    acceleration_entry.delete(0, tk.END)
    force_result_label.config(text="Calculated Force: ", fg="black")

# Create the main window
root = tk.Tk()
root.title("Newton's Second Law of Motion - Force Calculator")
root.geometry("500x400")
root.configure(bg="lightblue")

# Create a frame for the input fields and labels
frame = tk.Frame(root, bg="lightblue")
frame.pack(padx=20, pady=20, expand=True)

# Add widgets to the frame
mass_label = tk.Label(frame, text="Enter Mass (kg):", font=("Helvetica", 12), bg="lightblue")
mass_label.grid(row=0, column=0, pady=10, sticky="w")

mass_entry = tk.Entry(frame, font=("Helvetica", 12))
mass_entry.grid(row=0, column=1, pady=10, padx=10)

acceleration_label = tk.Label(frame, text="Enter Acceleration (m/s²):", font=("Helvetica", 12), bg="lightblue")
acceleration_label.grid(row=1, column=0, pady=10, sticky="w")

acceleration_entry = tk.Entry(frame, font=("Helvetica", 12))
acceleration_entry.grid(row=1, column=1, pady=10, padx=10)

# Add calculate and clear buttons with styling
button_frame = tk.Frame(root, bg="lightblue")
button_frame.pack(pady=20)

calculate_button = tk.Button(button_frame, text="Calculate Force", font=("Helvetica", 12), bg="green", fg="white", command=update_ontology_and_calculate, relief="raised", width=15)
calculate_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(button_frame, text="Clear", font=("Helvetica", 12), bg="red", fg="white", command=clear_fields, relief="raised", width=15)
clear_button.grid(row=0, column=1, padx=10)

# Add result label for displaying calculated force
force_result_label = tk.Label(root, text="Calculated Force: ", font=("Helvetica", 14), bg="lightblue")
force_result_label.pack(pady=20)

# Optional: Add a footer with additional information
footer_label = tk.Label(root, text="Newton's Second Law of Motion: F = m * a", font=("Helvetica", 10), bg="lightblue", fg="gray")
footer_label.pack(side="bottom", pady=10)

# Start the GUI loop
root.mainloop()
