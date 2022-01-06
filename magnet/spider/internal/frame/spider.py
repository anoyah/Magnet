import httpx

from magnet.spider.internal.frame.request import Response
import logging
"""
    磁链爬虫基类
"""

logger = logging.getLogger(__name__)


class MagnetSpider:
    def __init__(self, url: str = None, **kwargs) -> None:
        self.http = httpx
        if url is not None:
            self.url = url
        elif not getattr(self, "url", None):
            raise ValueError(f"{type(self).__name__} must have a url.")
        self.headers = None
        self.__dict__.update(kwargs)
        self.logger = logger

    # 获取响应
    def get_resp(self,
                 url: str = None,
                 req_type: str = "get",
                 data: dict = None) -> Response:
        if not url:
            if isinstance(url, str):
                self.url = url
            else:
                raise TypeError
        if isinstance(req_type, str):
            req_type = req_type.lower()
        else:
            raise TypeError
        if req_type == "get":
            resp = self.http.get(self.url,
                                 headers=self.headers,
                                 params=data,
                                 verify=False)
        elif req_type == "post":
            resp = self.http.post(url=self.url,
                                  headers=self.headers,
                                  data=data)
        return Response(resp)

    # 子类必须实现
    def spider(self):
        raise NotImplementedError

    def main(self):
        return self.spider()

    def search(self, words):
        return self.spider(words)
