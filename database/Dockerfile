# Use the official PostgreSQL image as the base
FROM postgres:15-alpine

# Set default environment variables (can be overridden by docker-compose)
ENV POSTGRES_DB=assignment_db
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres

# Copy initialization scripts if any
COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 5432
