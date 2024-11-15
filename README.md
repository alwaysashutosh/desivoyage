# Desivoyage - Travel Website

DesiVoyage is a web-based travel booking platform built using Django. This application allows users to book travel packages by specifying destinations, travel dates, class preferences, and additional services. The project demonstrates basic Django features such as form handling, model management, and data storage with SQLite.

## Features

- User registration and authentication system
- Travel Booking Form: A user-friendly form to capture travel details, including destination, departure city, travel dates, number of travelers, travel class, and additional options
- Customizable Travel Packages: Allows users to choose options like accommodation and activities for personalized travel experiences
- Data Storage and Management: Saves user bookings to a database with Django models
- Admin Interface: Manage and view bookings through Django's admin interface.
- Dynamic Styling: Beautiful UI with CSS and background image integration for a modern, clean design.
- Efficiently running on local host , working on production deployment




## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/alwaysashutosh/desivoyage.git
   ```

2. Navigate to the project directory:

   ```bash
   cd desivoyage
   ```

3. Create a virtual environment:

   ```bash
   python -m venv env
   ```

4. Activate the virtual environment:

   - For Windows:
     ```bash
     env\Scripts\activate
     ```
   - For macOS and Linux:
     ```bash
     source env/bin/activate
     ```

5. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

7. Start the development server:

   ```bash
   python manage.py runserver
   ```

8. Open your web browser and visit `http://localhost:8000` to access the application.


