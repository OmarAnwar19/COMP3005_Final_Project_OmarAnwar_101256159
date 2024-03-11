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

The overall application is a web-based platform developed using Flask, a micro web framework written in Python. The application follows the MVC architecture, with separate modules for handling database operations, business logic, and the user interface. The general flow of the application is that the user interacts with the user interface, which sends requests to the Flask application. The Flask application then processes these requests, interacts with the database as necessary, and returns the appropriate response to the user, and the user interface displays this response to the user through different views and templates, which are rendered by the Flask application to the web browser. The application also interacts with a PostgreSQL relational database, which stores and manages all the data related to members, trainers, sessions, rooms, equipment, and more, through the Psycopg2 library.

### File Structure and Architecture

The application is structured as follows:

- `/database`: This directory contains files related to the database, including the database connection settings, and configuration keys.
- `/database/queries`: This directory contains functions for executing SQL queries against the database. These functions are used by the route handlers to interact with the database.
- `/routes`: This directory contains the route handlers for the Flask application. Each file corresponds to a different endpoint of the application.
- `/SQL`: This directory contains SQL queries used in the application, including DDL and DML scripts for creating tables and inserting initial data.
- `/static`: This directory contains static files like CSS and JavaScript files.
- `/templates`: This directory contains the HTML templates for the application. Flask uses these templates to generate the HTML that it sends to the client.
- `/util`: This directory contains utility functions and classes that are used throughout the application.
- `app.py`: This is the main file of the application. It sets up the Flask application and registers the routes.

### Database Design

The database consists of several tables representing entities such as members, trainers, and administrative staff. Relationships between these entities are represented as foreign keys in the tables. The database design is based on the requirements specified in the project spec. ER and Relational diagrams are included with the project report included along with my submission.

### Bonus Features

- **User Authentication**: The application uses a secure authentication system to ensure that only authorized users can access the system. At the moment, passwords are stored in the database in plain text, however, in the future they would be encrypted to ensure a more secure connection.
- **Role-Based Access Control**: The application uses role-based access control to ensure that users can only access the features that are relevant to their role. For example, members can only view their own dashboard, while administrative staff can view and manage all members and trainers.
- **Web Application**: The application is a web application built with Flask, which allows users to access it from any device with a web browser. This was quite a time-consuming task, but means that the application is more accessible and easier to use than a command-line application.
- **Responsive Design**: The application uses responsive design to ensure that it looks good and is easy to use on any device, including desktops, tablets, and smartphones.
- **Data Validation**: The application uses data validation to ensure that users enter valid data when registering, updating their profile, or making bookings. This helps to prevent errors and ensure that the data in the database is accurate.
- **Error Handling**: The application uses error handling to ensure that users receive helpful error messages when something goes wrong. This helps to prevent frustration and confusion when using the application.
- **Session Management**: The application uses session management to ensure that users remain logged in as they navigate the application. This means that users don't have to log in every time they visit a new page, which makes the application more convenient to use.
- **Additional User Functions**: The application includes additional user functions which are not required by the project spec, such as increased administrative staff functions, and the ability for members to modify their cart for bookings.

These features represent significant additional effort, accounting for more than 10% of the overall project workload. They also introduce innovative elements to the system, such as a fully functional web application with server-side session management, and a responsive design that adapts to different screen sizes. These features are not only functional, but also add significant value to the system, making it more user-friendly and accessible, while meeting all the requirements of the project spec.

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
