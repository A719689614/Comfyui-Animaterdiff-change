from .animatediff.logger import logger
from .animatediff.nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
from .animatediff.model_utils import get_available_models
# if len(get_available_models()) == 0:
#     logger.error("No models available. Please download one and put it in models folder")

WEB_DIRECTORY = "./web"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]

print("Cc啊程、AnimateDiff模块移植版")
