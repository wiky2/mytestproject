# -*- coding: cp936 -*-
import xlrd '打开excel
data = xlrd.open_workbook('demo.xls') '#注意这里的workbook首字母是小写 查看文件中包含sheet的名称
data.sheet_names() '得到第一个工作表，或者通过索引顺序 或 工作表名称
table = data.sheets()[0]
table = data.sheet_by_index(0)
'table = data.sheet_by_name(u'Sheet1') ''获取行数和列数
'nrows = table.nrows
ncols = table.ncols '获取整行和整列的值（数组）
table.row_values(i)
table.col_values(i) '循环行,得到索引的列表
for rownum in range(table.nrows):
    print table.row_values(rownum) '单元格
cell_A1 = table.cell(0,0).value
cell_C4 = table.cell(2,3).value '分别使用行列索引
'cell_A1 = table.row(0)[0].value
'cell_A2 = table.col(1)[0].value ''简单的写入
row = 0
col = 0
ctype = 1 '# 类型 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
value = 'lixiaoluo'
xf = 0 '# 扩展的格式化 (默认是0)
table.put_cell(row, col, ctype, value, xf)
table.cell(0,0) '# 文本:u''lixiaoluo'
table.cell(0,0).value '# ''lixiaoluo'
