from sqlmodel import Session, select
from typing import List, Optional
from .model import News
from app.routes.category.model import Category
from .schemas import NewsCreate, NewsUpdate

class NewsRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, news_data: NewsCreate) -> News:
        news = News(
            title=news_data.title,
            subtitle=news_data.subtitle,
            category_id=news_data.category.id
        )
        self.db.add(news)
        self.db.commit()
        self.db.refresh(news)
        return news

    def get_all(self) -> List[News]:
        statement = select(News, Category).join(Category)
        results = self.db.exec(statement).all()
        news_list = []
        for news, category in results:
            news.category = category
            news_list.append(news)
        return news_list

    def get_by_id(self, news_id: int) -> Optional[News]:
        statement = select(News, Category).join(Category).where(News.id == news_id)
        result = self.db.exec(statement).first()
        if result:
            news, category = result
            news.category = category
            return news
        return None

    def update(self, news_id: int, news_data: NewsUpdate) -> Optional[News]:
        news = self.db.exec(select(News).where(News.id == news_id)).first()
        if news:
            news.title = news_data.title
            news.subtitle = news_data.subtitle
            news.category_id = news_data.category.id
            
            self.db.add(news)
            self.db.commit()
            self.db.refresh(news)
        return news

    def delete(self, news_id: int) -> bool:
        news = self.db.exec(select(News).where(News.id == news_id)).first()
        if news:
            self.db.delete(news)
            self.db.commit()
            return True
        return False