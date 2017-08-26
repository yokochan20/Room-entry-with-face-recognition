# -*- coding: utf-8 -*-

import requests
import json

def post_slack(name):
    requests.post('https://hooks.slack.com/services/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', data = json.dumps({
        'text':name + u' has entered to s103 room', # 投稿するテキスト
        'username': u'yokochan_bot', # 投稿のユーザー名
        'icon_emoji': u':ghost:', # 投稿のプロフィール画像に入れる絵文字
        'link_names': 1, # メンションを有効にする
    }))

post_slack("yokochan")
