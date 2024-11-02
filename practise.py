class Doctor:
    def __init__(self, name):
        self.name = name

class Patient:
    def __init__(self, name):
        self.name = name

    def introduce_doctor(self, doctor):
        print(f"My Doctor is {doctor.name}")


doctor1 = Doctor("Mr.Vadym")
patient1 = Patient("Ihor")
patient1.introduce_doctor(doctor1)