from src.estudiante import aprobo

def test_aprobado():
    assert aprobo(11) == "aprobado"

def test_aprobado_nota_alta():
    assert aprobo(18) == "aprobado"

def test_desaprobado():
    assert aprobo(10) == "desaprobado"

def test_desaprobado_nota_baja():
    assert aprobo(5) == "desaprobado"

def test_aprobado_nota_limite():
    assert aprobo(10.5) == "aprobado"
    
    