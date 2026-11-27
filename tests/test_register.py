from services.test_case_register import TestCaseRegister as Register

def test_new_is_empty():
    register = Register()

    assert register.get_test_cases() == []


def test_add_a_testcase():
    register = Register()

    register.add_test_case(
        "Register a testcase",
        "input Title, Description, Expected Result",
        "Testcase get saved in register"

    )

    test_cases = register.get_test_cases()

    assert len(test_cases) == 1
    assert test_cases[0].title == "Register a testcase"



    