
docker run --name data-engineering-postgres -e POSTGRES_PASSWORD=secret -d postgres

docker exec -u postgres data-engineering-postgres createdb postgres-db

docker exec -it c1b0e2f587fc psql -U postgres -d postgres-db
docker exec -it data-engineering-postgres psql -U postgres -d postgres-db

\l : list db
\dt : list tables
\c postgres-db

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    date_of_birht DATE
);

INSERT INTO users (first_name, last_name, email, date_of_birht) VALUES
('Phil', 'Mbambi', 'philippembambi413@gmail.com', '1999-06-05'),
('Wesley', 'Mawana', 'wesley@gmail.com', '1999-03-09'),
('jackson', 'Mbambi', 'jackson@gmail.com', '1996-04-012'),
('Anne', 'Ebengo', 'anne@gmail.com', '1999-02-10'),
('Rachel', 'Lowa', 'rach@gmail.com', '2000-06-05')
;


default:
  target: dev
  outputs:
    dev:
      type: postgres
      host: "{{ env_var('DBT_ENV_SECRET_HOST') }}"
      user: "{{ env_var('DBT_ENV_SECRET_USER') }}"
      password: "{{ env_var('DBT_ENV_SECRET_PASSWORD') }}"
      port: "{{ env_var('DBT_ENV_SECRET_PORT') }}"
      dbname: "{{ env_var('DBT_ENV_SECRET_DBNAME') }}"
      schema: "{{ env_var('DBT_ENV_SECRET_SCHEMA') }}"

      
# dbt-docker-airflow
