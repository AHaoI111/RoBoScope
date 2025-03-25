# -*- encoding: utf-8 -*-
"""
@Description:
读取和保存配置文件
@File    :   read_config.py
@Time    :   2024/07/16
@Author  :   Li QingHao
@Version :   2.0
@Time_END :  最后修改时间：
@Developers_END :  最后修改作者：
"""
import logging
import shutil

import yaml


class ConfigReader:
    def __init__(self, config_file='config.yaml', error_log_file='config_error.log'):
        self.config_file = config_file
        self.error_log_file = error_log_file
        self.data = {}



        try:
            with open(self.config_file, 'r', encoding='utf-8') as file:
                self.data = yaml.safe_load(file)
        except FileNotFoundError:
            # 配置日志记录器
            self._configure_logger()
            self.logger.warning('配置文件读取出错')
        except Exception as e:
            self.logger.warning('配置文件读取出错: %s', e)

    def _configure_logger(self):
        # 创建并配置日志记录器
        self.logger = logging.getLogger('file_logger')
        self.logger.setLevel(logging.DEBUG)

        # 创建文件处理程序
        file_handler = logging.FileHandler(self.error_log_file)
        file_handler.setLevel(logging.DEBUG)
        # 创建日志记录格式并添加到文件处理程序
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        # 将文件处理程序添加到日志记录器
        self.logger.addHandler(file_handler)

        # 删除默认的控制台处理程序
        self.logger.propagate = False

    def get_config_info(self) -> dict:
        return self.data

    def save_config_info(self, data: dict) -> None:
        try:
            # 备份原始配置文件
            shutil.copy2(self.config_file, f"{self.config_file}.bak")

            with open(self.config_file, 'w', encoding='utf-8') as file:
                yaml.dump(data, file, allow_unicode=True)
        except FileNotFoundError:
            self.logger.warning('配置文件写入出错：文件找不到')
        except PermissionError:
            self.logger.warning('配置文件写入出错：没有权限')
        except IsADirectoryError:
            self.logger.warning('配置文件写入出错：目标是目录')
        except Exception as e:
            self.logger.warning('配置文件写入出错: %s', e)


