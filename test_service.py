from unittest import mock

from src.services import _get_trends


def test_get_trends_with_success():
    # Arrange
    mock_api = mock.Mock()
    mock_api.trends_place.return_value = [{
        "trends": [
            {"name": "", "url": ""},
            {"name": "", "url": ""},
        ]
    }]

    # Act
    trends = _get_trends(woe_id=1000, api=mock_api)

    # Assert
    assert trends == [
            {"name": "", "url": ""},
            {"name": "", "url": ""},
        ]


def test_get_trends_without_return_with_success():
    # Arrange
    mock_api = mock.Mock()
    mock_api.trends_place.return_value = [{"trends": []}]

    # Act
    trends = _get_trends(woe_id=1000, api=mock_api)

    # Assert
    assert trends == []
