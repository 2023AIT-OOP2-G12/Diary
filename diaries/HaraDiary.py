from diaries.AbstractDiary import AbstractDiary

class DiaryHara(AbstractDiary):
    
    def get_date(self):
        return "2021-12-14"

    def get_summary(self):
        return "リーダーになった"
    
    def get_author(self):
        return "Miyake"