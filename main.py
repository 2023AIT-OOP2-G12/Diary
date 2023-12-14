from diaries.DiarySample import DiarySample
from diaries.MiyakeDiary import DiaryMiyake
from diaries.InadaDiary import DiaryInada
# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(),
            DiaryMiyake(),
            DiaryInada(),]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()