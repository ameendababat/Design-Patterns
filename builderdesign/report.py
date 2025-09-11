

class Report:
    def __init__(self, title = None, has_toc = False, has_data = False, has_chart = False, has_appendx = False):
        self.title = title
        self.has_toc = has_toc
        self.has_data = has_data
        self.has_chart = has_chart
        self.has_appendx = has_appendx


    def __str__(self):
        return f"the Report title: {self.title} has_toc: {self.has_toc} has_data: {self.has_data} has_chart: {self.has_chart} has_appendx: {self.has_appendx}"