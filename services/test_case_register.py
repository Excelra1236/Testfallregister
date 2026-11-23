from models.test_case import TestCase
from dataclasses import dataclass, field


@dataclass
class TestCaseRegister:
    test_cases: list[TestCase] = field(default_factory=list)  


    def add_test_case(self, title: str, description: str, expected_result:str):
        test_case = TestCase(title, description, expected_result)
        self.test_cases.append(test_case)
        return test_case


    def get_test_cases(self):
        return self.test_cases
        



        






