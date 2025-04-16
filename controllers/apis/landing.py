from fastapi.responses import HTMLResponse
from config import logger


async def get_chat_page():
    """
    Serves the chat landing page (index.html) to the user.
    """

    logger.info("Landing page requested (/)")
    with open("templates/index.html", "r") as f:
        html_content = f.read()
    logger.info("Landing page response sent (/)")

    return HTMLResponse(content=html_content)