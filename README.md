
# Flask Image Upload Application

This is a simple Flask application that allows users to upload two images. The images are temporarily saved to the `uploads/images` directory and then deleted after the post function execution completes.

## Folder Structure
```
flask_app/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── main/
│   │   ├── __init__.py
│   │   ├── routes.py
│   └── static/
│       └── uploads/
│           └── images/
├── venv/
├── requirements.txt
└── run.py
```

## Setup and Installation

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd flask_app
   ```

2. **Create Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scriptsctivate`
   ```

3. **Install Requirements**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Environment Variables** (optional):
   ```bash
   export FLASK_APP=run.py
   export FLASK_ENV=development
   ```

## Running the Application

### Using Flask Development Server

1. **Run the Application**:
   ```bash
   flask run
   ```

2. **Open your browser** and go to `http://127.0.0.1:5000` to access the application.

### Using Gunicorn

1. **Install Gunicorn**:
   ```bash
   pip install gunicorn
   ```

2. **Run the Application with Gunicorn**:
   ```bash
   gunicorn -w 4 -b 127.0.0.1:5000 run:app
   ```

   - `-w 4` specifies 4 worker processes.
   - `-b 127.0.0.1:5000` binds the server to `127.0.0.1` on port `5000`.

3. **Open your browser** and go to `http://127.0.0.1:5000` to access the application.

## Application Details

- **Configuration**: Configuration settings are stored in `app/config.py`.
- **Routes**: The main routes for the application are defined in `app/main/routes.py`.
- **Templates**: HTML templates are located in the `app/main/templates` directory.
- **Uploads**: Uploaded images are temporarily stored in `app/static/uploads/images`.

## License

This project is licensed under the MIT License.
