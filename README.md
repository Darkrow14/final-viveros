# Proyecto Final Viveros

Para instalar correctamente la librerias necesarías en este proyecto es necesario usar el siguiente comando estando ubicado en la carpeta sistema del proyecto
```python
pip install -r requirements.txt
```

## Variables de entorno
Se configuro un archivo que contiene los datos necesarios para la conexión con la base de datos, para ello se debe crear un archivo local llamado ``` .env ``` ubicado en la siguiente ruta ```sistema/sistema/.env``` y en el configurar las siguientes variables:
```enviroment
DB_NAME=proyectovivero
DB_USER=<<YOUR_USER_DB_CONNECTION>>
DB_PASSWORD=<<YOUR_PASSWORD_DB_CONNECTION>>
DB_HOST=<<YOUR_HOST_DB_CONNECTION>>
DB_PORT=<<YOUR_PORT_DB_CONNECTION>>
```
