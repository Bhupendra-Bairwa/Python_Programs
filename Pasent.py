# Step 1: Patient Enroll
patient = {}

print("=== Enroll Patient ===")
patient['name'] = input("Enter patient name: ")
patient['id'] = input("Enter patient ID: ")
patient['symptoms'] = input("Enter symptoms: ")

# Step 2: Department Selection (4 options)
print("\n=== Department Referral ===")
print("1. General Medicine")
print("2. Cardiology")
print("3. Dermatology")
print("4. Neurology")

dept_choice = input("Choose department number (1-4): ")

if dept_choice == '1':
    patient['department'] = "General Medicine"
elif dept_choice == '2':
    patient['department'] = "Cardiology"
elif dept_choice == '3':
    patient['department'] = "Dermatology"
elif dept_choice == '4':
    patient['department'] = "Neurology"
else:
    patient['department'] = "Unknown"

# Step 3: Lab Checkups (2 predefined tests)
print("\n=== Lab Tests ===")
if patient['department'] == "General Medicine":
    patient['lab_tests'] = ["Blood Test", "Urine Test"]
elif patient['department'] == "Cardiology":
    patient['lab_tests'] = ["ECG", "Echo"]
elif patient['department'] == "Dermatology":
    patient['lab_tests'] = ["Skin Biopsy", "Allergy Test"]
elif patient['department'] == "Neurology":
    patient['lab_tests'] = ["MRI", "EEG"]
else:
    patient['lab_tests'] = ["None"]

# Step 4: Store Data in a Text File
print("\nSaving patient details to file...")

with open("patient_report.txt", "w") as file:
    file.write("----- Patient Report -----\n")
    file.write(f"Name: {patient['name']}\n")
    file.write(f"ID: {patient['id']}\n")
    file.write(f"Symptoms: {patient['symptoms']}\n")
    file.write(f"Department: {patient['department']}\n")
    file.write(f"Lab Tests: {', '.join(patient['lab_tests'])}\n")
    file.write("--------------------------\n")

print("✅ Patient details saved in 'patient_report.txt'")