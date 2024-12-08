import secrets
import string
import pyperclip

def yes_or_no(query:str): # query(str)でinputし、小文字化したものがy,ye,yesならreturn True、n,noならreturn True
    while True:
        match input(query).lower():
            case "y" | "ye" | "yes":
                return True
            case "n" | "no":
                return False

class Options: # オプションの型のみ決定。値を指定はできるが存在しないことになっている。
    Uppercase: bool
    Lowercase: bool
    digits: bool
    symbol: bool
    length: int

class strings: # 定数を決定。
    UPPERCASE=string.ascii_uppercase # 大文字アルファベット
    LOWERCASE=string.ascii_lowercase # 小文字アルファベット
    DIGITS=string.digits # 数字
    SYMBOL=string.punctuation # 記号

class Generator:
    def generate():
        output: str=""
        for _ in range(Options.length): # Option.length回繰り返す
            output:str =+ secrets.choice(Generator.choiceall(Options.Uppercase,Options.Lowercase,Options.digits,Options.symbol))
            # オプションを元に1文字ごとに乱数で取り出して追加。strはイテラブル。
        return output
    
    def question():
        x=0
        while True:
            try:
                Options.Uppercase=yes_or_no("大文字含む?(y/n)")
                Options.Lowercase=yes_or_no("小文字含む?(y/n)")
                Options.digits=yes_or_no("数字含む?(y/n)")
                Options.symbol=yes_or_no("記号含む?(y/n)") # オプションを追加
                x=int(input("長さどれくらい?(1以上の整数)"))
                if x>=1:
                    Options.length=x
                else:
                    raise ValueError() # ValueError例外を発生。except文に行く。

                if Options.Uppercase | Options.Lowercase | Options.digits | Options.symbol: # いずれかのオプションがTrueならば
                    break # 通常に処理を終了
                else: # while True文なのでもう一回
                    print("このジェネレータに対して少なすぎる引数が入力されています。")
            except ValueError: # もう一回
                print("それは1以上の整数ではありません。")

    def choiceall(Uppercase:bool,lowercase:bool,digits:bool,symbol:bool):
        x: str = ""
        if Uppercase: x+=str(strings.UPPERCASE)
        if lowercase: x+=str(strings.LOWERCASE)
        if digits: x+=str(strings.DIGITS)
        if symbol: x+=str(strings.SYMBOL)
        return x # 大文字・小文字・数字・記号をTrueのものだけ取り出しそれを返す

if __name__=="__main__": # importされていないなら
    Generator.question() # 聞く
    output_=Generator.generate() # output_にgenerateした文字列を代入
    print(output_) # 文字列をprint。セキュリティ的には要らない
    pyperclip.copy(output_) # クリップボードにコピー
    print("Copied!") # コピーされたことを通知