if __name__ == "__main__":
    from bs4 import BeautifulSoup

class banner():
    def __init__(self):
        f = open('../index.html',mode='r',encoding='utf8')
        self.soup = BeautifulSoup(f.read(),features='lxml')
        f.close()
    def to_html(self,change):
        f = open('../index_newbanner.html',mode='w',encoding='utf8')
        f.write(change)
        f.close()
    def change_text(self,slide,line,text):
        # slide: điền trang muốn thay đổi; 1 hoặc 2
        # line: điền dòng muốn thay đổi; 1, 2 hoặc 3
        # text: điền nội dung thay đổi
        self.soup.find(id=[['bannertext1','bannertitle1','bannertyping1'],
                           ['bannertext2','bannertitle2','bannertyping2']][slide-1][line-1]).string.replace_with(text)
        self.to_html(str(self.soup.prettify()))

# ví dụ
b = banner()
b.change_text(slide=1,line=2,text='fresh porto coffee')