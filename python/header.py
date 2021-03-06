if __name__ == "__main__":
    from bs4 import BeautifulSoup

class header():
    def __init__(self):
        f = open('../index.html',encoding='utf8',mode='r')
        self.soup = BeautifulSoup(f.read(),features='lxml')
        f.close()
    def to_html(self,change):
        f = open('../index_newheader.html',encoding='utf8',mode='w')
        f.write(change)
        f.close()
    def change_items(self,items):
        for item in range(8): # navbar có 8 mục không đổi
            self.soup.find_all(attrs={'class':'header-link'})[item].string.replace_with(items[item])
        self.to_html(str(self.soup.prettify()))
    def change_logo(self,url='img/logo.png'):
        self.soup.find(id='logo-img')['src'] = url
        self.to_html(str(self.soup.prettify()))

# ví dụ
new_items = ['new home','about','reservations','menu','news','location','elements','buy porto!']
b = header()
b.change_items(new_items)
b.change_logo('img/logo2.png')
