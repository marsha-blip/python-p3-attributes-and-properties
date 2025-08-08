APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

import string

class Person:
    def __init__(self, name: str = "John Doe", job: str = "Admin"):
        self.name = name  # triggers setter with validation & formatting
        self.job = job    # triggers setter with validation

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str) or not (1 <= len(value) <= 25):
            print("Name must be string between 1 and 25 characters.")
        else:
            # title-case conversion using standard method
            formatted = string.capwords(value)
            self._name = formatted

    @property
    def job(self) -> str:
        return self._job

    @job.setter
    def job(self, value: str):
        if value not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
        else:
            self._job = value

