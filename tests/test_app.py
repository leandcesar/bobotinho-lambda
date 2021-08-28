# -*- coding: utf-8 -*-
from unittest.mock import MagicMock

import pytest
from chalice.test import Client

from app import app, db


@pytest.fixture
def prepare_db() -> None:
    """Prepare database data for testing."""
    db.init()
    db.execute("DELETE FROM public.user WHERE id IN (1, 2);")
    db.execute("DELETE FROM public.cookie WHERE id IN (1, 2);")
    db.execute(
        "INSERT INTO public.user (id, name, sponsor) VALUES(%s, %s, %s);",
        (1, "user_1", True),
    )
    db.execute(
        "INSERT INTO public.user (id, name, sponsor) VALUES(%s, %s, %s);",
        (2, "user_2", False),
    )
    db.execute(
        "INSERT INTO public.cookie (id, name, daily) VALUES(%s, %s, %s);",
        (1, "user_1", 0),
    )
    db.execute(
        "INSERT INTO public.cookie (id, name, daily) VALUES(%s, %s, %s);",
        (2, "user_2", 0),
    )
    db.close()


def test_reset_daily(prepare_db) -> None:
    """Test the "reset-daily" Lambda function.

    Args:
        prepare_db (fixture): prepare database data for testing
    """
    with Client(app) as client:
        result = client.lambda_.invoke("reset-daily", MagicMock())
        assert result.payload is True
    db.init()
    assert db.fetch("SELECT daily FROM public.cookie WHERE id = 1;") == [(2,)]
    assert db.fetch("SELECT daily FROM public.cookie WHERE id = 2;") == [(1,)]
    db.close()
