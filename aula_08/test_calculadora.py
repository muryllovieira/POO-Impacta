from calculadora import Calculadora


def test_01_soma_0_0():
    calc = Calculadora()
    assert calc.soma(0, 0) == 0


def test_02_soma_0_10():
    calc = Calculadora()
    assert calc.soma(0, 10) == 0
    assert calc.soma(10, 0) == 10


def test_03_soma_3_5():
    calc = Calculadora()
    assert calc.soma(3, 5) == 8
    assert calc.soma(5, 3) == 8


def test_04_substrai_10_2():
    calc = Calculadora()
    assert calc.subtrai(10, 2) == 8
    

def test_05_substrai_2_10():
    calc = Calculadora()
    assert calc.subtrai(2, 10) == -8
