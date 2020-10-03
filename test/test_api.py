import unittest

import requests
from run import app
import pytest
import json

FLASK_PORT = 5000
get_url = 'http://localhost:{port}'.format(port=FLASK_PORT)
patient_URL = '{}/patients/'.format(get_url)

class ApiTest(unittest.TestCase):

    def test_get(self):
        response = requests.get(patient_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()),2)


if __name__ == "__main__":
    unittest.main()