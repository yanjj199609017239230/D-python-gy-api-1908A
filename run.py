# -*- coding:utf-8 -*-																		
# Author : 小吴老师                                                                        
# Data ：2019/7/12 7:41                                                                    
from tools import log_tool                                                                 
from tools import shell_tool                                                               
from tools import log_tool                                                                 
import pytest                                                                              
                                                                                           
if __name__ == '__main__':                                                                 
    # 修改成要执行的测试用例                                                               
    test_case = 'test_case/test_liu_cheng.py'

    xml_report_path = './reports/xml/'                                                     
    html_report_path = './reports/html/'                                                   
                                                                                           
    pytest.main(['-s', '-q', '--alluredir',                                                
                 xml_report_path, test_case])                                              
    cmd1 = 'allure generate %s -o %s --clean' % (xml_report_path, html_report_path)        
    cmd2 = 'allure serve %s' % (xml_report_path)                                           
                                                                                           
    shell_tool.invoke(cmd1)                                                                
    shell_tool.invoke(cmd2)                                                              
