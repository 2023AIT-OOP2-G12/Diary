from diaries.AbstractDiary import AbstractDiary

class DiaryInada(AbstractDiary):
    
    def get_date(self):
        return "2021-12-14"

    def get_summary(self):
        return "覚えることが多くて大変な１日だった。"
    
    def get_author(self):
        return "Inada"