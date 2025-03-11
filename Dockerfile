FROM python:3.8

#establce un directorio dentro del contenedor
WORKDIR /usr/src/app

RUN pip install fastapi 
RUN pip install uvicorn
RUN pip install psycopg2-binary
RUN pip install pyjwt
RUN pip install pyjwt[crypto]
RUN pip install passlib[bcrypt]
RUN pip install -U pytest
RUN pip install requests
RUN pip install sqlalchemy
RUN pip install pyyaml
RUN pip install kubernetes
RUN pip install python-dotenv

#COPY requirements.txt .
#RUN pip install -r requirements.txt


 

#Copia todos los archivos de la carpeta app al directorio de trabajo 
#COPY app/* .
COPY app/ /usr/src/app/

RUN pip list

EXPOSE 8004

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0" ]