FROM python:3.8-slim

WORKDIR /app

RUN apt-get update && apt-get install -y postgresql-client

# Copy the ELT script 
COPY . .

CMD [ "python", "elt_script.py" ]