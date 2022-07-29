from io import StringIO  
class Report(object):
    report_template = None
    def __init__(self):
        self.report_template =""
        pass
    def WriteReportHeader(self):
        self.report_template += ("""
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Test Report</title>
</head>
<style>
    body{
        background-color: #ffffff;
    }
    .title{
        font-size: 1.6em;
        font-weight: bold;
        color: #003939;
    }
    * {
        font-family: sans-serif;
        }
    .content-table{
        border-collapse: collapse;
        margin: 25px 0;
        font-size: 1em;
        min-width: 400px;
        border-radius: 5px 5px 0 0;
        overflow: hidden;
        box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
    }
    .content-table thead tr{
        background-color: #009879;
        color: #ffffff;
        text-align: left;
        font-weight: bold;
        
    }
    .content-table th ,
    .content-table td{
        padding: 12px 15px;
    }
    .content-table tbody tr {
        border-bottom: 1px solid #dddddd ;
    }
    .content-table tbody tr:nth-of-type(even) {
        background-color: #f3f3f3;
    }
    .content-table tbody tr:last-child{
        border-bottom: 2px solid #009879;
    }
    .content-table tbody tr.passed-test{
    font-weight: bold;
    color: #04c9a1;
    }
    .content-table tbody tr.failed-test{
    font-weight: bold;
    color: #fd4d4d;
    }
</style>
<body>
    <p class="title">ShipperApp Test Results</p>
    <table class="content-table">
        <thead>
            <tr>
                <th>Test ID</th>
                <th>Test Case</th>
                <th>Execution time</th>
                <th>Result</th>
            </tr>
        </thead>
        <tbody>""")
    def appendToReport(self,Test_ID, Test_case,Execution_time , Result):
        if(Result.lower()=="passed"):
            self.report_template += '<tr class="passed-test">'
        else:
            self.report_template += '<tr class="failed-test">'
        self.report_template+= '<td>' +Test_ID+'</td>'  
        self.report_template+= '<td>' +Test_case+'</td>'  
        self.report_template+= '<td>' +Execution_time+'</td>'  
        self.report_template+= '<td>' +Result+'</td>'
        self.report_template+= '</tr></tbody>'
    def writeReportFooter(self):
        self.report_template+='</table></body></html>'
    def writeToFile(self,fileName):
        final_template = self.report_template
        report_file = open(fileName,'w')
        report_file.write(final_template)
        report_file.close()










