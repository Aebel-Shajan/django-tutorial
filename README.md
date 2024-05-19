

# Setup project
1. Create virtual environment for project
```
python -m venv .venv
```

2. Activate the virtual environment:
  * Windows:
    ```
    venv\Scripts\activate
    ```
  * For macOS/Linux:
    ```
    source venv/bin/activate
    ```

3. Install required dependencies:
```
pip install -r requirements.txt
```

# Making model changes
1. Change your models (in models.py).
2. Run python manage.py makemigrations to create migrations for those changes
3. Run python manage.py migrate to apply those changes to the database.