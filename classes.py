class Cookie:
    def __init__(self, colors):
        self.colors = colors
    def SetColor(self, colors):
        self.colors = colors
    def GetColors(self):
        return self.colors

cookie_one = Cookie('viloet')
cookie_two = Cookie('Blue')

print(f'Cookie one Color :' , cookie_one.GetColors())
print(f'Cookie one Color :' , cookie_two.GetColors())