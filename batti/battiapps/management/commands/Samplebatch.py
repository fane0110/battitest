import argparse
from django.core.management.base import BaseCommand

import random
from ...models import passcode

class Command(BaseCommand):
    # [python manage.py help sampleBatch]で表示されるメッセージ
    help = 'これはテスト用のコマンドバッチです'

    def add_arguments(self, parser):
        # コマンドライン引数を指定
        parser.add_argument('-n', action='store', dest='strname', help='50文字以下で名前を入力してください',required=True, type=valid_type)
        parser.add_argument('-s', action='store', dest='intValue', help='整数値を入力してください',required=False, type=int)


    def handle(self, *args, **options):
        try:
            #destで指定した名前
            p=passcode(passname_text=options['strname'])
            seed = options['intValue']
            #無い場合は適当に作成
            if seed is None:
                seed=random.randint(-1*10**100 ,10**100)
            p.makepasstext(x=seed)
            retstr=p.pass_text
            p.save()
            return('バッチが動きました： 作成された名前:{0},生成された文字列：{1}'.format(options['strname'],retstr))
        except Exception as e:
            print(e)


def valid_type(t):
    """
    引数のバリデーション
    :param unicode t:
    :rtype: int
    """
    passname = str(t)
    if len(passname)<50:
            return passname
    raise argparse.ArgumentTypeError('given {} is too long!!'.format(passname))