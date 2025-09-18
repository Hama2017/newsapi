from fastapi import APIRouter, Depends, HTTPException
from app.db.base import get_session
from app.models import News
router = APIRouter()

@router.get("")
def get_news(session=Depends(get_session)):
    news = News(title='test', subtitle='test', category='sport')
    session.add(news)
    session.commit()
    #raise HTTPException(status_code=404, detail="NOT_FOUND")
    return {"message": "ok"}
