# Proyecto Final Python - Web estilo blog

Web con sistema de usuarios con el fin de crear post relacionados a reviews de peliculas para que estos puedan subir sus opiniones y comentar en otros post.

## Instalación 

Adicional al uso normal solo necesitamos Pillow (10.4.0 usado en mi caso)

Comandos:
   - python manage.py makemigrations (Si no funciona ejecutar: python manage.py makemigrations reviews users)
   - python manage.py migrate
   - python manage.py runserver

### Funciones

- Página de inicio: Una pequeña presentación de la web
- Barra de navegación (No logeado):
    - Barra de búsqueda: Permite buscar post por título
    - Todos los posts: Lista todos los post que se encuentran cargados
    - Sobre Mi: Detalles acerca del creador de la web
    - Iniciar sesión: Permite al usuario ingresar si es que ya tiene una cuenta
    - Registro: Permite registrar nuevos usuarios

- Barra de navegación (Logeado):
    - Barra de búsqueda: Permite buscar post por título
    - Todos los posts: Lista todos los post que se encuentran cargados
    - Crear Post: Permite al usuario crear un post mediante un formulario
    - Mis Post: Lista todos los post creados por el usuario logeado
    - Sobre Mi: Detalles acerca del creador de la web
    - Dropdown con nombre de usuario:
        - Mi perfil: Permite al usuario ver sus datos
        - Editar perfil: Permite al usuario modificar sus datos
        - Cambiar contraseña: Permite al usuario modificar su contraseña

- Posts: Solo pueden modificar o eliminar los usuarios creadores del post, pero a su vez tambien puede hacerlo un admin en caso de tener que moderar. Distintos usuarios pueden hacer comentarios en cualquier post, pero solo el dueño del comentario puede eliminar o modificar el mismo, los admin tambien pueden eliminar o modificar cualquier comentario en caso de tener que moderar.

- Vista de Admin: Los admin poseen su cuenta de superusuario con la que pueden Ver, editar o eliminar cualquier post creado por cualquier usuario como asi tambien comentarios de cualquier post. Los admin no pueden crear post, ya que su función es simplemente la de moderar, si un admin deseara hacer un post debería tener una cuenta de usuario común.
    
#### Video demostrativo

https://youtu.be/fhm_mnStEiY
