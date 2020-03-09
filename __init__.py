def pytest_configure(config):
    config.addinivalue_line("markers", "bdd: this one is for cool tests.")
