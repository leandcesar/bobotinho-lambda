# -*- coding: utf-8 -*-
from typing import Optional

import psycopg2
from psycopg2.extensions import connection, cursor


class Database:
    """Database interface with psycopg2."""

    def __init__(self, name: str, user: str, password: str, host: str, port: str) -> None:
        """Create a new Database instance.

        Args:
            name (str): the database name
            user (str): user name used to authenticate
            password (str): password used to authenticate
            host (str): database host address
            port (str): connection port number
        """
        self.config: dict = {
            "database": name,
            "user": user,
            "password": password,
            "host": host,
            "port": port,
        }
        self.conn: Optional[connection] = None
        self.cur: Optional[cursor] = None

    def init(self) -> None:
        """Create a new database connection and cursor."""
        self.conn: connection = psycopg2.connect(**self.config)
        self.cur = self.conn.cursor()

    def close(self) -> None:
        """Close the cursor and the database connection."""
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()

    def fetch(self, query: str) -> list:
        """Execute query and return rows of a result set.

        Args:
            query (str): SQL query

        Returns:
            list: all the remaining rows of a query result set
        """
        self.cur.execute(query)
        result: Optional[list] = self.cur.fetchall()
        return result or []

    def execute(self, query: str) -> None:
        """Execute query with bound variables and commit all changes to database.

        Args:
            query (str): SQL query
        """
        self.cur.execute(query)
        self.conn.commit()
