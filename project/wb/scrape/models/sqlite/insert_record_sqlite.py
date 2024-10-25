from .records import RecordsDb


def insert_records(records:list, _)->None:
    db = RecordsDb()
    db.save(records)
    db.get_all()
    db.close()
