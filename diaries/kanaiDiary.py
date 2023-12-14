from diaries.AbstractDiary import AbstractDiary

class kanaiDiary(AbstractDiary):
    
    def get_date(self):
        return "2023-12-14"

    def get_summary(self):
        return "プログラミングは難しい"
    
    def get_author(self):
        return "Sample"