class SymptomChecker:
    def __init__(self):
        self.symptoms = { 
        "fever": False,
        "cough": False,
        "headache": False,
        "rash":False}
        
    def ask_symptoms(self):
        print("Please answer with Yes or No")
        for symptom in self.symptoms:
            response = input (f"Do you have {symptom} ?").lower()
            if response == "yes":
                self.symptoms[symptom] = True
                
    def diagnose(self):
        if self.symptoms["fever"] and self.symptoms["cough"]:
            print("You May Have Flu .")
        elif self.symptoms["fever"] and self.symptoms["headache"]:
            print("You May Have A Meningtitis .")
        elif self.symptoms["fever"] and self.symptoms["rash"]:
            print("You May Have Measles .")
        elif self.symptoms["headache"] and self.symptoms["fever"]:
            print("You May Have Tension Headache .")
        else:
            print("Its difficult to diagnose with the given symptoms")
            
if __name__ == '__main__':
    checker = SymptomChecker()
    checker.ask_symptoms()
    checker.diagnose()
    