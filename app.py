from dialogs.test_case_dialogs import TestCaseDialog
from services.test_case_register import TestCaseRegister

def main():
    register= TestCaseRegister()
    dialog= TestCaseDialog()
    dialog.show_menu()


if __name__ == "__main__":
    main()




