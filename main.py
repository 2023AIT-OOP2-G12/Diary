from diaries.DiarySample import DiarySample
from diaries.MiyakeDiary import DiaryMiyake
from diaries.HaraDiary import DiaryHara
from diaries.KonisiDiary import KonisiDiary
# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(),
            DiaryMiyake(),
            DiaryHara(),
            KonisiDiary(),]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()