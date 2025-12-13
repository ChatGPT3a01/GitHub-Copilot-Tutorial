import json
import tempfile
import os
from unittest.mock import patch
from practice9 import is_valid_email, is_prime, remove_duplicates, days_between_dates, read_json_file, fetch_json_from_url

def test_is_valid_email_valid():
    assert is_valid_email("test@example.com") == True
    assert is_valid_email("user.name+tag@example.co.uk") == True

def test_is_valid_email_invalid():
    assert is_valid_email("invalid-email") == False
    assert is_valid_email("test@") == False
    assert is_valid_email("@example.com") == False
    assert is_valid_email("test@example") == False

def test_is_prime_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(7) == True
    assert is_prime(11) == True

def test_is_prime_not_prime():
    assert is_prime(1) == False
    assert is_prime(0) == False
    assert is_prime(-1) == False
    assert is_prime(4) == False
    assert is_prime(9) == False

def test_remove_duplicates():
    assert remove_duplicates([1, 2, 2, 3, 3, 3]) == [1, 2, 3]
    assert remove_duplicates(["a", "b", "a"]) == ["a", "b"]
    assert remove_duplicates([]) == []

def test_days_between_dates():
    assert days_between_dates("2023-01-01", "2023-01-02") == 1
    assert days_between_dates("2023-01-01", "2023-01-01") == 0
    assert days_between_dates("2023-01-02", "2023-01-01") == 1

def test_read_json_file():
    test_data = {"key": "value", "number": 42}
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json.dump(test_data, f)
        temp_file = f.name
    try:
        result = read_json_file(temp_file)
        assert result == test_data
    finally:
        os.unlink(temp_file)

@patch('requests.get')
def test_fetch_json_from_url(mock_get):
    mock_response = mock_get.return_value
    mock_response.json.return_value = {"data": "test"}
    result = fetch_json_from_url("http://example.com")
    assert result == {"data": "test"}
    mock_get.assert_called_once_with("http://example.com")