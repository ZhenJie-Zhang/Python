# 使用write()將字串寫入檔案
# 覆蓋寫入
with open('lang.txt', 'w') as f:
    f.write('Python\n')
    f.write('C\n')
    f.write('Java\n')

# 增加寫入
with open('lang.txt', 'a') as f:
    f.write('C++\n')
    f.write('Pan語言\n')

# Python
# error: Py_Initialize: can
# 't initialize sys standard streams
#
# LookupError: unknown
# encoding: x - windows - 950
#
# Process
# finished
# with exit code 3
#
# 解決方法: 此為編碼問題
#
# 由Pycharm
# Setting->Edior->FileEncoding
# 將編碼設定由x - windows - 950
# 改成utf - 8