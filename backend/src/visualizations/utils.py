import csv

'''
TODO:
get_job_applications is a temporary POC function.
It will be replaced by real DB fetching using an ORM.
'''
def get_job_applications(filename: str = "src/visualizations/applications.csv") -> list[ApplicationSnapshot]:
    job_applications = []
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        for job_application in reader:
            company, date_applied, status = job_application[0], job_application[1], job_application[2]
            job_applications.append(ApplicationSnapshot(company, date_applied, status))
    
    return job_applications