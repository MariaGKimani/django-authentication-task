# Django User Authentication Assignment

This project is a Django application created as part of an internship assignment. It implements a user authentication system with essential features, providing a secure and user-friendly interface.

## Features

1. **Login Page**:
   - Fields for Username/Email and Password.
   - Links to Sign Up and Forgot Password pages.

2. **Sign Up Page**:
   - Fields for Username, Email, Password, and Confirm Password.
   - A link to return to the Login page.

3. **Forgot Password Page**:
   - Input field for Email.
   - Sends a password reset email with instructions.

4. **Change Password Page**:
   - Accessible only to authenticated users.
   - Fields for Old Password, New Password, and Confirm Password.
   - A link to return to the Dashboard.

5. **Dashboard**:
   - Displays a personalized greeting for logged-in users.
   - Links to the Profile page and Change Password page.
   - Logout option.

6. **Profile Page**:
   - Displays user details (Username, Email, Date Joined, Last Updated).
   - Links to the Dashboard.
   - Logout option.

## Installation and Setup

1. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

4. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

5. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

6. **Access the application in your browser at:**

    [http://127.0.0.1:8000](http://127.0.0.1:8000)
