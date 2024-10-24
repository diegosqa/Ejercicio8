Feature: Protocolo de comunicación seguro

  Scenario: Comunicación exitosa entre dispositivos autenticados
    Given el dispositivo A tiene el token "secreto123"
    And el dispositivo A está autenticado con "secreto123"
    When el dispositivo A envía un mensaje "Hola Mundo"
    Then el dispositivo B debe recibir el mensaje "Hola Mundo" correctamente desencriptado

  Scenario: Fallo de autenticación por token incorrecto
    Given el dispositivo A tiene el token "secreto123"
    When el dispositivo A intenta autenticarse con "incorrecto"
    Then debe aparecer un error de "Autenticación fallida"

  Scenario: Intento de enviar mensaje sin autenticación
    Given el dispositivo A tiene el token "secreto123"
    When el dispositivo A intenta enviar un mensaje "Hola Mundo" sin autenticarse
    Then debe aparecer un error de "Usuario no autenticado"
