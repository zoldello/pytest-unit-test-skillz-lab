import pytest


# Add fixtures files and plugins here
pytest_plugins = [
    'fixture_set.fixtures',
]


# Fixtures also added directly in conftest.py
@pytest.fixture
def fixture_from_conftest():
    return 4
