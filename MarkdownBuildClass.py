# -*- coding:utf-8 -*-
class MarkDownBuild:

    table_header = '|字段名称|字段类型|字段含义|\n|:---:|:---:|:---:|\n'
    table_content_template = '|%s|%s|%s|\n'

    def __init__(self):
        pass

    def buildMarkdown(self, table_data):
        text = ''
        for table in table_data:
            text = text + '### ' + table[0][0] + '表(' + table[0][1] + ')\n\n'
            text += self.table_header
            for column in table[1]:
                text = text + '|' + column[0] + '|' + column[1] + '|' + column[2] + '|\n'
            text += '\n'
        return text