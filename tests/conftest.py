from unittest.mock import Mock
import pytest


@pytest.fixture()
def mock_stack():
    mock = Mock()
    mock.id = 111
    mock.stack = [1, 2, 3]
    return mock
