﻿# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 14:48:30 2016

@author: sunwhale
"""

DictImport={
"":"未列出",\
"  SHANGHAI":"上海",\
" SHANGHAI":"上海",\
" 东莞沙田":"东莞沙田",\
" 防城":"广州防城",\
" 防城  ":"广州防城",\
" 防城   ":"广州防城",\
" 黄埔":"广州黄埔",\
" 江门":"广东江门",\
"\"SHATIAN,CHINA\"":"东莞沙田",\
"\"SHATIAN,DONGGUAN\"":"东莞沙田",\
"\"SHIHU,QUANZHOU\"":"泉州",\
"\"WEITOU,QUANZHOU\"":"泉州",\
"\"ZHONGSHAN,CHINA\"":"广东中山",\
"?SHANGHAI":"上海",\
"BAIYUN AIRPORT":"广州",\
"BEI HAI":"广西北海",\
"BEIHAI":"广西北海",\
"BEIJING":"北京",\
"BEIJING CHAOYANG":"北京",\
"CHANGBAI":"吉林长白",\
"CHANGSHU":"常熟",\
"CHENGDU":"成都",\
"CHIWAN":"深圳赤湾",\
"CHONGQING":"重庆",\
"CN":"CN",\
"DACHANWAN":"深圳大铲湾",\
"DALIAN":"大连",\
"DALIAN DA YAO WAN GANG":"大连",\
"DANDONG":"丹东",\
"DONGGUAN":"东莞",\
"DONGGUAN SHATIAN":"东莞沙田",\
"DONGGUANSHATIAN":"东莞沙田",\
"DONGXING":"广西东兴",\
"FANGCHENG":"广州防城",\
"FANGCHENGGANG":"广州防城",\
"FRANKFURT":"法兰克福",\
"FUZHOU":"福州",\
"GAOMING":"佛山高明",\
"GAOMING SHICHU PORT":"佛山高明",\
"GUANGZHOU":"广州",\
"GUANGZHOU ":"广州",\
"GUANGZHOU JIAOXIN PORT":"广州",\
"HAIKOU":"海口",\
"HANGZHOU":"杭州",\
"HAUNGPU":"广州黄埔",\
"HEKOU":"云南河口",\
"HONGKONG":"香港",\
"HUADU":"广州",\
"HUANG PU":"广州黄埔",\
"HUANGOU":"广州黄埔",\
"HUANGPU":"广州黄埔",\
"HUANGPU ":"广州黄埔",\
"HUANGPU GUANGZHOU":"广州黄埔",\
"HUANGPU OLD PORT":"广州黄埔",\
"HUANGPU PORT":"广州黄埔",\
"HULIN":"黑龙江虎林",\
"JIANG MEN":"广西江门",\
"JIANGMEAN WAIHAI PORT":"广西江门",\
"JIANGMEN":"广西江门",\
"JIANGMEN WAIHAI PORT":"广西江门",\
"JIAO XIN":"JIAOXIN",\
"JIAOXIN":"JIAOXIN",\
"JIAXING":"嘉兴",\
"JINGJIANG":"靖江",\
"JINGJIANG ":"靖江",\
"KIROVSKLES":"KIROVSKLES",\
"LAOS":"老挝",\
"LIANHUASHAN":"番禺莲花山",\
"LIANYUNGANG":"连云港",\
"LIN JIANG CHANGBAIBADAOGOU":"吉林长白",\
"LIN JIANG/CHANGBAIBADAOGOU":"吉林长白",\
"LONGBANG":"LONGBANG",\
"LUZHOU":"泸州",\
"MAWEI":"福州马尾",\
"MENGLA":"云南勐腊",\
"MOHAN":"云南磨憨",\
"NANSHA":"广州南沙",\
"NANSHA NEW PORT":"广州南沙",\
"NANTONG":"江苏南通",\
"NANTONG ":"江苏南通",\
"NEW YORK":"纽约",\
"NINGBO":"宁波",\
"PINGXIANG":"广西凭祥",\
"PINXIANG":"广西凭祥",\
"PORT OF XIUYU":"福建莆田秀屿",\
"PUTIAN":"福建莆田",\
"QINGDAO":"青岛",\
"QINGDAO ":"青岛",\
"QINGDDAO":"青岛",\
"RUILI":"云南瑞丽",\
"SHAGNHAI":"上海",\
"SHANG HAI":"上海",\
"SHANG HAI ":"上海",\
"SHANGHAI":"上海",\
"SHANGHAI ":"上海",\
"SHANGHIA":"上海",\
"SHANHAI":"上海",\
"SHANTOU":"广东汕头",\
"SHATIAN":"东莞沙田",\
"SHATIAN PORT":"东莞沙田",\
"SHEKOU":"深圳蛇口",\
"SHENZHEN":"深圳",\
"SHIFENHE":"绥芬河",\
"SHITIAN":"SHITIAN",\
"SHNGHAI":"上海",\
"SHUIFENHE":"绥芬河",\
"SUFENHE":"绥芬河",\
"SUIFEHE":"绥芬河",\
"SUIFENGHE":"绥芬河",\
"SUIFENHE":"绥芬河",\
"Shanghai":"上海",\
"TAICANG":"苏州太仓",\
"TAIZHOU":"泰州",\
"TIANJIN":"天津",\
"TIANJIN ":"天津",\
"TIANJIN XINGANG":"天津",\
"TIANJINXINGANG":"天津",\
"WEIHAI":"威海",\
"WENJINDU":"深圳文锦渡",\
"WENZHOU":"温州",\
"XIAMEN":"厦门",\
"XINGANG":"天津新港",\
"XINHUI":"广东江门新会",\
"XISHUANGBANNA":"西双版纳",\
"XIUYU":"福建莆田秀屿",\
"YANGZHOU":"扬州",\
"YANTAI":"烟台",\
"YANTIAN":"深圳盐田",\
"YANTIAN PORT":"深圳盐田",\
"YINGJIANG":"云南盈江",\
"YIWU":"义乌",\
"YIWU ":"义乌",\
"YOU YI GUAN":"凭祥友谊关",\
"YOUYI GUAN":"凭祥友谊关",\
"YOUYI HUAN":"凭祥友谊关",\
"YOUYIGUAN":"凭祥友谊关",\
"ZHANG JIA GANG":"张家港",\
"ZHANGFENG":"云南章凤",\
"ZHANGJIAGANG":"张家港",\
"ZHANGJIAGANG ":"张家港",\
"ZHANGJIAGNAG":"张家港",\
"ZHANGJIANGANG":"张家港",\
"ZHAPU":"浙江乍浦",\
"ZHENJIANG":"镇江",\
"ZHONGSHAN":"广东中山",\
"ZHONGSHAN PORT":"广东中山",\
"ZHONGSHAN PORTO":"广东中山",\
"ZHOUSHAN":"浙江舟山",\
"shanghai":"上海",\
"版纳（240）":"西双版纳",\
"沧源":"云南沧源",\
"岔河":"岔河",\
"长沙":"长沙",\
"赤湾":"深圳赤湾",\
"打洛":"云南打洛",\
"大鹏":"大鹏",\
"东兴":"广西东兴",\
"东莞":"东莞",\
"东莞沙田":"东莞沙田",\
"东莞沙田港":"东莞沙田",\
"东莞少田":"东莞沙田",\
"东莞太平港":"东莞太平港",\
"番禺莲花山":"番禺莲花山",\
"番禺莲花山港":"番禺莲花山",\
"芳村":"广州芳村",\
"防城":"广州防城",\
"防城 ":"广州防城",\
"防城  ":"广州防城",\
"防城   ":"广州防城",\
"防城    ":"广州防城",\
"防城港":"广州防城",\
"佛山":"广东佛山",\
"佛山澜石":"广东佛山",\
"佛山新港":"广东佛山",\
"关累":"云南勐腊关累",\
"广州":"广州",\
"广州黄埔":"广州黄埔",\
"广州黄埔港":"广州黄埔",\
"广州黄埔旧港大码头":"广州黄埔",\
"广州黄埔老港":"广州黄埔",\
"广州机场":"广州",\
"广州窖心":"广州窖心",\
"广州窖心港":"广州窖心",\
"广州南沙":"广州南沙",\
"广州新风港":"广州新风港",\
"海口":"海口",\
"河口":"云南河口",\
"猴桥":"云南腾冲猴桥",\
"虎门":"广东东莞虎门",\
"花都":"广州花都",\
"花都港":"广州花都",\
"黄埔":"广州黄埔",\
"黄埔 ":"广州黄埔",\
"黄埔  ":"广州黄埔",\
"黄埔 HUANGPU":"广州黄埔",\
"黄埔　":"广州黄埔",\
"黄埔港":"广州黄埔",\
"黄埔港 ":"广州黄埔",\
"黄埔关区":"广州黄埔",\
"黄埔口岸":"广州黄埔",\
"黄埔老港":"广州黄埔",\
"黄浦":"广州黄埔",\
"黄檀":"黄檀",\
"皇岗":"深圳皇岗",\
"江门":"广东江门",\
"江门外海":"广东江门",\
"江门外海码头":"广东江门",\
"江山":"浙江江山",\
"金水河":"金水河",\
"景洪":"云南景洪",\
"九江":"江西九江",\
"九洲港":"珠海九洲港",\
"勒流":"佛山勒流",\
"勒流港":"佛山勒流",\
"莲花山":"番禺莲花山",\
"陇川":"云南陇川",\
"马鹿塘":"云南马鹿塘",\
"马尾":"福州马尾",\
"曼庄":"云南勐腊",\
"孟定":"云南孟定",\
"孟连":"云南孟连",\
"磨憨":"云南磨憨",\
"木姐":"瑞丽木姐",\
"南港":"天津南港",\
"南伞":"云南南伞",\
"南沙":"广州南沙",\
"南沙港":"广州南沙",\
"南沙新港":"广州南沙",\
"南通":"南通",\
"南伟码头":"广州南沙南伟",\
"宁波":"宁波",\
"弄岛":"瑞丽弄岛",\
"片马":"云南片马",\
"片马(丹珠通道)":"云南片马",\
"凭祥":"广西凭祥",\
"凭祥 ":"广西凭祥",\
"凭祥友谊关":"凭祥友谊关",\
"钦保":"广西钦保",\
"青岛":"青岛",\
"清水河":"清水河",\
"瑞丽":"瑞丽",\
"三山":"安徽三山",\
"三山港":"安徽三山",\
"三水":"广东佛山三水",\
"沙田":"沙田",\
"沙田 SHATIAN":"沙田",\
"汕头":"广东汕头",\
"上海":"上海",\
"上海 SHANGHAI":"上海",\
"上海SHANGHAI":"上海",\
"上海外高桥港":"上海",\
"蛇口":"深圳蛇口",\
"深圳":"深圳",\
"深圳赤湾":"深圳赤湾",\
"深圳皇岗":"深圳皇岗",\
"深圳蛇口":"深圳蛇口",\
"深圳盐田":"深圳盐田",\
"深圳盐田港":"深圳盐田",\
"神湾":"广东中山神湾",\
"神湾港":"广东中山神湾",\
"水东":"广东水东",\
"顺德":"广东顺德",\
"绥芬河":"绥芬河",\
"台山":"广东台山",\
"台山公益港":"广东台山",\
"泰国":"泰国",\
"太平":"太平",\
"腾冲":"云南腾冲",\
"天保":"云南天保",\
"天津":"天津",\
"天津新港":"天津",\
"文锦渡":"深圳文锦渡",\
"乌鲁木齐机场":"乌鲁木齐机场",\
"梧州":"广西梧州",\
"西双版纳":"西双版纳",\
"厦门":"厦门",\
"新港":"天津新港",\
"新会":"广东江门新会",\
"新会港":"广东江门新会",\
"秀屿港":"福建莆田秀屿",\
"盐田":"深圳盐田",\
"盐田港":"深圳盐田",\
"义乌":"义乌",\
"盈江":"云南盈江",\
"永和":"永和",\
"友谊":"凭祥友谊关",\
"友谊关":"凭祥友谊关",\
"云浮":"广东云浮",\
"云浮新港":"广东云浮",\
"增城":"广州增城",\
"章凤":"云南章凤",\
"张家港":"张家港",\
"肇庆三榕":"肇庆三榕",\
"肇庆三榕港":"肇庆三榕",\
"镇江":"镇江",\
"中港":"中港",\
"中山":"广东中山",\
"中山港":"广东中山",\
"珠海":"珠海",\
"珠海九洲港":"珠海",\
"勐康":"云南勐康",\
"勐腊":"云南勐腊",\
"畹丁":"云南畹町",\
"畹叮":"云南畹町",\
"畹町":"云南畹町",\
'ZHAO QING':"肇庆",\
'NANJING':"南京",\
'KUNMING':"昆明",\
'ZHANGSHAN':"中山",\
" GUANGZHOU":"广州",\
"MAWEI,FUZHOU":"福州",\
"ANQING":"安庆",\
"CHANGSHA":"长沙",\
"FANGCHENG PORT":"广州防城",\
"FANGCHRNG PORT":"广州防城",\
"GECHENG":"绥芬河",\
"GUCHENGLI":"延吉古城里",\
"HUNCHUN":"吉林珲春",\
"Huangpu":"广州黄埔",\
"JIAN":"通化吉安",\
"JIAN/QINGSHI/LAOHUSHAO":"通化吉安",\
"JIANGMEN WAI HAI PORT":"江门",\
"JIAN\QINGSHI":"通化吉安",\
"JING JIANG":"北京",\
"KATSURAGII":"绥芬河",\
"LAOHUSHAO":"通化吉安",\
"LAOHUSHAO/JI'AN/QINGSHI":"通化吉安",\
"LAOHUSHAO/QINGSHI":"通化吉安",\
"LIAN YUN GANG":"连云港",\
"Luzhou":"四川泸州",\
"NANSHA ":"广州南沙",\
"NINGBO ":"宁波",\
"PUTIAN XIU YU":"福建莆田秀屿",\
"QINGSHI":"通化吉安",\
"QINGSHI/LAOHUSHAO":"通化吉安",\
"QINZHOU":"广西钦州",\
"QINZHOUNANGUANQINBAO":"广西钦州",\
"QIUGUYEFUKA":"绥芬河",\
"SHANGAHI":"上海",\
"SHANGHAI2225":"上海",\
"SHANGHIA ":"上海",\
"SHENZHEN YANGTIAN":"深圳盐田",\
"TAI CANG":"苏州太仓",\
"TAICANG ":"苏州太仓",\
"TIAN JIN":"天津",\
"YWU":"义乌",\
"ZHAGNJIAGANG":"张家港",\
"ZHAOQING":"肇庆",\
"Zhongshan":"中山",\
"成都":"成都",\
"大连":"大连",\
"广州白云机场":"广州",\
"广州芳村":"广州芳村",\
"黄铺":"广州黄埔",\
"黄埔            ":"广州黄埔",\
"姐告":"云南瑞丽",\
"连云港 LIANYUNGANG":"连云港",\
"南海九江":"广东佛山",\
"瑞丽木姐":"云南瑞丽",\
"三榕港":"肇庆三榕",\
"小勐拉":"勐拉",\
"漳洲":"漳州",\
"张家港 ":"张家港",\
"肇庆":"肇庆",\
"重庆":"重庆",\
"勐满":"勐满",\
"广州花都":"广州花都",\
"窖心港":"广州滘心港",\
"南海三山":"广东佛山",\
"顺德勒流":"佛山勒流",\
"\"MAWEI,FUZHOU\"":"福州",\
}