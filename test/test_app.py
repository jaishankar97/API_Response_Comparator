import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src/'))
from app import App


class TestApp:

    def test_app(self):
        app_object = App(debug_mode=True)
        resp = app_object.compare_api_responses('https://reqres.in/api/users/3', 'https://reqres.in/api/users/2')
        assert resp is False
        resp = app_object.compare_api_responses('https://reqres.in/api/users/2', '/api/unknown/2')
        assert resp is None
        resp = app_object.compare_api_responses('https://reqres.in/api/users?page=2', 'https://reqres.in/api/users?page=2')
        assert resp is True

TestApp().test_app()
