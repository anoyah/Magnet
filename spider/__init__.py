# from typing import Type
# from lxml import etree
# import typing
# import httpx
# """
#     磁链爬虫基类
# """


# class MagnetSpider:
#     def __init__(self, url: str = None) -> None:
#         self.http = httpx
#         self.url = url
#         self.header = {}

#     # 获取响应
#     def get_response(self,
#                      url: str = None,
#                      req_type: str = "get",
#                      data: dict = None) -> httpx.Response:
#         if not url:
#             if isinstance(url, str):
#                 self.url = url
#             else:
#                 raise TypeError
#         if isinstance(req_type, str):
#             req_type = req_type.lower()
#         else:
#             raise TypeError
#         if req_type == "get":
#             return self.http.get(self.url, headers=self.header)
#         elif req_type == "post":
#             return self.http.post(self.url, data=data)

#     def resp_text(self, resp: httpx.Response) -> str:
#         if isinstance(resp, httpx.Response):
#             return resp.text
#         else:
#             raise TypeError

#     def resp_json(self, resp: httpx.Response) -> typing.Any:
#         if isinstance(resp, httpx.Response):
#             return resp.json()
#         else:
#             raise TypeError

#     # xpath解析节点
#     def xpath_dom(self, dom: str, xpath: str) -> typing.Any:
#         if isinstance(dom, str) and isinstance(xpath, str):
#             text_dom = etree.HTML(dom)
#             return text_dom.xpath(xpath)
#         else:
#             raise TypeError

#     # 子类必须实现
#     def spider(self):
#         raise NotImplementedError

#     def main(self):
#         self.spider()
