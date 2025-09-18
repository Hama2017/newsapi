from sqlmodel import Session
from .repository import NewsRepository
from app.routes.category.repository import CategoryRepository
from .schemas import NewsCreate, NewsUpdate, NewsRead
from .exceptions import NewsNotFoundException, NewsServerErrorException
from typing import List

class NewsService:
    def __init__(self, db: Session):
        self.news_repository = NewsRepository(db)
        self.category_repository = CategoryRepository(db)

    def create_news(self, news_data: NewsCreate) -> NewsRead:
        try:
            if not self.category_repository.exists_by_id(news_data.category_id):
                raise NewsNotFoundException()
            
            news = self.news_repository.create(news_data)
            news_with_category = self.news_repository.get_by_id(news.id)
            return NewsRead.model_validate(news_with_category) 
        except NewsNotFoundException:
            raise
        except Exception:
            raise NewsServerErrorException()

    def get_all_news(self) -> List[NewsRead]:
        try:
            news_list = self.news_repository.get_all()
            return [NewsRead.model_validate(news) for news in news_list] 
        except Exception:
            raise NewsServerErrorException()

    def get_news_by_id(self, news_id: int) -> NewsRead:
        try:
            news = self.news_repository.get_by_id(news_id)
            if not news:
                raise NewsNotFoundException()
            
            return NewsRead.model_validate(news) 
        except NewsNotFoundException:
            raise
        except Exception:
            raise NewsServerErrorException()

    def update_news(self, news_id: int, news_data: NewsUpdate) -> NewsRead:
        try:
            if news_data.category_id and not self.category_repository.exists_by_id(news_data.category_id):
                raise NewsNotFoundException()
            
            updated_news = self.news_repository.update(news_id, news_data)
            if not updated_news:
                raise NewsNotFoundException()
            
            news_with_category = self.news_repository.get_by_id(updated_news.id)
            return NewsRead.model_validate(news_with_category)  
        except NewsNotFoundException:
            raise
        except Exception:
            raise NewsServerErrorException()

    def delete_news(self, news_id: int) -> dict:
        try:
            deleted = self.news_repository.delete(news_id)
            if not deleted:
                raise NewsNotFoundException()
            
            return {"message": "News deleted successfully"}
        except NewsNotFoundException:
            raise
        except Exception:
            raise NewsServerErrorException()