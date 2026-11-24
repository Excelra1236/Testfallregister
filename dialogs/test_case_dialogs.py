from dataclasses import dataclass, field
from services.test_case_register import TestCaseRegister
from models.test_case import TestCase

@dataclass
class TestCaseDialog:
    register: TestCaseRegister =field(default_factory=TestCaseRegister)

    def show_test_cases(self):
        test_cases =self.register.get_test_cases()
        
        if not test_cases:
            print("\nDet finns inga registrerade testfall")
            return
    
        for test_case in test_cases:
            print(f"Titel:{test_case.titel}")
            print(f"Beskrivning {test_case.beskrivning}")
            print(f"förväntat resultat{test_case.förväntat_resultat}")
            print(f"id: {test_case.id}")

    def register_test_case(self):
        title = input("Titel: ").strip()
        description = input("Beskrivning: ").strip()
        expected_result = input("Förväntat Resultat: ").strip()

        self.register.add_test_case(title, description, expected_result)


    def show_menu(self):
        print("\n Välj bland alternativen")
        while True:
            print( "\n1. Registrera ett Testfall") 
            print( "2. Visa dina Testfall" )
            print("3 Avsluta")

            choice = input("Välj ett alternativ: ").strip()


            match choice:
                case "1":
                    self.register_test_case()
                    

                case "2":
                    print("\ndetta är de registrerade testfallen")
                    self.show_test_cases()


                case "3":
                    print("\n###### Programet är avslutat ######")
                    break

                case _:
                    print("\n### Felaktigt alternativ välj bland 1,2,3 ### ")

            




