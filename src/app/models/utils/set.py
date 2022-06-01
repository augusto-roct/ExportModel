async def Set(collection, document, data, db):
    try:
        db.collection(collection).document(document).set(data.dict())
        return {"message": "Insert datas on " + collection + " -> " + document + " works!"}
    except Exception as e:
        print(e)
        return {"message": "Error on insert datas"}