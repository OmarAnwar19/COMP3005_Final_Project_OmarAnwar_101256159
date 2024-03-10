# COMP 3005 Final Project: Health and Fitness Club Management System

### Assignment Demonstration Video

- [Demo Video](https://youtu.be/xyz)

### Student Name and Number

- Name: Omar Anwar
- Student Number: 101256159

## Problem Statement

This project is a web application built with Flask and Python, designed to manage a Health and Fitness Club. The system serves as a comprehensive platform catering to the diverse needs of club members, trainers, and administrative staff. I completed this project as the only member of my team, and I was responsible for the entire development process, including requirements gathering, design, implementation, and testing.

## Functionality

**Member Functions**

- User Registration
- Profile Management
- Dashboard Display
- Schedule Management

**Trainer Functions**

- Schedule Management
- Member Profile Viewing

**Administrative Staff Functions**

- Room Booking Management
- Equipment Maintenance Monitoring
- Class Schedule Updating
- Billing and Payment Processing

## Implementation

### File Structure and Architecture

The application is built with Flask and Python, and uses a PostgreSQL database to store data. The application follows the MVC architecture, with separate modules for handling database operations, business logic, and the user interface.

The application is structured as follows:

- `/database`: This directory contains files related to setting up the database, including DDL scripts for creating tables and inserting initial data.
- `/routes`: This directory contains the route handlers for the Flask application. Each file corresponds to a different endpoint of the application.
- `/SQL`: This directory contains SQL queries used in the application.
- `/static`: This directory contains static files like CSS and JavaScript files.
- `/templates`: This directory contains the HTML templates for the application. Flask uses these templates to generate the HTML that it sends to the client.
- `/util`: This directory contains utility functions and classes that are used throughout the application.
- `app.py`: This is the main file of the application. It sets up the Flask application and registers the routes.

### Database Design

The database consists of several tables representing entities such as members, trainers, and administrative staff. Relationships between these entities are represented as foreign keys in the tables. The database design is based on the requirements specified in the project spec. ER and Relational diagrams are included with the project report included along with my submission.

## Running the Application

### Prerequisites

- Before you begin, ensure you have installed the latest version of Python and Flask.
- You can download the latest version of Python from the official Python website and the latest version of Flask from the official Flask website.
- In the source directory, please run the following command to install the necessary packages for this application:

```
pip install -r requirements.txt
```

### Setting Up the Database

- Before running the application, you need to make sure you set up the database. Please follow the instructions outlined in the `database/SETUP_DB.md` file to create the necessary database and user.
- After this, please run the query inside the `database/ddl.sql` file in PgAdmin to create the necessary tables in the database.
- Finally, run the query inside the `database/ddl.sql` file in PgAdmin to insert the necessary data into the tables.

### Running the Application

To run the application, please run the following command in the source directory:

```
python app.py
```

Alternatively, you can run the following command to run the application in debug mode:

```
python app.py --debug
```

The application will start running at `http://127.0.0.1:5000/`.

### Using the Application

1. **Installation**: Clone the repository to your local machine and install the necessary dependencies. If you're using pip, you can do this by running `pip install -r requirements.txt` in the project directory.

2. **Setting up the Database**: Ensure you have followed the steps to set-up the appropriate database in PgAdmin, then run the DDL script to set up the database, and the DML script to load sample data into the database.

3. **Starting the Application**: Start the application by running `python app.py` in the terminal. This will start the application on your local machine.

4. **User Registration**: Navigate to the registration page to create a new account. You'll need to provide a username, and password. Each user can be one of three types: member, trainer, or administrative staff. You can select your user type when registering.

5. **User Login**: Once you've registered, you can log in with your username and password. After you're logged in, depending on your user type, you can perform different tasks.

6. **Member Functions**: Members can view their dashboard, which displays exercise routines, fitness achievements, and health statistics. Members can also update their profile information, and schedule personal training sessions or group fitness classes from the schedule management page. The system will ensure that the trainer is available before confirming your booking.

7. **Trainer Functions**: If you're a trainer, you can manage your schedule and view member profiles from the trainer dashboard. You can change your availability, and view the profiles of any members in the system. You can also view the schedule of any member to see if they have any upcoming bookings.

8. **Administrator Functions**: If you're an administrative staff member, you can view all members and trainers in the system. You can also manage room bookings, equipment maintenance, and class schedules. You can also process billing and payments for members, and choose to approve or deny any booking / payment requests.

<br/>

#### Thank you for your time!
