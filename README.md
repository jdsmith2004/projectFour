## PART 1 - Create App

1. Run the REPL Template first to download django
2. (Already done) Run: `python manage.py startapp weather` from the console
3. (Already done) Add `weather` to the `INSTALLED_APPS` in `my_site/settings.py`
4. Run and see Test Page (rocket ship)

## PART 2 - Create Database
1. Create the model for the Observations database table
2. Create the physical database file (repeat these two commands anytime the model file changes):
    * `python manage.py makemigrations`
    * `python manage.py migrate`
3. Add: `admin.site.register(Observation)` to the admin.py file to allow modification of the database from the admin page.  To do this, we also need to create a password here: `python manage.py createsuperuser`
4. Run App and Add Some Observations

## PART 3 - Create First Web Page
1. Modify `my_site/urls.py` to include link to `my_weather` view
2. Create a `my_weather` function in `weather/views.py` to respond to the URL request.
3. Read all data from the database and calculate the mean temperature and use it to render the `display_my_weather.html`.
4. Run the App to view the observations we added manually.

## PART 4 - Respond to POST from HTML Form
1. Modify the form to send the POST back to the `my_weather` function.
2. Modify the `my_weather` function to process the POST request.
3. Run the App to enter our observations from the form.

## PART 5 - Read data from External API 
1. Modify `my_site/urls.py` to include link to `nws_weather` view along with a `site` parameter.
2. Create a `nws_weater` function in `weather/views.py` to respond to the URL request.
3. Read all data from the NWS server and create a list of dictionaries (just like what we would read from the database) and use it to render the `display_nws_weather.html`.
4. Run the App and try different sites.