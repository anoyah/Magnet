import json
from typing import Optional
import logging

logger = logging.getLogger(__name__)


class Item:
    title: Optional[str] = None
    magnet: Optional[str] = None
    time: Optional[str] = None
    size: Optional[str] = None
    count: Optional[str] = None
    hot: Optional[str] = None

    def __init__(self, **kwargs) -> None:
        self.__dict__.update(kwargs)
        # self.format_print()

    def format_print(self):
        raise NotImplementedError


# 磁链Item
class MagnetItem(Item):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def format_print(self):
        info = {
            "title": self.title,
            "magnet": self.magnet,
            "time": self.time,
            "size": self.size,
            "count": self.count,
            "hot": self.hot,
        }
        logger.info(
            f"{json.dumps(info,sort_keys=True,indent=4,ensure_ascii=False)}")

    def json(self):
        return {
            "title": self.title,
            "magnet": self.magnet,
            "time": self.time,
            "size": self.size,
            "count": self.count,
            "hot": self.hot,
        }


if __name__ == "__main__":
    item = Item()
    item.format_print()
