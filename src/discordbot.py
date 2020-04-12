# モジュールインポート
import discord
import json
from collections import OrderedDict
import pprint
from discord.ext import commands  # Bot Commands Frameworkをインポート
import traceback  # エラー表示のためにインポート

# 読み込むコグの名前を格納しておく。
INITIAL_EXTENSIONS = [
    'cogs.cog'
]

# アクセストークンの取得
f = open('../config/config.json', 'r')
load_config = json.load(f)
pprint.pprint(f)
BOT_ACCESS_TOKEN = load_config["TOKEN"]


class DiplomacyBot(commands.Bot):

    def __init__(self, command_prefix):
        # スーパークラスのコンストラクタに値を渡して実行。
        super().__init__(command_prefix)

        for cog in INITIAL_EXTENSIONS:
            try:
                self.load_extension(cog)
            except Exception:
                traceback.print_exc()

    async def on_ready(self):
        print('----------------')
        print(self.user.name)
        print(self.user.id)
        print('Login Successful')
        print('----------------')


print(__name__)
if __name__ == '__main__':
    bot = DiplomacyBot(command_prefix='!')
    bot.run(BOT_ACCESS_TOKEN)
