from fastapi import FastAPI, HTTPException, Depends
import models
import schemas
from database import get_db
from sqlalchemy.orm import Session
import uuid4
app = FastAPI()

@app.post('/user/{user_name}/activity')
async def create_item(request : dict, user_name : str, db:Session = Depends(get_db)):

    if request.get('event_type', '') not in ['page_view', 'click', 'form_submit']:
        return HTTPException(status_code=502, detail="Event type is invalid..!!!")
    
    if user_name in ['', None]:
        return HTTPException(status_code=502, detail="Username must be required..!!!")
    
    post_obj = {
        'id': uuid4.uuid(),
        'user_name': user_name,
        'event': request
    }
    
    new_post = models.Post(**post_obj.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return { "message": "activity recorded" }
