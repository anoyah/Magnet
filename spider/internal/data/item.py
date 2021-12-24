import json
from typing import Optional
from internal.logger.log import color_log

logger = color_log()


class Item:
    title: Optional[str] = None
    magnet: Optional[str] = None
    time: Optional[str] = None

    def __init__(self, **kwargs) -> None:
        self.__dict__.update(kwargs)
        self.format_print()

    def format_print(self):
        raise NotImplementedError


class MagnetItem(Item):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def format_print(self):
        info = {
            "title": self.title,
            "magnet": self.magnet,
            "time": self.time,
        }
        logger.info(f"{json.dumps(info,sort_keys=True,indent=4,ensure_ascii=False)}")


if __name__ == "__main__":
    item = Item()
    item.format_print()
