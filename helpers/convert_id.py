def convert_id(doc: dict) -> dict:
    """Converts MongoDB _id to a string."""
    if "_id" in doc:
        doc["_id"] = str(doc["_id"])
    return doc
