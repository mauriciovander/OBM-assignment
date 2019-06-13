#!/bin/sh

DB_NAME=obm
DB_USER=obm
DB_PASSWORD=obm
 
createdb obm
createuser obm
psql $DB_NAME -c "alter user ${DB_USER} with encrypted password '${DB_PASSWORD}';"
psql $DB_NAME -c "grant all privileges on database ${DB_NAME} to ${DB_USER};"