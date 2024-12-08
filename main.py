import secrets
import string
import pyperclip
from typing import Union

def yes_or_no(query:str):
    while True:
        match input(query).lower():
            case "y" | "ye" | "yes":
                return True
            case "n" | "no":
                return False

class Options:
    Uppercase:bool
    Lowercase:bool
    digits:bool
    symbol:bool
    length:int

class strings:
    UPPERCASE=string.ascii_uppercase 
    LOWERCASE=string.ascii_lowercase 
    DIGITS=string.digits 
    SYMBOL=string.punctuation 

class Generator:
    def generate():
        output:str=""
        for _ in range(Options.length):
            z = secrets.choice(Generator.choiceall(Options.Uppercase,Options.Lowercase,Options.digits,Options.symbol))
            output = output + z
        return output
    
    def question():
        x=0
        while True:
            try:
                Options.Uppercase=yes_or_no("大文字含む?(y/n)")
                Options.Lowercase=yes_or_no("小文字含む?(y/n)")
                Options.digits=yes_or_no("数字含む?(y/n)")
                Options.symbol=yes_or_no("記号含む?(y/n)")
                x=int(input("長さどれくらい?(1以上の整数)"))
                if x>=1:
                    Options.length=x
                else:
                    raise ValueError()

                if Options.Uppercase | Options.Lowercase | Options.digits | Options.symbol:
                    break 
                else:
                    print("このジェネレータに対して少なすぎる引数が入力されています。")
            except ValueError:
                print("それは1以上の整数ではありません。")

    def choiceall(Uppercase:bool,lowercase:bool,digits:bool,symbol:bool)-> str:
        x:str = ""
        if Uppercase:x+=str(strings.UPPERCASE)
        if lowercase:x+=str(strings.LOWERCASE)
        if digits:x+=str(strings.DIGITS)
        if symbol:x+=str(strings.SYMBOL)
        return x 
    
    def OptionUpdate(type:Options, content:Union[bool,int]):
        match type:
            case Options.Uppercase:
                Options.Uppercase=content
                return
            case Options.Lowercase:
                Options.Lowercase=content
                return
            case Options.digits:
                Options.digits=content
                return
            case Options.symbol:
                Options.symbol=content
                return
            case Options.length:
                Options.length=content
                return

if __name__=="__main__":
    Generator.question()
    Generator.OptionUpdate(Options.digits)
    output_=Generator.generate()
    print(output_)
    pyperclip.copy(output_)
    print("Copied!")