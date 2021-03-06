﻿# -*- coding: utf-8 -*-
from http.server import HTTPServer, SimpleHTTPRequestHandler
from .webpy import DispatcherHandler, RestController, ResponseEntity, File
from .mapper import *


@RestController
class MainController:

    urls = {
        '/tableList': 'table_list',
        '/tableColumn': 'table_column',
        '/cogen': 'generate_code'
    }

    def table_list(self, table_name=None):
        results = select_table_list(table_name)
        return ResponseEntity.ok([result() for result in results])

    def table_column(self, table_name):
        results = select_table_column(table_name)
        return ResponseEntity.ok([result() for result in results])

    def generate_code(self):
        return File('E:\\temp\\B.zip')


def main():
    port = 8002
    DispatcherHandler.init(globals())
    httpd = HTTPServer(('', port), DispatcherHandler)
    print("Starting HTTP server on port: " + str(httpd.server_port))
    httpd.serve_forever()


if __name__ == '__main__':
    main()
