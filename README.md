# Weather Query Web Application

This is a simple web application built on Django that allows users to request the current weather by entering a city name using the OpenWeatherMap API, and it saves the query history in a PostgreSQL database.

## Features

- **Weather Retrieval:** Enter a city name and get the current weather (temperature, description).
- **Query Storage:** Each query (city name, query timestamp, temperature, description) is saved in the database.
- **Query History Display:** View a list of previous queries.

## Technology Stack

- **Language:** Python
- **Web Framework:** Django with Jinja2 templates
- **Database:** PostgreSQL
- **Docker:** For containerizing the application and the database

## Prerequisites

- [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) must be installed.
- An API key from [OpenWeatherMap](https://openweathermap.org).

## Installation and Running

1. **Clone the repository:**

   ```bash
   git clone https://github.com/AlexisIndustries/python-weather-app
   cd python-weather-app
   ```

2. **Configure environment variables:**

   - In the `docker-compose.yml` file, replace `your_db_user` and `your_db_password` with your PostgreSQL credentials.
   - In the `docker-compose.yml` file, replace `'OWM_API_KEY'` with your OpenWeatherMap API key.
   - Adjust `weather_project/settings.py` to use environment variables if needed.

3. **Build and start the containers:**

   ```bash
   docker-compose up --build
   ```

   The application will be accessible at [http://localhost:8000](http://localhost:8000).

4. **Run Migrations (if necessary):**

   If migrations are not automatically executed, run:

   ```bash
   docker-compose run web python manage.py migrate
   ```

## Project Structure

```
weather_project/
├── manage.py
├── weather_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── jinja2.py
├── weather/
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── weather/
│           ├── index.html
│           └── history.html
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Testing

You can run tests with:

```bash
docker-compose run web python manage.py test
```

## Additional Notes

- **Docker:** The Dockerfile and docker-compose.yml files allow for easy deployment of the application along with the PostgreSQL database.
- **Configuration:** Ensure that you properly configure environment variables for the PostgreSQL connection and the API key.
- **Extensibility:** You can add a Docker volume for PostgreSQL data persistence and set up CI/CD for automated deployment.

## License

This project is licensed under the MIT License.
```