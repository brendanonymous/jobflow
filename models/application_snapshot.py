from datetime import datetime, timedelta

class StatusLabelGenerationError(Exception):
    pass

class ApplicationSnapshot:
    def __init__(self, company, applied_date_string, status_string: str):
        self.company = company
        self.applied_date = datetime.strptime(applied_date_string, "%m/%d/%Y")
        self.status_string = status_string

        self.status_path = []
        status_symbols = self.status_string.split(",")
        self.status_path.append("Applied")
        
        for i, status_symbol in enumerate(status_symbols):
            if status_symbol == "":
                break
            try:
                status_label = self.__get_status_string(status_symbol) + (f" {i + 1}" if status_symbol == "I" else "")
                self.status_path.append(status_label)
            except StatusLabelCreationError as e:
                print("error occurred while generating a status label: {e}")
        
        if len(self.status_path) == 1 and self.applied_date + timedelta(days=30) <= datetime.today():
            self.status_path.append("Ghosted")

        
    def __get_status_string(self, status_symbol: str) -> str:
        if status_symbol == "A":
            return "Applied"
        if status_symbol == "I":
            return "Interview"
        if status_symbol == "R":
            return "Rejected"
        if status_symbol == "O":
            return "Offer"
        if status_symbol == "G":
            return "Ghosted"