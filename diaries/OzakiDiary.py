from diaries.AbstractDiary import AbstractDiary

class OzakiDiary(AbstractDiary):
    
    def get_date(self):
        return "2023-12-14"

    def get_summary(self):
        return "プログラミング疲れた"
    
    def get_author(self):
        return "Sample"