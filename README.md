# Django Tutorial
Followed tutorial from https://docs.djangoproject.com/en/5.0/intro/tutorial01/.

Lessons learned:
* Django is used to create static full stack server side website.
* Django rest framework is used to create apis
* Django makes use of the model, view, template design pattern.
* You can use shortcuts from django.shortcuts to cut down on code that gets repeated across multiple projects.
* You can use generic views to replace writing out views in full by hand.
* Pycache is not important, you should put it in gitignore

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
