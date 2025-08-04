from report import Report
from reportbuilder import ReportBuilder

def main():
    """Complex object construction object with many optional components
    
    """
    report = (
        ReportBuilder().title("Monthly report")
        .toc()
        .data()
        .chart()
        .appendx()
        .build()
        
    )
    
    print(report)


if __name__ == "__main__":
    main()