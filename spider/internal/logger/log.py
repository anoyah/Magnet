import logging
from logging.handlers import RotatingFileHandler
from colorlog import ColoredFormatter


def color_log():
    #第一步：创建一个日志收集器logger
    logger = logging.getLogger("autotest")

    #第二步：修改日志的输出级别
    logger.setLevel(logging.DEBUG)

    #第三步：设置输出的日志内容格式
    fmt = "%(log_color)s%(asctime)s  %(log_color)s%(filename)s  %(log_color)s%(funcName)s [line:%(log_color)s%(lineno)d] %(log_color)s%(levelname)s %(log_color)s%(message)s"
    datefmt = '%a, %d %b %Y %H:%M:%S'

    formatter = ColoredFormatter(fmt=fmt,
                                 datefmt=datefmt,
                                 reset=True,
                                 log_colors={
                                     'DEBUG': 'cyan',
                                     'INFO': 'green',
                                     'WARNING': 'yellow',
                                     'ERROR': 'red',
                                     'CRITICAL': 'red,bg_white'
                                 },
                                 secondary_log_colors={},
                                 style='%')

    #设置输出渠道--输出到控制台
    hd_1 = logging.StreamHandler()
    #在handler上指定日志内容格式
    hd_1.setFormatter(formatter)

    #第五步：将headler添加到日志logger上
    logger.addHandler(hd_1)
    return logger