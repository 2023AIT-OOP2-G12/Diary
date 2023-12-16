from diaries.AbstractDiary import AbstractDiary

class MasunagaDiary(AbstractDiary):
    
    def get_date(self):
        return "2023-12-16"

    def get_summary(self):
        return "今日は土曜日です。休日だけど作業します。というか休日くらいしか作業する時間が取れなさそうです。これからグループで何を作るのか楽しみです。コンフリクトが起こらないように、自分がいつ作業をしたのかはなるべく共有します。よろしくお願いします。"
    
    def get_author(self):
        return "MasunagaKazuki"