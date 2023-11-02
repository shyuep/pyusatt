from __future__ import annotations

from usatt._data import get_ratings


def test_get_ratings(usattid):
    ratings = get_ratings(usattid)
    assert ratings["USATT#"] == usattid
    assert ratings["Name"] == "Lily Zhang"
