from diaries.DiarySample import DiarySample
from diaries.MiyakeDiary import DiaryMiyake
from diaries.InadaDiary import DiaryInada
from diaries.HaraDiary import DiaryHara
from diaries.OzakiDiary import OzakiDiary
from diaries.kanaiDiary import kanaiDiary
# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(),
            DiaryMiyake(),
            DiaryHara(),
           DiaryInada(),
            OzakiDiary(),
          DiarySample(),]
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()