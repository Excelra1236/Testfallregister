from services.test_case_register import TestCaseRegister as Register

def test_nytt_ar_tomt():
    register = Register()

    assert register.get_test_cases() == []


def test_lagg_till_testfall():
    register = Register()

    register.add_test_case(
        "Registera ett testfall",
        "Fyll i titel, beskrivning och förväntat resultat",
        "Testfallet sparas i registret"

    )

    test_cases = register.get_test_cases()

    assert len(test_cases) == 1
    assert test_cases[0].titel == "Registera ett testfall"