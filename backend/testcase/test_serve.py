import requests


class TestServe:
    def test_get(self):
        r=requests.get("http://localhost:5000/run",params={"name":"tmp1234"})
        assert r.status_code==200