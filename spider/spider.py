from base.spider import MagnetSpider


class Duo33(MagnetSpider):
    def __init__(self, url=None) -> None:
        super().__init__(url)
        self.headers = {
            'authority': 'duo1.dns33.top:39988',
            'sec-ch-ua':
            '" Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'upgrade-insecure-requests': '1',
            'user-agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.57',
            'accept':
            'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'iframe',
            'referer': 'https://duo1.dns33.top:39988/',
            'accept-language':
            'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        }

    def spider(self):
        params = (('word', '91'), )
        resp = self.get_resp(self.url, req_type="get", data=params)
        tbox = resp.xpath("//div[@class='tbox']//div[@class='ssbox']")
        for t in tbox:
            title = "".join(t.xpath(".//h3/a/em/text() | .//h3/a/text()"))
            magnet = "".join(t.xpath(".//div[@class='sbar']/span[1]/a/@href"))
            time = "".join(t.xpath(".//div[@class='sbar']/span[2]/b/text()"))
            file_size = "".join(
                t.xpath(".//div[@class='sbar']/span[3]/b/text()"))
            file_count = "".join(
                t.xpath(".//div[@class='sbar']/span[4]/b/text()"))
            file_hot = "".join(
                t.xpath(".//div[@class='sbar']/span[5]/b/text()"))
            print(
                f"{title}\n{magnet}\n{time}\n{file_size}\n{file_count}\n{file_hot}"
            )


if __name__ == "__main__":
    duo = Duo33("https://duo1.dns33.top:39988/search")
    duo.main()