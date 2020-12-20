from enum import Enum
import itertools
import sqlite3


class Contract:
    class Status(Enum):
        OPEN = "open"
        ACTIVE = "active"
        COMPLETE = "complete"

    def __init__(self, id, item, crew_size, crew_conditions, destination, status):
        self._id = id
        self._item = item
        self._crew_size = crew_size
        self._crew_conditions = crew_conditions
        self._destination = destination
        self._status = status

    def serialize(self):
        return {
            "id": self._id,
            "item": self._item,
            "crew_requirements": {
                "size": self._crew_size,
                "conditions": self._crew_conditions,
            },
            "destination": self._destination,
        }

    @classmethod
    def find_by_id(cls, id):
        cursor = cls._db_cursor()
        contract_row = cursor.execute(
            """
            SELECT c.id, c.item, c.crew_size, c.destination, cs.status
            FROM contract c
            JOIN contract_status cs on cs.contract_id = c.id
            WHERE c.id = ?;
            """,
            [id],
        ).fetchone()

        crew_conditions = cls._crew_conditions_for_contract(id)

        return Contract(
            contract_row[0],
            contract_row[1],
            contract_row[2],
            crew_conditions,
            contract_row[3],
            contract_row[4],
        )

    @classmethod
    def _db_cursor(cls):
        return sqlite3.connect("delivery_contract_system.db")

    @classmethod
    def _crew_conditions_for_contract(cls, contract_id):
        cursor = cls._db_cursor()
        conditions = cursor.execute(
            """
            SELECT cc.condition
            FROM crew_condition cc
            WHERE cc.contract_id = ?;
            """,
            [contract_id],
        ).fetchall()

        return list(itertools.chain(*conditions))
