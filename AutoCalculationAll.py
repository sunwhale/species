# -*- coding: utf-8 -*-

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
inpath = 'F:\\GitHub\\species\\物种证明'+year+'整理好txt\\'
outpath = 'F:\\GitHub\\species\\'+year+'output\\'

if not os.path.isdir(outpath):
    os.makedirs(outpath)
    print 'Create new directory:',outpath
    
filenames = getFiles(inpath)

for s in [year]:
    print '----------'
    print '物种拉丁学名：' + s
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
#        print 'Reading: ' + filename[1]
        if isTextFile(filename[1]):
            infile = open(fullname,'r')
            list1 = infile.readlines()
            list2 = [i.strip() for i in list1[:]]
            list3 = [i.split('\t') for i in list2[2:]]
#            for r in list3:
#                species_list.append(r[9])
            result = [ i for i in list3 if DataToLatin[i[9]] in Latin ]
#            for i in list3:
#                if i[46] == "\"TG.PRIOK,JAKARTA\"":
#                    print DictCountryToChinese[DictCountry[i[5]]],i[50],filename[1]

#            for r in result:
##                if r[5]=='VU':
##                    print r[46]
##                export_country_list.append(DictCountry[r[5]])
#                if r[5] not in DictCountry.keys():
#                    export_country_list.append(r[5])
##                mass_unit_list.append(DictUnit[r[13]])
#                if r[13] not in DictUnit.keys():
#                    mass_unit_list.append(r[13])
#                cmonetary_unit_list.append(r[39])
#                species_list.append(r[9])
##                species_chinese_list.append(r[8])
#
##                export_port_list.append(DictPort[r[46]])
#                if r[46] not in DictPort.keys():
#                    export_port_list.append(r[46])
##                country_origin_list.append(DictCountry[r[14]])
#                country_origin_list.append(r[14])
#                if r[26] not in DictOrigin.keys():
#                    origin_list.append(DictOrigin[r[26]])
##                import_port_list.append(DictImport[r[54]])
#                if r[54] not in DictImport.keys():
#                    import_port_list.append(r[54])
##                goods_type_list.append(DictGoodsType[r[10]])
#                if r[10] not in DictGoodsType.keys():
#                    goods_type_list.append(r[10])
            
            for r in result:
#                if r[5]=='VU':
#                    print r[46]
                export_country_list.append(DictCountry[r[5]])
#                export_country_list.append(r[5])
                mass_unit_list.append(DictUnit[r[13]])
#                mass_unit_list.append(r[13])
                cmonetary_unit_list.append(r[39])
                species_list.append(r[9])
#                species_chinese_list.append(r[8])

                export_port_list.append(DictPort[r[46]])
#                export_port_list.append(r[46])
                country_origin_list.append(DictCountry[r[14]])
#                country_origin_list.append(r[14])
                origin_list.append(DictOrigin[r[26]])
                import_port_list.append(DictImport[r[54]])
#                import_port_list.append(r[54])
                goods_type_list.append(DictGoodsType[r[10]])
#                goods_type_list.append(r[10])
                
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
    
#    print '--------------------species_list--------------------'
#    for species in species_list:
#        print species
    print '--------------------export_country_list--------------------'
    for export_country in export_country_list:
        print export_country
    print '--------------------export_port_list--------------------'
    for export_port in export_port_list:
        print export_port
    print '--------------------import_port_list--------------------'
    for import_port in import_port_list:
        print import_port
    print '--------------------goods_type_list--------------------'
    for goods_type in goods_type_list:
        print goods_type
    print '--------------------mass_unit_list--------------------'
    for mass_unit in mass_unit_list:
        print mass_unit
    print '--------------------origin_list--------------------'
    for origin in origin_list:
        print origin
    
    for filename in filenames:
        fullname = filename[0] + '\\' + filename[1]
        outname = fullname.replace('\\','_')
        outname = outname.replace(':','')
        outname = outname[:-4] + '.txt'
        if isTextFile(filename[1]):
            print 'Reading: ' + filename[1]
            infile = open(fullname,'r')
            list1 = infile.readlines()
            list2 = [i.strip() for i in list1[:]]
            list3 = [i.split('\t') for i in list2[2:]]
            
#            item = list2[1].split('\t')
#            for i in range(len(item)):
#                print i,item[i],list3[0][i]
#==============================================================================
# All                
#==============================================================================
#            result = [ i for i in list3 if DataToLatin[i[9]] in Latin ]
#==============================================================================
# Hongmu
#==============================================================================
            result = [ i for i in list3 if DataToLatin[i[9]] in Latin ]

            s = '全部树种'
#            s = '红木类'
#            s = '濒危树种'     
            outname = outpath + year + '_' + s + '_' + 'All' + '.csv'  
            
#            for r in result:
#                export_country_list.append(r[5])
#            export_country_list = list(set(export_country_list))
    
            for r in result:
            
#                for i in list3:
#                    if DataToLatin[r[9]] in hongmu:
#                        print i[0],filename[1]
            
                
                for i in range(len(mass_unit_list)):
                    if DictUnit[r[13]] == mass_unit_list[i]:
                        mass_sum[i]+=float(r[12])
                        
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
                        
    if sum(export_port_sum)>0:
        print '----------'  
#        print export_country_list
#        print mass_unit_list
#        print cmonetary_unit_list
        
        print '总数量: '
        for i in range(len(mass_unit_list)):
            print str(mass_sum[i])+':'+str(mass_unit_list[i])
        print '总金额: '
        for i in range(len(cmonetary_unit_list)):
            print str(cmonetary_sum[i])+':'+str(cmonetary_unit_list[i])
        print '进口份额: '
        for i in range(len(export_country_list)):
            print str(export_country_list[i])+':'+str(export_country_sum[i])
    
        print '出口口岸: '
        for i in range(len(export_port_list)):
            print str(export_port_list[i])+':'+str(export_port_sum[i])
            
        print '进口口岸: '
        for i in range(len(import_port_list)):
            print str(import_port_list[i])+':'+str(import_port_sum[i])
            
        print '货物类型: '
        for i in range(len(goods_type_list)):
            print str(goods_type_list[i])+':'+str(goods_type_sum[i])
            
        print '原产国： '
        print country_origin_list
        
        print '来源： '
        for origin in origin_list:
            print origin
    
        print '----------'              
        

#        outfile = open(outname, 'w')
#        print outname
#        outfile.writelines( '物种拉丁学名,' + s + '\n')
#        outfile.writelines( '物种中文名,' + s + '\n')
#        outfile.writelines('总数量'+'\n')
#        for i in range(len(mass_unit_list)):
#            outfile.writelines( str(mass_sum[i])+','+str(mass_unit_list[i])+'\n' )
#        outfile.writelines('\n')
#        
#        
#        outfile.writelines('总金额'+'\n')
##        for i in range(len(cmonetary_unit_list)):
##            outfile.writelines( str(cmonetary_sum[i])+','+str(cmonetary_unit_list[i])+'\n' )
##        outfile.writelines('\n')
#        outfile.writelines( str(sum(cmonetary_sum))+','+'CNY'+'\n' )
#        outfile.writelines('\n')
#        
#        
#        outfile.writelines('进口份额'+'\n')
#        for i in range(len(export_country_list)):
#            outfile.writelines( str(export_country_list[i])+','+str(DictCountryToEnglish[export_country_list[i]])+','+str(DictCountryToChinese[export_country_list[i]])+','+str(export_country_sum[i])+'\n' )
#        outfile.writelines('\n')
#        
#        
#        outfile.writelines('出口口岸'+'\n')
#        for i in range(len(export_port_list)):
#            outfile.writelines( str(export_port_list[i])+','+str(DictPortToChinese[export_port_list[i]])+','+str(export_port_sum[i])+'\n' )
#        outfile.writelines('\n')
#        
#        outfile.writelines('进口口岸'+'\n')
#        for i in range(len(import_port_list)):
#            outfile.writelines( str(import_port_list[i])+','+str(import_port_sum[i])+'\n' )
#        outfile.writelines('\n')
#        
#        outfile.writelines('货物类型'+'\n')
#        for i in range(len(goods_type_list)):
#            outfile.writelines( str(goods_type_list[i])+','+str(goods_type_sum[i])+'\n' )
#        outfile.writelines('\n')
#        
#        outfile.writelines('原产国：'+'\n')
#        for i in range(len(country_origin_list)):
#            outfile.writelines( str(country_origin_list[i])+','+str(DictCountryToEnglish[country_origin_list[i]])+','+str(DictCountryToChinese[country_origin_list[i]])+'\n' )
#        outfile.writelines('\n')
        
#        outfile.writelines('来源：'+'\n')
#        for origin in origin_list:
#            outfile.writelines( origin+'\n' )
#==============================================================================
# 输出Excel
#==============================================================================
        
        workbook = xlsxwriter.Workbook(outname[:-4] + '.xlsx')
        print outname[:-4]
        worksheet = workbook.add_worksheet()
        bold = workbook.add_format({'bold': 1})
        
        row_number = 1
        height = 15
        
        # Add the worksheet data that the charts will refer to.
  
        worksheet.write_row('A'+str(row_number), [ '类型',s ], bold); row_number += 1
        worksheet.write_row('A'+str(row_number), [ '年份', year ], bold); row_number += 1
        row_number += 1
        
        worksheet.write_row('A'+str(row_number), [ '总数量' ], bold); row_number += 1
        for i in range(len(mass_unit_list)):
            worksheet.write_row('A'+str(row_number), [ mass_sum[i],str(mass_unit_list[i]) ]); row_number += 1
        row_number += 1

        worksheet.write_row('A'+str(row_number), ['总金额' ], bold); row_number += 1
        worksheet.write_row('A'+str(row_number), [ sum(cmonetary_sum)/10000,'万元' ]); row_number += 1
        row_number += 1
#==============================================================================
# 
#==============================================================================
        worksheet.write_row('A'+str(row_number), [ '进口国家及金额（按金额倒序排列）' ], bold); row_number += 1
        worksheet.write_row('A'+str(row_number), [ '国家名称缩写','国家英文名','国家中文名','金额','单位' ], bold); row_number += 1; row_begin = row_number
        for i in range(len(export_country_list)):
            worksheet.write_row('A'+str(row_number), [ str(export_country_list[i]),str(DictCountryToEnglish[export_country_list[i]]),str(DictCountryToChinese[export_country_list[i]]),export_country_sum[i]/10000,'万元' ]); row_number += 1
        row_end = row_number-1
        row_number += 1
        
        chart1 = workbook.add_chart({'type': 'pie'})
        chart1.add_series({
            'name':       '',
            'categories': '=Sheet1!$C$'+str(row_begin)+':$C$'+str(row_end),
            'values':     '=Sheet1!$D$'+str(row_begin)+':$D$'+str(row_end),
        })
        chart1.set_title({'name': year + '年' + s + '进口份额'})
        chart1.set_style(10)
        worksheet.insert_chart('G'+str(1), chart1, {'x_offset': 0, 'y_offset': 0})
#==============================================================================
# 
#==============================================================================
        worksheet.write_row('A'+str(row_number), [ '出口口岸及金额（按金额倒序排列）' ], bold); row_number += 1
        worksheet.write_row('A'+str(row_number), [ '口岸英文名','口岸中文名','金额','单位' ], bold); row_number += 1; row_begin = row_number
        for i in range(len(export_port_list)):
            worksheet.write_row('A'+str(row_number), [ str(export_port_list[i]),str(DictPortToChinese[export_port_list[i]]),export_port_sum[i]/10000,'万元' ]); row_number += 1
        row_end = row_number-1
        row_number += 1
        chart2 = workbook.add_chart({'type': 'pie'})
        chart2.add_series({
            'name':       '',
            'categories': '=Sheet1!$B$'+str(row_begin)+':$B$'+str(row_end),
            'values':     '=Sheet1!$C$'+str(row_begin)+':$C$'+str(row_end),
        })
        chart2.set_title({'name': year + '年' + s + '出口口岸'})
        chart2.set_style(10)
        worksheet.insert_chart('G'+str(1+height), chart2, {'x_offset': 0, 'y_offset': 0})
#==============================================================================
# 
#==============================================================================
        worksheet.write_row('A'+str(row_number), [ '进口口岸及金额（按金额倒序排列）' ], bold); row_number += 1
        worksheet.write_row('A'+str(row_number), [ '口岸中文名','金额','单位' ], bold); row_number += 1; row_begin = row_number
        for i in range(len(import_port_list)):
            worksheet.write_row('A'+str(row_number), [ str(import_port_list[i]),import_port_sum[i]/10000,'万元' ]); row_number += 1
        row_end = row_number-1
        row_number += 1
        chart3 = workbook.add_chart({'type': 'pie'})
        chart3.add_series({
            'name':       '',
            'categories': '=Sheet1!$A$'+str(row_begin)+':$A$'+str(row_end),
            'values':     '=Sheet1!$B$'+str(row_begin)+':$B$'+str(row_end),
        })
        chart3.set_title({'name': year + '年' + s + '进口口岸'})
        chart3.set_style(10)
        worksheet.insert_chart('G'+str(1+height*2), chart3, {'x_offset': 0, 'y_offset': 0})
#==============================================================================
# 
#==============================================================================
        worksheet.write_row('A'+str(row_number), [ '货物类型及金额（按金额倒序排列）' ], bold); row_number += 1
        worksheet.write_row('A'+str(row_number), [ '货物类型','金额','单位' ], bold); row_number += 1; row_begin = row_number
        for i in range(len(goods_type_list)):
            worksheet.write_row('A'+str(row_number), [ str(goods_type_list[i]),goods_type_sum[i]/10000,'万元' ]); row_number += 1
        row_end = row_number-1
        row_number += 1
        chart4 = workbook.add_chart({'type': 'pie'})
        chart4.add_series({
            'name':       '',
            'categories': '=Sheet1!$A$'+str(row_begin)+':$A$'+str(row_end),
            'values':     '=Sheet1!$B$'+str(row_begin)+':$B$'+str(row_end),
        })
        chart4.set_title({'name': year + '年' + s + '货物类型'})
        chart4.set_style(10)
        worksheet.insert_chart('G'+str(1+height*3), chart4, {'x_offset': 0, 'y_offset': 0})
#==============================================================================
# 
#==============================================================================
        worksheet.write_row('A'+str(row_number), [ '原产国' ], bold); row_number += 1
        worksheet.write_row('A'+str(row_number), [ '国家名称缩写','国家英文名','国家中文名' ], bold); row_number += 1
        for i in range(len(country_origin_list)):
            worksheet.write_row('A'+str(row_number), [ str(country_origin_list[i]),str(DictCountryToEnglish[country_origin_list[i]]),str(DictCountryToChinese[country_origin_list[i]]) ]); row_number += 1
        row_number += 1
#==============================================================================
# 
#==============================================================================
        worksheet.write_row('A'+str(row_number), [ '来源' ], bold); row_number += 1
        for i in range(len(origin_list)):
            worksheet.write_row('A'+str(row_number), [ str(origin_list[i]) ]); row_number += 1
        row_number += 1
        
        workbook.close()