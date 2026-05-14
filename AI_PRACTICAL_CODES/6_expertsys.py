# Expert System for Medical Diagnosis

class SymptomChecker:

    def __init__(self):

        self.symptoms = {
            "fever": False,
            "cough": False,
            "headache": False,
            "rash": False
        }

    # Taking User Input
    def ask_symptoms(self):

        print("Please answer with yes or no\n")

        for symptom in self.symptoms:

            response = input(f"Do you have {symptom}? ").lower()

            if response == "yes" or response == "y":
                self.symptoms[symptom] = True

    # Diagnosis Function
    def diagnose(self):

        print("\nDiagnosis Result:")

        # All Symptoms
        if (self.symptoms["fever"] and
            self.symptoms["cough"] and
            self.symptoms["headache"] and
            self.symptoms["rash"]):

            print("You may have Severe Viral Infection")

        # Three Symptoms
        elif (self.symptoms["fever"] and
              self.symptoms["cough"] and
              self.symptoms["headache"]):

            print("You may have Severe Flu")

        elif (self.symptoms["fever"] and
              self.symptoms["headache"] and
              self.symptoms["rash"]):

            print("You may have Serious Infection")

        # Two Symptoms
        elif self.symptoms["fever"] and self.symptoms["cough"]:
            print("You may have Flu")

        elif self.symptoms["fever"] and self.symptoms["headache"]:
            print("You may have Meningitis")

        elif self.symptoms["fever"] and self.symptoms["rash"]:
            print("You may have Measles")

        elif self.symptoms["cough"] and self.symptoms["headache"]:
            print("You may have Cold and Migraine")

        elif self.symptoms["headache"] and self.symptoms["rash"]:
            print("You may have Skin Infection")

        # Single Symptoms
        elif self.symptoms["fever"]:
            print("You may have Viral Infection")

        elif self.symptoms["cough"]:
            print("You may have Common Cold")

        elif self.symptoms["headache"]:
            print("You may have Stress or Migraine")

        elif self.symptoms["rash"]:
            print("You may have Skin Allergy")

        # No Symptoms
        else:
            print("You seem healthy")


# Driver Code
if __name__ == '__main__':

    checker = SymptomChecker()

    checker.ask_symptoms()

    checker.diagnose()