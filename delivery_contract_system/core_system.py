import itertools
import random
import sqlite3

from delivery_contract_system.contract import Contract


class DeliveryContractSystem:
    @classmethod
    def request_contract(cls):
        contract_id = cls._select_contract_id()

        return Contract.find_by_id(contract_id)

    @classmethod
    def _db_cursor(cls):
        return sqlite3.connect("delivery_contract_system.db")

    @classmethod
    def _select_contract_id(cls):
        cursor = cls._db_cursor()
        ids = cursor.execute(
            """
            SELECT c.id
            FROM contract c
            JOIN contract_status cs
              ON cs.contract_id = c.id
            WHERE cs.status = ?;
            """,
            [Contract.Status.OPEN.value],
        ).fetchall()

        return random.choice(list(itertools.chain(*ids)))
