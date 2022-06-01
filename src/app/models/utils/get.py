import json

async def Get(collection, document, db):
    try:
        doc = db.collection(collection).document(document).get()
        
        if doc.exists:
            return doc.to_dict()
        else:
            return {"message": "No such document!"}
    except Exception as e:
        print(e)
        return {"message": "Error on get datas"}