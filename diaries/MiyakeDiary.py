from diaries.AbstractDiary import AbstractDiary

class DiaryMiyake(AbstractDiary):
    
    def get_date(self):
        return "2021-12-14"

    def get_summary(self):
        return "本当になにもない一日だった"
    
    def get_author(self):
        return "Miyake"