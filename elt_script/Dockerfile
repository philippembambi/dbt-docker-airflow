FROM python:3.8-slim

WORKDIR /app
# Install PostgreSQL command-line tools
RUN apt-get update && apt-get install -y postgresql-client-15

# Copy the ELT script 
COPY . .

# Set the default command to run the ELT script
CMD ["python", "elt_script.py"]