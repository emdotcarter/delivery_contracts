import datetime
import sqlite3

from resources.contracts import contracts

db_connection = sqlite3.connect("delivery_contract_system.db")
cursor = db_connection.cursor()

cursor.execute(
    """
    DROP TABLE IF EXISTS contract;
    """
)

cursor.execute(
    """
    CREATE TABLE contract
    (
        id INTEGER PRIMARY KEY NOT NULL,
        item TEXT NOT NULL,
        crew_size INTEGER NOT NULL,
        destination TEXT NOT NULL
    );
    """
)

cursor.execute(
    """
    DROP TABLE IF EXISTS crew_condition;
    """
)

cursor.execute(
    """
    CREATE TABLE crew_condition
    (
        id INTEGER PRIMARY KEY NOT NULL,
        condition TEXT NOT NULL,
        contract_id INTEGER NOT NULL,
        FOREIGN KEY(contract_id) REFERENCES contract(id)
    );
    """
)

cursor.execute(
    """
    DROP TABLE IF EXISTS contract_status;
    """
)

cursor.execute(
    """
    CREATE TABLE contract_status
    (
        id INTEGER PRIMARY KEY NOT NULL,
        contract_id INTEGER NOT NULL,
        status TEXT NOT NULL,
        updated_at DATETIME,
        FOREIGN KEY(contract_id) REFERENCES contract(id)
    );
    """
)

for c in contracts:
    cursor.execute(
        """
        INSERT INTO contract (item, crew_size, destination)
        VALUES (?, ?, ?);
        """,
        (c["item"], c["crew"]["size"], c["destination"]),
    )
    contract_id = cursor.execute(
        """
        SELECT last_insert_rowid();
        """
    ).fetchone()[0]

    for r in c["crew"]["conditions"]:
        cursor.execute(
            """
            INSERT INTO crew_condition (condition, contract_id)
            VALUES (?, ?);
            """,
            (r, contract_id),
        )

    cursor.execute(
        """
            INSERT INTO contract_status (contract_id, status, updated_at)
            VALUES (?, ?, ?)
            """,
        (contract_id, "open", datetime.datetime.utcnow()),
    )

db_connection.commit()

cursor.close()
db_connection.close()
