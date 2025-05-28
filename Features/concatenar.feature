Feature: Concatenación de dos palabras

    Scenario: Concatenar dos palabras
        Given que ingreso "Hola M"
        And que ingreso "undo"
        When realizo la concatenación
        Then el resultado debe ser "Hola Mundo"