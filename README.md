
docker run --name data-engineering-postgres -e POSTGRES_PASSWORD=secret -d postgres

docker exec -u postgres data-engineering-postgres createdb postgres-db

docker exec -it c1b0e2f587fc psql -U postgres -d postgres-db
docker exec -it data-engineering-postgres psql -U postgres -d postgres-db

\l : list db
\dt : list tables
\c postgres-db


# dbt-docker-airflow
