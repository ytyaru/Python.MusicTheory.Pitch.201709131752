import PitchClass
class Degree:
    @classmethod
    def Get(cls, name:str):
        degree = int(name)
        for d in cls.GetList():
            if d[0] == degree: return (degree, 0)
        raise Exception('1,2,3,4,5,6,7の文字のみ対応しています。将来、8〜14や変化記号にも対応予定です。')
    
    #定数のようにしたい: readonlyにしたい。クラス・プロパティにして()不要にし、名前を"Degrees"にしたい。
    @classmethod
    def GetList(cls): return ((1,0),(2,2),(3,4),(4,5),(5,7),(6,9),(7,11))


if __name__ == '__main__':
    print(Degree.GetList())
    for degree in range(1, 8):
        print(degree, Degree.Get(str(degree)))
    print(degree, Degree.Get('#5'))#ValueError: invalid literal for int() with base 10: '#5'
