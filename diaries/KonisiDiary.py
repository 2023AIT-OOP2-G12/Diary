from diaries.AbstractDiary import AbstractDiary

class KonisiDiary(AbstractDiary):
    
    def get_date(self):
        return "2023-12-14"

    def get_summary(self):
        return "なにもない一日だった"
    
    def get_author(self):
        return "Sample"