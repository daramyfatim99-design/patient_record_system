# ---------- Task 1: Classes ----------
class Patient:
    total_patients = 0

    def __init__(self, name, patient_id, age, condition):
        self.name = name
        self.patient_id = patient_id
        self.age = age
        self.condition = condition
        Patient.total_patients += 1

    def display_info(self):
        print(f"ID: {self.patient_id} | Name: {self.name} | Age: {self.age} | Condition: {self.condition}")

    def update_record(self, new_condition):
        self.condition = new_condition

    @classmethod
    def get_total_patients(cls):
        return cls.total_patients

    @staticmethod
    def is_valid_id(patient_id):
        return patient_id.startswith("P")


class Doctor:
    def __init__(self, name, doctor_id, specialty):
        self.name = name
        self.doctor_id = doctor_id
        self.specialty = specialty

    def display_info(self):
        print(f"Doctor ID: {self.doctor_id} | Name: Dr. {self.name} | Specialty: {self.specialty}")

    def examine(self, patient):
        print(f"Dr. {self.name} is examining {patient.name}.")


p1 = Patient("Aminata", "P001", 25, "Malaria")
d1 = Doctor("Kamara", "D001", "General Medicine")

p1.display_info()
d1.display_info()

d1.examine(p1)
p1.update_record("Recovering")
p1.display_info()


# ---------- Task 2: Dictionary ----------
patients = {}

def add_patient(patient):
    patients[patient.patient_id] = patient
    print(f"Added: {patient.name}")

def display_all_patients():
    print("--- All Patient Records ---")
    for patient_id, patient in patients.items():
        patient.display_info()

p2 = Patient("Fatmata", "P002", 30, "Typhoid")
p3 = Patient("Mohamed", "P003", 40, "Flu")

add_patient(p1)
add_patient(p2)
add_patient(p3)

display_all_patients()


# ---------- Task 3: Class and static methods ----------
print("--- Task 3 ---")
print("Total patients created:", Patient.get_total_patients())
print("Is P001 valid?", Patient.is_valid_id("P001"))
print("Is X999 valid?", Patient.is_valid_id("X999"))