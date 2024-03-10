# Creating the PostgreSQL User and Database for the Final Project

This document outlines the steps to create the PostgreSQL user and database specifically for the final project both through the terminal, and PgAdmin.

## Database Setup Through the Terminal

First, you need to launch the PostgreSQL session in terminal with the following command:

```
sudo -u postgres psql
```

### Creating the 'postgres' User

The database configuration for the final project specifies a user named 'postgres'.

To create this user, use the `createuser` command in a terminal session:

```
sudo -u postgres createuser --interactive --pwprompt
```

When prompted, enter `postgres` for both the username and password. When asked if the new role should be a superuser, enter `y`. This will give the `postgres` user all the necessary permissions for managing databases.

### Creating the 'FinalProject' Database

The database for the final project is aptly named `FinalProject`. To create this database, use the `createdb` command in a terminal session:

```
createdb -O postgres FinalProject
```

This command creates a new database named `FinalProject` and sets the `postgres` user as the owner.

## Database Setup Through PgAdmin

First, you need to ensure that you have PgAdmin installed on your system. If you do not have it installed, you can download it from the official PgAdmin website.

### Creating the 'postgres' User

To create the `postgres` user through pgAdmin, follow these steps:

- Launch pgAdmin and connect to your PostgreSQL server.
- Right-click on "Login/Group Roles" and select "Create" > "Login/Group Role".
- Enter postgres as the name and set a password.
- In the "Privileges" tab, set "Can login?" to "Yes" and "Superuser?" to "Yes".
- Click "Save" to create the user.

### Creating the 'FinalProject' Database

To create the `FinalProject` database through pgAdmin, follow these steps:

- Launch pgAdmin and connect to your PostgreSQL server.
- Right-click on "Databases" and select "Create" > "Database".
- Enter FinalProject as the database name and select postgres as the owner.
- Click "Save" to create the database.
