from app import app

def test_home_page_loads():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"NOT a medical device" in response.data

def test_valid_submission_shows_result():
    client = app.test_client()
    response = client.post("/", data={"age": "50", "ast": "40", "alt": "25", "platelets": "200"})
    assert response.status_code == 200
    assert b"2.000" in response.data
    assert b"Indeterminate" in response.data

def test_invalid_submission_shows_error():
    client = app.test_client()
    response = client.post("/", data={"age": "50", "ast": "40", "alt": "25", "platelets": "0"})
    assert response.status_code == 200
    assert b"platelets must be greater than 0" in response.data

def test_blank_input_shows_friendly_error():
    client = app.test_client()
    response = client.post("/", data={"age": "50", "ast": "40", "alt": "", "platelets": "200"})
    assert response.status_code == 200
    assert b"Please enter a number in every box" in response.data
    assert b"could not convert" not in response.data
