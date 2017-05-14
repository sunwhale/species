# -*- coding: utf-8 -*-

import codecs
import numpy as np
import os
import matplotlib.pyplot as plt
from DictCountry import *
from DictLatin import *
from DictPort import *
from DictImport import *
from DictGoodsType import *
from DictUnit import *
import xlsxwriter

def getFiles( path ):
    fns=[]
    for root, dirs, files in os.walk( path ):
        for fn in files:
            fns.append( [ root , fn ] )
    return fns

def isTextFile( filename ):
    b = False
    suffixs = ['txt','dat','csv']
    for suffix in suffixs:
        if filename.split('.')[-1] == suffix:
            b = True
    return b

def select_sort(sort_array, other_array):
    for i, elem in enumerate(sort_array):
        for j, elem in enumerate(sort_array[i:]):
            if sort_array[i] < sort_array[j + i]:
                #交换
                sort_array[i], sort_array[j + i] = sort_array[j + i], sort_array[i]
                other_array[i], other_array[j + i] = other_array[j + i], other_array[i]
                
year = '2015'
inpath = 'F:\\Cloud\\species\\'+year+'\\'
outpath = 'F:\\GitHub\\species\\'+year+'output\\'

if not os.path.isdir(outpath.decode('utf8').encode('gbk')):
    os.makedirs(outpath.decode('utf8').encode('gbk'))
    print 'Create new directory:',outpath.decode('utf8').encode('gbk')
    
filenames = getFiles(inpath.decode('utf8').encode('gbk'))

latin_name = []
chinese_name = []
import_number = []
import_money = []
import_country_top3 = []
import_port_top3 = []
export_port_top3 = []
origin_country_top3 = []

for s in Latin[20:]:
    print '----------'
    print '物种拉丁名：' + s
    print '----------'
    export_country_list = []
    mass_unit_list = []
    cmonetary_unit_list = []
    species_list = []
    species_chinese_list = []
    import_port_list = []
    export_port_list = []
    country_origin_list = []
    origin_list = []
    goods_type_list = []
    
    for filename in filenames:
        fullname = filename[0] + '\\' + filename[1]
        fullname = fullname.decode('gbk').encode('gbk')
#        print 'Reading: ' + filename[1].decode('gbk')
        if isTextFile(filename[1]):
            infile = open(fullname,'r')
            list1 = infile.readlines()
            list2 = [i.decode('gbk').encode('utf8').strip() for i in list1[:]]
            list3 = [i.split('\t') for i in list2[2:]]

            result = [ i for i in list3 if s == DataToLatin[i[9]] ]

            for r in result:
                export_country_list.append(DictCountry[r[5]])
                mass_unit_list.append(DictUnit[r[13]])
                cmonetary_unit_list.append(r[39])
                species_list.append(r[9])
#                species_chinese_list.append(r[8])
                export_port_list.append(DictPort[r[46]])
                country_origin_list.append(DictCountry[r[14]])
                origin_list.append(DictOrigin[r[26]])
                import_port_list.append(DictImport[r[54]])
                goods_type_list.append(DictGoodsType[r[10]])

                
    export_country_list = list(set(export_country_list))
    export_country_sum = [0]*len(export_country_list)
    
    mass_unit_list = list(set(mass_unit_list))
    mass_sum = [0]*len(mass_unit_list)
    
    cmonetary_unit_list = list(set(cmonetary_unit_list))
    cmonetary_sum = [0]*len(cmonetary_unit_list)
    
    species_list = list(set(species_list))
#    species_chinese_list = list(set(species_chinese_list))
    
    export_port_list = list(set(export_port_list))
    export_port_sum = [0]*len(export_port_list)
    
    import_port_list = list(set(import_port_list))
    import_port_sum = [0]*len(import_port_list)
    
    country_origin_list = list(set(country_origin_list))
    origin_list = list(set(origin_list))   
    
    goods_type_list = list(set(goods_type_list))
    goods_type_sum = [0]*len(goods_type_list)
    
    import_port_list.sort()
    export_country_list.sort()
    export_port_list.sort()
    country_origin_list.sort()
    origin_list.sort()
    goods_type_list.sort()
    mass_unit_list.sort()
    species_list.sort()
    
#    for species in species_list:
#        print species
#    for export_country in export_country_list:
#        print export_country
#    for export_port in export_port_list:
#        print export_port
#    for import_port in import_port_list:
#        print import_port
    
    for filename in filenames:
        fullname = filename[0] + '\\' + filename[1]
        outname = fullname.replace('\\','_')
        outname = outname.replace(':','')
        outname = outname[:-4] + '.txt'
        if isTextFile(filename[1]):
#            print 'Reading: ' + filename[1].decode('gbk')
            infile = open(fullname,'r')
            list1 = infile.readlines()
            list2 = [i.decode('gbk').encode('utf8').strip() for i in list1[:]]
            list3 = [i.split('\t') for i in list2[2:]]
            
            result = [ i for i in list3 if s == DataToLatin[i[9]] ]
    
            for r in result:
           
                for i in range(len(mass_unit_list)):
                    if DictUnit[r[13]] == mass_unit_list[i]:
                        mass_sum[i]+=float(r[12])
                        
                    if DictUnit[r[13]] == '小盒、容器、胶囊':
                        if len(r) == 81:
                            print r[0],r[12],r[13],r[80]
                            
                    if DictUnit[r[13]] == '箱':
                        if len(r) == 81:
                            print r[0],r[12],r[13],r[80]
                            
                for i in range(len(cmonetary_unit_list)):
                    if r[39] == cmonetary_unit_list[i]:
                        cmonetary_sum[i]+=float(r[38])
                        
                for i in range(len(export_country_list)):
                    if DictCountry[r[5]] == export_country_list[i]:
                        export_country_sum[i]+=float(r[38])
                        
                for i in range(len(export_port_list)):
                    if DictPort[r[46]] == export_port_list[i]:
                        export_port_sum[i]+=float(r[38])
                        
                for i in range(len(import_port_list)):
                    if DictImport[r[54]] == import_port_list[i]:
                        import_port_sum[i]+=float(r[38])
                        
                for i in range(len(goods_type_list)):
                    if DictGoodsType[r[10]] == goods_type_list[i]:
                        goods_type_sum[i]+=float(r[38])
                        
#    print sum(export_port_sum)
#    print sum(cmonetary_sum)
#    print sum(export_country_sum)
#    print sum(import_port_sum)
#==============================================================================
# 排序
#==============================================================================
    select_sort(export_country_sum, export_country_list)
    select_sort(export_port_sum, export_port_list)
    select_sort(goods_type_sum, goods_type_list)
    select_sort(import_port_sum, import_port_list)    
#==============================================================================
# 输出
#==============================================================================
    if sum(export_port_sum)>0:
#        print '----------'  
##        print export_country_list
##        print mass_unit_list
##        print cmonetary_unit_list
#        
#        print u'总数量: '
#        for i in range(len(mass_unit_list)):
#            print str(mass_sum[i])+':'+str(mass_unit_list[i])
#            
#        print u'总金额: '
#        for i in range(len(cmonetary_unit_list)):
#            print str(cmonetary_sum[i])+':'+str(cmonetary_unit_list[i])
#            
#        print u'进口份额: '
#        for i in range(len(export_country_list)):
#            print str(export_country_list[i])+':'+str(export_country_sum[i])
#            
#        print u'出口口岸: '
#        for i in range(len(export_port_list)):
#            print str(export_port_list[i])+':'+str(export_port_sum[i])
#            
#        print u'进口口岸: '
#        for i in range(len(import_port_list)):
#            print str(import_port_list[i])+':'+str(import_port_sum[i])
#            
#        print u'货物类型: '
#        for i in range(len(goods_type_list)):
#            print str(goods_type_list[i])+':'+str(goods_type_sum[i])
#            
#        print u'原产国： '
#        print country_origin_list
#        
#        print u'来源： '
#        print origin_list
#    
#        print '----------'
#==============================================================================
# 单位转换          
#==============================================================================
#        for i in range(len(mass_unit_list)):
#            if mass_unit_list[i] == '立方米':
#                print mass_sum[i], mass_unit_list[i]
                
        for i in range(len(mass_unit_list)):
            if mass_unit_list[i] == '千克':
#                print mass_sum[i], mass_unit_list[i]
#                print '密度：%s千克/立方米' % (str(density[s]*1000.0))
#                print '%s千克 = %s立方米' % (mass_sum[i],mass_sum[i]/density[s]/1000.0)
                
                if '立方米' not in mass_unit_list:
                    mass_unit_list.append('立方米')
                    mass_sum.append(mass_sum[i]/density[s]/1000.0)
                else:
                    for j in range(len(mass_unit_list)):
                        if mass_unit_list[j] == '立方米':
                            mass_sum[j] = mass_sum[j] + mass_sum[i]/density[s]/1000.0
#==============================================================================
# 输出 csv
#==============================================================================
        outname = outpath + s + '_' + LatinToChinese[s] + '_' + year + '.csv'
#==============================================================================
# 输出Excel
#==============================================================================
        excel_name = outname[:-4] + '.xlsx'
        excel_name = excel_name.decode('utf8')
        excel_name = excel_name.encode('gbk')
        workbook = xlsxwriter.Workbook(excel_name)
        
        worksheet = workbook.add_worksheet()
        bold = workbook.add_format({'bold': 1})
        
        row_number = 1
        height = 15
        
        # Add the worksheet data that the charts will refer to.
        worksheet.write_row('A'+str(row_number), [ u'物种拉丁名', s ], bold); row_number += 1
        worksheet.write_row('A'+str(row_number), [ u'物种中文名', LatinToChinese[s].decode('utf8') ], bold); row_number += 1
        worksheet.write_row('A'+str(row_number), [ u'年份', year ], bold); row_number += 1
        row_number += 1
        
        worksheet.write_row('A'+str(row_number), [ u'总数量' ], bold); row_number += 1
        for i in range(len(mass_unit_list)):
            if mass_unit_list[i] <> '千克': 
                worksheet.write_row('A'+str(row_number), [ mass_sum[i],str(mass_unit_list[i]).decode('utf8') ]); row_number += 1
        row_number += 1

        worksheet.write_row('A'+str(row_number), [ u'参考密度' ], bold); row_number += 1
        worksheet.write_row('A'+str(row_number), [ density[s], u'克/立方厘米' ]); row_number += 1
        row_number += 1

        worksheet.write_row('A'+str(row_number), [ u'总金额' ], bold); row_number += 1
        worksheet.write_row('A'+str(row_number), [ sum(cmonetary_sum)/10000, u'万元' ]); row_number += 1
        row_number += 1
#==============================================================================
# 
#==============================================================================
        worksheet.write_row('A'+str(row_number), [ u'进口国家及金额（按金额倒序排列）' ], bold); row_number += 1
        worksheet.write_row('A'+str(row_number), [ u'国家名称缩写',u'国家英文名',u'国家中文名',u'金额',u'单位' ], bold); row_number += 1; row_begin = row_number
        for i in range(len(export_country_list)):
            worksheet.write_row('A'+str(row_number), [ str(export_country_list[i]).decode('utf8'),str(DictCountryToEnglish[export_country_list[i]]).decode('utf8'),str(DictCountryToChinese[export_country_list[i]]).decode('utf8'),export_country_sum[i]/10000,u'万元' ]); row_number += 1
        row_end = row_number-1
        row_number += 1
        
        chart1 = workbook.add_chart({'type': 'pie'})
        chart1.add_series({
            'name':       '',
            'categories': '=Sheet1!$C$'+str(row_begin)+':$C$'+str(row_end),
            'values':     '=Sheet1!$D$'+str(row_begin)+':$D$'+str(row_end),
        })
        chart1.set_title({'name': year + u'年' + LatinToChinese[s].decode('utf8') + u'进口份额'})
        chart1.set_style(10)
        worksheet.insert_chart('G'+str(1), chart1, {'x_offset': 0, 'y_offset': 0})
#==============================================================================
# 
#==============================================================================
        worksheet.write_row('A'+str(row_number), [ u'出口口岸及金额（按金额倒序排列）' ], bold); row_number += 1
        worksheet.write_row('A'+str(row_number), [ u'口岸英文名',u'口岸中文名',u'金额',u'单位' ], bold); row_number += 1; row_begin = row_number
        for i in range(len(export_port_list)):
            worksheet.write_row('A'+str(row_number), [ str(export_port_list[i]).decode('utf8'),str(DictPortToChinese[export_port_list[i]]).decode('utf8'),export_port_sum[i]/10000,u'万元' ]); row_number += 1
        row_end = row_number-1
        row_number += 1
        chart2 = workbook.add_chart({'type': 'pie'})
        chart2.add_series({
            'name':       '',
            'categories': '=Sheet1!$B$'+str(row_begin)+':$B$'+str(row_end),
            'values':     '=Sheet1!$C$'+str(row_begin)+':$C$'+str(row_end),
        })
        chart2.set_title({'name': year + u'年' + LatinToChinese[s].decode('utf8') + u'出口口岸'})
        chart2.set_style(10)
        worksheet.insert_chart('G'+str(1+height), chart2, {'x_offset': 0, 'y_offset': 0})
#==============================================================================
# 
#==============================================================================
        worksheet.write_row('A'+str(row_number), [ u'进口口岸及金额（按金额倒序排列）' ], bold); row_number += 1
        worksheet.write_row('A'+str(row_number), [ u'口岸中文名',u'金额',u'单位' ], bold); row_number += 1; row_begin = row_number
        for i in range(len(import_port_list)):
            worksheet.write_row('A'+str(row_number), [ str(import_port_list[i]).decode('utf8'),import_port_sum[i]/10000,u'万元' ]); row_number += 1
        row_end = row_number-1
        row_number += 1
        chart3 = workbook.add_chart({'type': 'pie'})
        chart3.add_series({
            'name':       '',
            'categories': '=Sheet1!$A$'+str(row_begin)+':$A$'+str(row_end),
            'values':     '=Sheet1!$B$'+str(row_begin)+':$B$'+str(row_end),
        })
        chart3.set_title({'name': year + u'年' + LatinToChinese[s].decode('utf8') + u'进口口岸'})
        chart3.set_style(10)
        worksheet.insert_chart('G'+str(1+height*2), chart3, {'x_offset': 0, 'y_offset': 0})
#==============================================================================
# 
#==============================================================================
        worksheet.write_row('A'+str(row_number), [ u'货物类型及金额（按金额倒序排列）' ], bold); row_number += 1
        worksheet.write_row('A'+str(row_number), [ u'货物类型',u'金额',u'单位' ], bold); row_number += 1; row_begin = row_number
        for i in range(len(goods_type_list)):
            worksheet.write_row('A'+str(row_number), [ str(goods_type_list[i]).decode('utf8'),goods_type_sum[i]/10000,u'万元' ]); row_number += 1
        row_end = row_number-1
        row_number += 1
        chart4 = workbook.add_chart({'type': 'pie'})
        chart4.add_series({
            'name':       '',
            'categories': '=Sheet1!$A$'+str(row_begin)+':$A$'+str(row_end),
            'values':     '=Sheet1!$B$'+str(row_begin)+':$B$'+str(row_end),
        })
        chart4.set_title({'name': year + u'年' + LatinToChinese[s].decode('utf8') + u'货物类型'})
        chart4.set_style(10)
        worksheet.insert_chart('G'+str(1+height*3), chart4, {'x_offset': 0, 'y_offset': 0})
#==============================================================================
# 
#==============================================================================
        worksheet.write_row('A'+str(row_number), [ u'原产国' ], bold); row_number += 1
        worksheet.write_row('A'+str(row_number), [ u'国家名称缩写',u'国家英文名',u'国家中文名' ], bold); row_number += 1
        for i in range(len(country_origin_list)):
            worksheet.write_row('A'+str(row_number), [ str(country_origin_list[i]).decode('utf8'),str(DictCountryToEnglish[country_origin_list[i]]).decode('utf8'),str(DictCountryToChinese[country_origin_list[i]]).decode('utf8') ]); row_number += 1
        row_number += 1
#==============================================================================
# 
#==============================================================================
        worksheet.write_row('A'+str(row_number), [ u'来源' ], bold); row_number += 1
        for i in range(len(origin_list)):
            worksheet.write_row('A'+str(row_number), [ str(origin_list[i]).decode('utf8') ]); row_number += 1
        row_number += 1
        
        workbook.close()
#==============================================================================
# 总体统计数据
#==============================================================================
        latin_name.append(s.decode('utf8'))
        
        chinese_name.append(LatinToChinese[s].decode('utf8'))
            
        u = u''
        for i in range(len(mass_unit_list)):
            if mass_unit_list[i] <> '千克': 
                u += u'%.2f%s\n' % (mass_sum[i], str(mass_unit_list[i]).decode('utf8'))
        import_number.append(u[:-1])

        import_money.append(u'%.2f' % float(sum(cmonetary_sum)/10000.0))

        u = u''
        for i in range(len(export_country_list)):
            u += u'%s %.2f\n' % (str(DictCountryToChinese[export_country_list[i]]).decode('utf8'),export_country_sum[i]/10000.0)
            if i >=2:
                break
        import_country_top3.append(u)
        
        u = u''
        for i in range(len(export_port_list)):
            u += u'%s %.2f\n' % (str(DictPortToChinese[export_port_list[i]]).decode('utf8'),export_port_sum[i]/10000.0)
            if i >=2:
                break
        export_port_top3.append(u)
        
        u = u''
        for i in range(len(import_port_sum)):
            u += u'%s %.2f\n' % (str(import_port_list[i]).decode('utf8'),import_port_sum[i]/10000.0)
            if i >=2:
                break
        import_port_top3.append(u)
        
        u = u''
        for i in range(len(country_origin_list)):
            u += u'%s\n' % (str(DictCountryToChinese[country_origin_list[i]]).decode('utf8'))
            if i >=2:
                break
        origin_country_top3.append(u)
#==============================================================================
# 输出Excel 一、	####年各树种进口数量及进口金额
#==============================================================================
outname = outpath + year + '年各树种进口数量及进口金额' + '.csv'
excel_name = outname[:-4] + '.xlsx'
excel_name = excel_name.decode('utf8')
excel_name = excel_name.encode('gbk')
workbook = xlsxwriter.Workbook(excel_name)

worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': 1})

row_number = 1
height = 15

worksheet.write_row('A'+str(row_number), [ u'树种拉丁名',u'树种中文名',u'进口数量',u'进口金额（万元）' ], bold); row_number += 1
for i in range(len(latin_name)):
#    print repr(latin_name[i])
#    print repr(chinese_name[i])
#    print repr(import_number[i])
#    print repr(import_money[i])
    worksheet.write_row('A'+str(row_number), [ latin_name[i], chinese_name[i], import_number[i], import_money[i] ], bold); row_number += 1
workbook.close()
#==============================================================================
# 输出Excel 二、	####年各树种进口国家（前三位）、进口口岸（前三位）、出口口岸（前三位）及原产国（取三个）
#==============================================================================
outname = outpath + year + '年各树种进口国家（前三位）、进口口岸（前三位）、出口口岸（前三位）及原产国（取三个）' + '.csv'
excel_name = outname[:-4] + '.xlsx'
excel_name = excel_name.decode('utf8')
excel_name = excel_name.encode('gbk')
workbook = xlsxwriter.Workbook(excel_name)

worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': 1})

row_number = 1
height = 15

worksheet.write_row('A'+str(row_number), [ u'树种拉丁名',u'树种中文名',u'主要进口国家及金额（万元）',u'主要进口口岸及金额（万元）',u'主要出口口岸及金额（万元）' ,u'原产国'  ], bold); row_number += 1
for i in range(len(latin_name)):
    worksheet.write_row('A'+str(row_number), [ latin_name[i], chinese_name[i], import_country_top3[i], import_port_top3[i], export_port_top3[i],  origin_country_top3[i]], bold); row_number += 1
workbook.close()