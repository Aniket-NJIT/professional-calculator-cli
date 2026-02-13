import pytest
from faker import Faker

fake = Faker()

@pytest.fixture
def fake_numbers():
    """Generates a tuple of two random floats."""
    return (fake.random_number(digits=2), fake.random_number(digits=2))