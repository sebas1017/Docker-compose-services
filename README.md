# INTERCONEXION DE SERVICIOS CON DOCKER-COMPOSE
 ![alt text](https://github.com/sebas1017/flask-faker-app/blob/master/docker.png?raw=true)
 ![alt text](https://github.com/sebas1017/flask-faker-app/blob/master/REQUERIMIENTOS.png?raw=true)

Para correr el proyecto simplemente debe clonarlo en su maquina y en la raiz escribir
docker-compose up


para verificar que todo esta en orden ejecutar el comando
docker ps

y debera ver 4 contenedores activos ejecutandose


esto lo que hara es ejecutar 4 servicios interconectados mediante un bridge  de docker entre si , cada servicio  en su contenedor independiente, 
podra visualizar el servicio web  para interactuar con el sistema en la direccion http://localhost:5002/

este proyecto lo desarrolle de acuerdo a los siguientes requerimientos:
