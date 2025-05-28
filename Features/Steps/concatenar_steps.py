from behave import given, when, then
from concatenar import concatenar


@given('que ingreso "{string}"')
def step_given_string(context, string):
    if not hasattr(context, 'strings'):
        context.strings = []
    context.strings.append(string)

@when('realizo la concatenación')
def step_when_conc(context):
    context.resultado = concatenar(context.strings[0], context.strings[1])

@then('el resultado debe ser "{esperado}"')
def step_then_result(context, esperado):
    assert context.resultado == esperado, f"Se esperaba {esperado}, pero se recibió {context.resultado}"