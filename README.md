
# Task Management App with Google Login

## Highlights and Features

- **Google Authentication**: Users can log in using their Google accounts through OAuth integration.
- **Task Management**: Users can create, view, edit, and delete personal tasks, each having a title and description.
- **Admin Panel**: Admin users can manage Google OAuth credentials and send registration invitation emails to new users.
- **User Roles**: Superusers can configure OAuth credentials and manage users from the Custom Admin panel.

---

## How to Set Up Locally

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/royg-9595/google-auth-app.git
cd <your-project-directory>
```

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to isolate dependencies for the project:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scriptsctivate`
```

### 3. Install Dependencies

Use `requirements.txt` to install all necessary dependencies:

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file for environment-specific settings:

```bash
touch .env
```

Add the variables from `example_env` to your `.env` file:
example:
```bash
DEBUG=True
SECRET_KEY=your-secret-key
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-email-password
```

---

## Step-by-Step Setup

### 1. Apply Database Migrations

After configuring the environment, run migrations to set up your database:

```bash
python manage.py migrate
```

### 2. Create a Superuser

To access the Django admin panel, create a superuser account:

```bash
python manage.py createsuperuser
```

**Note**: You'll need to provide a username and email for the superuser.

### 3. Run the Server

To start the development server:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

### 4. Log in to add the OAuth credentials

Go to `http://127.0.0.1:8000` and log in using the superuser credentials.

---

## Configure Google OAuth Credentials

1. Go to [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing one.
3. Navigate to **APIs & Services > Credentials**.
4. Click **Create Credentials** and select **OAuth 2.0 Client IDs**.
5. Set the application type to **Web application** and configure the **Authorized redirect URIs** as follows:
   ```
   http://127.0.0.1:8000/accounts/google/login/callback/
   ```
6. Save your OAuth credentials, and copy the `Client ID` and `Client Secret`.

---

### 5. Add OAuth Credentials to the Admin Panel

- Go to the Django admin panel (`http://127.0.0.1:8000/admin`).
- Under **Social Applications**, add your **Google OAuth** credentials using the `Client ID` and `Client Secret`.
- After this, your app will be able to authenticate users via Google Login.

---

## How to Get Google OAuth Credentials

Here’s a quick guide on obtaining OAuth credentials from Google Cloud Console:

- **[How to Set Up OAuth 2.0 Credentials in Google Cloud Console](https://developers.google.com/identity/protocols/oauth2)**.

---

Now project should be ready to authenticate users with Google Login!
