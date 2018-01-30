# -*- coding: utf-8 -*-
import MySQLdb
import datetime
from zhihu_spider.myconfig import DbConfig


class ZhihuSpiderPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user=DbConfig['user'], passwd=DbConfig['passwd'], db=DbConfig['db'],
                                    host=DbConfig['host'], charset='utf8', use_unicode=True)
        self.cursor = self.conn.cursor()
        # 清空表
        # self.cursor.execute('truncate table weather;')
        # self.conn.commit()

    def process_item(self, item, spider):
        curTime = datetime.datetime.now()
        try:
            self.cursor.execute(
                """INSERT IGNORE INTO users (url, name, bio, location, business, gender, avatar, education, major, employment, position, content, ask, answer, agree, thanks, create_at)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                (
                    item['url'],
                    item['name'],
                    item['bio'],
                    item['location'],
                    item['business'],
                    item['gender'],
                    item['avatar'],
                    item['education'],
                    item['major'],
                    item['employment'],
                    item['position'],
                    item['content'],
                    item['ask'],
                    item['answer'],
                    item['agree'],
                    item['thanks'],
                    curTime
                )
            )
            self.conn.commit()
        except MySQLdb.Error as e:
            print('Error %d %s' % (e.args[0], e.args[1]))

        return item
