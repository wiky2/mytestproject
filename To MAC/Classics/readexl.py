# -*- coding: cp936 -*-
import xlrd '��excel
data = xlrd.open_workbook('demo.xls') '#ע�������workbook����ĸ��Сд �鿴�ļ��а���sheet������
data.sheet_names() '�õ���һ������������ͨ������˳�� �� ����������
table = data.sheets()[0]
table = data.sheet_by_index(0)
'table = data.sheet_by_name(u'Sheet1') ''��ȡ����������
'nrows = table.nrows
ncols = table.ncols '��ȡ���к����е�ֵ�����飩
table.row_values(i)
table.col_values(i) 'ѭ����,�õ��������б�
for rownum in range(table.nrows):
    print table.row_values(rownum) '��Ԫ��
cell_A1 = table.cell(0,0).value
cell_C4 = table.cell(2,3).value '�ֱ�ʹ����������
'cell_A1 = table.row(0)[0].value
'cell_A2 = table.col(1)[0].value ''�򵥵�д��
row = 0
col = 0
ctype = 1 '# ���� 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
value = 'lixiaoluo'
xf = 0 '# ��չ�ĸ�ʽ�� (Ĭ����0)
table.put_cell(row, col, ctype, value, xf)
table.cell(0,0) '# �ı�:u''lixiaoluo'
table.cell(0,0).value '# ''lixiaoluo'
