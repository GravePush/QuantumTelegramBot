from services.base import BaseService
from api.models import PostModel


class PostService(BaseService):
    model = PostModel
