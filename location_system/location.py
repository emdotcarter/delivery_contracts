from enum import Enum
import sqlite3


class Location:
    def __init__(self, name, x, y, z):
        self._name = name
        self._x = x
        self._y = y
        self._z = z

    def serialize(self):
        return {
            "name": self._name,
            "coordinates": {
                "x": self._x,
                "y": self._y,
                "z": self._z,
            },
        }

    @classmethod
    def find_by_name(cls, name):
        cursor = cls._db_cursor()
        location_row = cursor.execute(
            """
            SELECT l.name, l.x, l.y, l.z
            FROM location l
            WHERE l.name = ?;
            """,
            [name],
        ).fetchone()

        return cls(
            name=location_row[0],
            x=location_row[1],
            y=location_row[2],
            z=location_row[3],
        )

    @classmethod
    def _db_cursor(cls):
        return sqlite3.connect("delivery_contract_system.db")
