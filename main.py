from diaries.DiarySample import DiarySample
from diaries.MiyakeDiary import DiaryMiyake
from diaries.InadaDiary import DiaryInada
from diaries.HaraDiary import DiaryHara

diaries = [DiarySample(),
           DiaryMiyake(),
           DiaryInada(),
           DiaryHara(),]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()