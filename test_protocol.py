import pytest
from protocolo.protocol import Protocol

# Test 1: Autenticación y envío de un mensaje encriptado
def test_encryption_and_authentication():
    # Arrange
    token = "secreto123"
    protocol = Protocol(token)
    protocol.authenticate(token)
    message = "Hola Mundo"
    
    # Act
    encrypted_message = protocol.send_message(message)
    decrypted_message = protocol.receive_message(encrypted_message)
    
    # Assert
    assert decrypted_message == message

# Test 2: Fallo de autenticación
def test_authentication_failure():
    # Arrange
    token_correcto = "secreto123"
    token_incorrecto = "incorrecto"
    protocol = Protocol(token_correcto)
    
    # Act & Assert
    with pytest.raises(ValueError, match="Autenticación fallida"):
        protocol.authenticate(token_incorrecto)

# Test 3: Fallo de envío por falta de autenticación
def test_send_without_authentication():
    # Arrange
    protocol = Protocol("secreto123")
    message = "Hola Mundo"
    
    # Act & Assert
    with pytest.raises(ValueError, match="Usuario no autenticado"):
        protocol.send_message(message)

