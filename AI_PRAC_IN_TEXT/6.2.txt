# Expert System for Employee Performance Evaluation

class EmployeePerformance:

    def __init__(self):

        self.data = {
            "timely_completion": False,
            "appreciation": False,
            "innovation": False,
            "attendance": 0,
            "projects_completed": False,
            "time_taken": False,
            "teamwork": False,
            "client_feedback": False
        }

        self.score = 0

    # Taking Employee Input
    def get_input(self):

        print("Please answer with yes or no\n")

        self.name = input("Enter Employee Name: ")

        if input("Timely Completion of Tasks? ").lower() in ["yes", "y"]:
            self.data["timely_completion"] = True

        if input("Received Appreciation? ").lower() in ["yes", "y"]:
            self.data["appreciation"] = True

        if input("Innovation Offered? ").lower() in ["yes", "y"]:
            self.data["innovation"] = True

        self.data["attendance"] = int(input("Attendance Percentage: "))

        if input("Projects Completed More Than Target? ").lower() in ["yes", "y"]:
            self.data["projects_completed"] = True

        if input("Completed Work Before Expected Time? ").lower() in ["yes", "y"]:
            self.data["time_taken"] = True

        if input("Good Teamwork? ").lower() in ["yes", "y"]:
            self.data["teamwork"] = True

        if input("Positive Client Feedback? ").lower() in ["yes", "y"]:
            self.data["client_feedback"] = True

    # Evaluating Performance
    def evaluate(self):

        # Timely Completion
        if self.data["timely_completion"]:
            self.score += 1
        else:
            self.score -= 1

        # Appreciation
        if self.data["appreciation"]:
            self.score += 1

        # Innovation
        if self.data["innovation"]:
            self.score += 1

        # Attendance
        if self.data["attendance"] >= 90:
            self.score += 1

        elif self.data["attendance"] < 75:
            self.score -= 1

        # Projects Completed
        if self.data["projects_completed"]:
            self.score += 1
        else:
            self.score -= 1

        # Time Taken
        if self.data["time_taken"]:
            self.score += 1
        else:
            self.score -= 1

        # Teamwork
        if self.data["teamwork"]:
            self.score += 1
        else:
            self.score -= 1

        # Client Feedback
        if self.data["client_feedback"]:
            self.score += 1
        else:
            self.score -= 1

    # Final Result
    def result(self):

        final_score = 5 + ((self.score + 8) / 16) * 5

        print("\nEmployee Performance Report")
        print("Employee Name:", self.name)

        print("Performance Score:", round(final_score, 2))

        if final_score >= 9:

            if self.data["innovation"] and self.data["appreciation"]:
                print("Evaluation Result: Outstanding")

            else:
                print("Evaluation Result: Excellent")

        elif final_score >= 7:

            if self.data["attendance"] < 80:
                print("Evaluation Result: Good (Needs Attendance Improvement)")

            else:
                print("Evaluation Result: Good")

        elif final_score >= 6:
            print("Evaluation Result: Average")

        else:
            print("Evaluation Result: Needs Improvement")


# Driver Code
if __name__ == '__main__':

    employee = EmployeePerformance()

    employee.get_input()

    employee.evaluate()

    employee.result()