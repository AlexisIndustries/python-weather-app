from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch, MagicMock
from .models import QueryHistory

class WeatherQueryTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_weather_query_view(self):
        """
        Check that a GET request to the 'weather_query' view
        returns a 200 status code and uses the correct template.
        """
        response = self.client.get(reverse('weather_query'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    @patch('weather.views.requests.get')
    def test_post_weather_query_success(self, mock_get):
        """
        Verify proper handling of a POST request.
        When the API responds successfully, the record is saved in the database,
        and the result is displayed on the page.
        """
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "main": {"temp": 25.0},
            "weather": [{"description": "clear sky"}]
        }
        mock_get.return_value = mock_response

        response = self.client.post(reverse('weather_query'), {'city': 'Moscow'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(QueryHistory.objects.count(), 1)
        query = QueryHistory.objects.first()
        self.assertEqual(query.city_name, 'Moscow')
        self.assertEqual(query.temperature, 25.0)
        self.assertEqual(query.description, 'clear sky')
        self.assertContains(response, "Weather in Moscow")

    @patch('weather.views.requests.get')
    def test_post_weather_query_failure(self, mock_get):
        """
        Check that when the API returns an unsuccessful response (e.g., 404),
        no record is saved and an error message is displayed.
        """
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        response = self.client.post(reverse('weather_query'), {'city': 'InvalidCity'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(QueryHistory.objects.count(), 0)
        self.assertContains(response, "City not found or API error")

class QueryHistoryTests(TestCase):
    def setUp(self):
        self.client = Client()
        QueryHistory.objects.create(city_name="Moscow", temperature=20.0, description="clear sky")
        QueryHistory.objects.create(city_name="London", temperature=15.0, description="cloudy")

    def test_query_history_view(self):
        """
        Verify that the query history view returns a 200 status code,
        uses the correct template, and displays the created records.
        """
        response = self.client.get(reverse('query_history'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'history.html')
        self.assertContains(response, "Moscow")
        self.assertContains(response, "London")

