from fastapi import APIRouter

from controllers.apis.landing import get_chat_page
from controllers.apis.chat import chat_endpoint

from config import logger

router = APIRouter(prefix="")

logger.debug(f"Registering {chat_endpoint.__name__} route.")
router.add_api_route(
    path="/api/chat",
    endpoint=chat_endpoint,
    methods=["POST"],
)
logger.debug(f"Registered {chat_endpoint.__name__} route.")


logger.debug(f"Registering {get_chat_page.__name__} route.")
router.add_api_route(
    path="/",
    endpoint=get_chat_page,
    methods=["GET"],
)
logger.debug(f"Registered {get_chat_page.__name__} route.")
