from dataclasses import dataclass, field
from services.test_case_register import TestCaseRegister
from models.test_case import TestCase

@dataclass
class TestCaseDialog:
    register: TestCaseRegister =field(default_factory=TestCaseRegister)

    def show_test_cases(self):
        test_cases =self.register.get_test_cases()
        
        if not test_cases:
            print("\nThere are no registerd Test Cases")
            return
    
        for test_case in test_cases:
            print(f"Title:{test_case.title}")
            print(f"Descriptiom {test_case.description}")
            print(f"Expected Result{test_case.expected_result}")
            print(f"id: {test_case.id}")

    def register_test_case(self):
        title = input("Title: ").strip()
        description = input("Description: ").strip()
        expected_result = input("Expected Result: ").strip()

        self.register.add_test_case(title, description, expected_result)


    def show_menu(self):
        print("\n Choose one of these options")
        while True:
            print( "\n1. Register a Test Case") 
            print( "2. Show your registerd Test Cases" )
            print("3 Exit program")

            choice = input("Choose a option: ").strip()


            match choice:
                case "1":
                    self.register_test_case()
                    

                case "2":
                    print("\nThese are the registerd test cases")
                    self.show_test_cases()


                case "3":
                    print("\n###### The program has ended ######")
                    break

                case _:
                    print("\n### Invalid option choose between 1,2 or 3 ### ")

            




