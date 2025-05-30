from concatenar.py import concatenar

def test_concatenar():
    assert concatenar("A,", "B") == "A,B"
    assert concatenar("Ho", "la") == "Hola"
    assert concatenar("He", "llo") == "Hello"
    print("Todas las pruebas pasaron.")

test_concatenar()