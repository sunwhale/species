# -*- coding: gbk -*-

import codecs
import numpy as np
import os
import matplotlib.pyplot as plt

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
    
inpath = 'C:\\Users\\sunwhale\\Desktop\\数据统计2\\整理好数据\\all\\'
outpath = 'C:\\Users\\sunwhale\\Desktop\\数据统计2\\整理好数据\\2013output\\'


if not os.path.isdir(outpath):
    os.makedirs(outpath)
    print 'Create new directory:',outpath
    
filenames = getFiles(inpath)
#==============================================================================
# 2014
#==============================================================================
shuzhong = ['Cassia sia',
'Cedrela odorata',
'fusca',
'odorifera',
'Dalbergia bariensis',
'Dalbergia cearensis',
'Dalbergia cochi',
'Dalbergia cultrata',
'Dalbergia frutescens',
'Dalbergia latifolia',
'Dalbergia melanoxylon',
'Dalbergia oliveri',
'Dalbergia retusa',
'Dalbergia spruceana',
'Diospyros cele',
'Diospyros crassiflo',
'Diospyros ebenum',
'Diospyros phili',
'Diospyros pilosanthera',
'Ebenaceae spp.',
'mandshurica',
'Mesua  ferrea',
'Millettia laurentii',
'eucan',
'Millettia pendula',
'koraiensis',
'indicus',
'Pterocarpus  santalinus',
'Pterocarpus cambodianus',
'Pterocarpus erinaceus',
'Pterocarpus macarocarpus',
#'Pterocarpus macrocarpus',
'Pterocarpus marsupium',
'Pterocarpus pedatus',
'Quercus  mongolica',
'mahagoni',
'macrophylla',
'undefined',
]

for s in shuzhong[:1]:
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
    
    for filename in filenames:
        fullname = filename[0] + '\\' + filename[1]
#        print 'Reading: ' + filename[1]
        if isTextFile(filename[1]):
            infile = open(fullname,'r')
            list1 = infile.readlines()
            list2 = [i.strip() for i in list1[:]]
            list3 = [i.split('\t') for i in list2[2:]]
            for r in list3:
                species_list.append(r[9])
            result = [ i for i in list3 if s.lower() in i[9].lower()]
#            for i in list3:
#                if s.lower() in i[9].lower():
#                    print filename[1]

            for r in result:
                export_country_list.append(r[5])
                mass_unit_list.append(r[13])
                cmonetary_unit_list.append(r[39])
#                species_list.append(r[9])
#                species_chinese_list.append(r[8])
                export_port_list.append(r[46])
                country_origin_list.append(r[14])
                origin_list.append(r[26])
                import_port_list.append(r[54])
                
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
    
    import_port_list.sort()
    export_country_list.sort()
    export_port_list.sort()
    country_origin_list.sort()
    origin_list.sort()
    
    species_list.sort()
    for ss in species_list:
        print ss
    
    for filename in filenames:
        fullname = filename[0] + '\\' + filename[1]
        outname = fullname.replace('\\','_')
        outname = outname.replace(':','')
        outname = outname[:-4] + '.txt'
        if isTextFile(filename[1]):
#            print 'Reading: ' + filename[1]
            infile = open(fullname,'r')
            list1 = infile.readlines()
            list2 = [i.strip() for i in list1[:]]
            list3 = [i.split('\t') for i in list2[2:]]
            
#            item = list2[1].split('\t')
#            for i in range(len(item)):
#                print i,item[i],list3[0][i]
                
            result = [ i for i in list3 if s.lower() in i[9].lower()]
            
            for r in result:
                export_country_list.append(r[5])
            export_country_list = list(set(export_country_list))
    
            for r in result:
                for i in range(len(mass_unit_list)):
                    if r[13] == mass_unit_list[i]:
                        mass_sum[i]+=float(r[12])
                        
                for i in range(len(cmonetary_unit_list)):
                    if r[39] == cmonetary_unit_list[i]:
                        cmonetary_sum[i]+=float(r[38])
                        
                for i in range(len(export_country_list)):
                    if r[5] == export_country_list[i]:
                        export_country_sum[i]+=float(r[38])
                        
                for i in range(len(export_port_list)):
                    if r[46] == export_port_list[i]:
                        export_port_sum[i]+=float(r[38])
                        
                for i in range(len(import_port_list)):
                    if r[54] == import_port_list[i]:
                        import_port_sum[i]+=float(r[38])
                        
    print sum(export_port_sum)
    print sum(cmonetary_sum)
    print sum(export_country_sum)
    print sum(import_port_sum)
                        
    print '----------'  
#    print export_country_list
#    print mass_unit_list
#    print cmonetary_unit_list
    
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
        
    print '原产国： '
    print country_origin_list
    
    print '来源： '
    print origin_list

    print '----------'              
    
    outfile = open(outpath + s + '_2013' + '.csv', 'w')
    print outpath + s + '_2013' + '.csv'
    outfile.writelines('总数量'+'\n')
    for i in range(len(mass_unit_list)):
        outfile.writelines( str(mass_sum[i])+','+str(mass_unit_list[i])+'\n' )
    outfile.writelines('\n')
    
    
    outfile.writelines('总金额'+'\n')
    for i in range(len(cmonetary_unit_list)):
        outfile.writelines( str(cmonetary_sum[i])+','+str(cmonetary_unit_list[i])+'\n' )
    outfile.writelines('\n')
    
    
    outfile.writelines('进口份额'+'\n')
    for i in range(len(export_country_list)):
        outfile.writelines( str(export_country_list[i])+','+str(export_country_sum[i])+'\n' )
    outfile.writelines('\n')
    
    
    outfile.writelines('出口口岸'+'\n')
    for i in range(len(export_port_list)):
        outfile.writelines( str(export_port_list[i])+','+str(export_port_sum[i])+'\n' )
    outfile.writelines('\n')
    
    outfile.writelines('进口口岸'+'\n')
    for i in range(len(import_port_list)):
        outfile.writelines( str(import_port_list[i])+','+str(import_port_sum[i])+'\n' )
    outfile.writelines('\n')
    
    outfile.writelines('原产国：'+'\n')
    for country_origin in country_origin_list:
        outfile.writelines( country_origin+'\n' )
    outfile.writelines('\n')
    
    outfile.writelines('来源：'+'\n')
    for origin in origin_list:
        outfile.writelines( origin+'\n' )

                
            