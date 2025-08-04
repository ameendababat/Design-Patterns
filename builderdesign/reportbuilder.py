from builder import Builder
from report import Report 


class ReportBuilder(Builder):
    
    def __init__(self):
        self.__title = None
        self.__has_toc = False
        self.__has_data = False
        self.__has_chart = False
        self.__has_appendx = False
        # self.__has_sumary = False
        
        
    def title(self, title):
        self.__title = title
        return self
    
    
    def toc(self, toc=True):
        self.__has_toc = toc
        return self
    
        
    def data(self, data=True):
        self.__has_data = data
        return self
    
    
    def chart(self, chart=True):
        self.__has_chart = chart
        return self
    
    
    def appendx(self, appendx=True):
        self.__has_appendx = appendx
        return self
    
    
    def build(self) -> Report:
        return Report(
            title=self.__title,
            has_toc=self.__has_toc,
            has_data=self.__has_data,
            has_chart=self.__has_chart,
            has_appendx=self.__has_appendx
        )
        