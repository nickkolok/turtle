# -*- coding: utf-8 -*-

from datetime import datetime
import os
import sys

class Log:

    log_dir  = "logs/"
    log_path = ""

    def __init__(self, log_file_name = str(datetime.now())):
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

        self.log_path = self.log_dir + log_file_name

        if not os.path.exists(self.log_path):
            f = open(self.log_path, "w")
            f.close()

    def append(self, log_text):
        with open(self.log_path, "a") as f:
            f.write(str(datetime.now()) + " - " + log_text + "\n")
        print(log_text)

    def append_exception(self, exp):
        exc_type, exc_obj, exc_tb = sys.exc_info()
        with open(self.log_path, "a") as f:
            f.write(str(datetime.now()) + " - ## Error : " + str(exp) + " - Type : " + str(exc_type) + " - Line : " + str(exc_tb.tb_lineno) + "\n")
        print("## Error : " + str(exp) + " - Type : " + str(exc_type) + " - Line : " + str(exc_tb.tb_lineno))