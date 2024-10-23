# Historia de Usuario

**Como administrador de red**, necesito un protocolo de comunicación que permita a los dispositivos intercambiar datos de forma segura utilizando encriptación y autenticación, para proteger la información sensible en la red.

## Criterios de Aceptación

1. **Autenticación exitosa**:
   - El dispositivo debe autenticarse correctamente con el token "secreto123" antes de que se permita cualquier operación de envío o recepción de mensajes.
   - Si el token es incorrecto, debe lanzarse un error de autenticación.

2. **Comunicación segura**:
   - Una vez autenticado, el dispositivo debe poder enviar mensajes encriptados utilizando un mecanismo seguro (AES).
   - El dispositivo receptor debe ser capaz de desencriptar correctamente el mensaje recibido.

3. **Manejo de errores de autenticación**:
   - Si un dispositivo intenta autenticarse con un token incorrecto, debe recibirse un mensaje de error indicando "Autenticación fallida".

4. **Intento de envío sin autenticación**:
   - Si un dispositivo intenta enviar un mensaje sin estar autenticado, el sistema debe lanzar un error indicando "Usuario no autenticado".

