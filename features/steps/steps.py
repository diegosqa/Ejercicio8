from behave import given, when, then
from protocolo.protocol import Protocol

@given('el dispositivo A tiene el token "{token}"')
def step_impl(context, token):
    context.protocol_A = Protocol(token)

@given('el dispositivo A está autenticado con "{token}"')
def step_impl(context, token):
    context.protocol_A.authenticate(token)

@when('el dispositivo A envía un mensaje "{message}"')
def step_impl(context, message):
    context.encrypted_message = context.protocol_A.send_message(message)

@then('el dispositivo B debe recibir el mensaje "{expected_message}" correctamente desencriptado')
def step_impl(context, expected_message):
    decrypted_message = context.protocol_A.receive_message(context.encrypted_message)
    assert decrypted_message == expected_message

@when('el dispositivo A intenta autenticarse con "{token_incorrecto}"')
def step_impl(context, token_incorrecto):
    try:
        context.protocol_A.authenticate(token_incorrecto)
    except ValueError as e:
        context.auth_error = str(e)

@then('debe aparecer un error de "Autenticación fallida"')
def step_impl(context):
    assert context.auth_error == "Error: Autenticación fallida"

@when('el dispositivo A intenta enviar un mensaje "{message}" sin autenticarse')
def step_impl(context, message):
    try:
        context.protocol_A.send_message(message)
    except ValueError as e:
        context.auth_error = str(e)

@then('debe aparecer un error de "Usuario no autenticado"')
def step_impl(context):
    assert context.auth_error == "Error: Usuario no autenticado"

