class Hospital:
    def __init__(self):
        self.doctors = []
        self.patients = []

    # === DOCTOR methods ===
    def add_doctor(self, new_doctor_name):
        self.doctors.append(new_doctor_name)

    def remove_doctor(self, remove_doctor_name):
        self.doctors.remove(remove_doctor_name)

    def get_doctor(self):
        return self.doctors

    # === PATIENT methods ===
    def add_patient(self, new_patient_name):
        self.patients.append(new_patient_name)

    def remove_patient(self, remove_patient_name):
        self.patients.remove(remove_patient_name)

    def get_patient(self):
        return self.patients

# Object banate hain
hospital = Hospital()

# Doctors aur Patients add karo
hospital.add_doctor("Dr misbah")
hospital.add_doctor("Dr madiha")
hospital.add_patient("Hamza")
hospital.add_patient("Ali")

# Remove karo
hospital.remove_doctor("Dr madiha")
hospital.remove_patient("Hamza")

# Print results
print("Doctors:", hospital.get_doctor())
print("Patients:", hospital.get_patient())
