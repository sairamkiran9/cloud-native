import requests
import time

def test_grafana_service():
    url = "http://localhost:3000/login"
    for i in range(10):  # Try for 10 times
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print("Grafana is up and running.")
                return True
        except requests.ConnectionError:
            pass
        time.sleep(5)
    print("Grafana is not responding.")
    return False

if __name__ == "__main__":
    assert test_grafana_service(), "Test failed: Grafana service is not running."
