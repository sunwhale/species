# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 14:48:30 2016

@author: sunwhale
"""

DataToLatin = {'Aquilaria  crassna':'Aquilaria crassna',\
'Aquilaria  filaria':'Aquilaria filaria',\
'Aquilaria  malaccensis':'Aquilaria malaccensis',\
'Aquilaria  spp.':'Aquilaria spp.',\
'Aquilaria crassna':'Aquilaria crassna',\
'Aquilaria filaria':'Aquilaria filaria',\
'Bulnesia sarmientoi':'Bulnesia sarmientoi',\
'Caesalpinia aceae':'Caesalpinia aceae',\
'Caesalpinia echinata':'Caesalpinia echinata',\
'Caesalpinia sappan':'Caesalpinia sappan',\
'Caesalpinia siamea':'Caesalpinia siamea',\
'Caesalpinis sappan':'Caesalpinis sappan',\
'Casealpinia echinata':'Casealpinia echinata',\
'Cassia  siamea':'Cassia siamea',\
'Cassia Siamea':'Cassia siamea',\
'Cassia Siamea Lam':'Cassia siamea',\
'Cassia siamea':'Cassia siamea',\
'Cassia siamea Lam':'Cassia siamea',\
'Cassia siames':'Cassia siamea',\
'Cassla sianea':'Cassia siamea',\
'Cedrela odorata':'Cedrela odorata',\
'Dalbergia  fusca':'Dalbergia fusca',\
'Dalbergia  latifolia':'Dalbergia latifolia',\
'Dalbergia  odorifera':'Dalbergia odorifera',\
'Dalbergia  oliveri':'Dalbergia oliveri',\
'Dalbergia  retusa':'Dalbergia retusa',\
'Dalbergia  spp.':'Dalbergia spp.',\
'Dalbergia Bariensis':'Dalbergia bariensis',\
'Dalbergia Cochinchinensis':'Dalbergia cochinchinensis',\
'Dalbergia Latifolia':'Dalbergia latifolia',\
'Dalbergia aliveri':'Dalbergia oliveri',\
'Dalbergia aliveri Gamble':'Dalbergia oliveri',\
'Dalbergia bariensis':'Dalbergia bariensis',\
'Dalbergia bariensis Pierre':'Dalbergia bariensis',\
'Dalbergia baronii':'Dalbergia baronii',\
'Dalbergia cearensis':'Dalbergia cearensis',\
'Dalbergia cochichinensis':'Dalbergia cochinchinensis',\
'Dalbergia cochinchinensis':'Dalbergia cochinchinensis',\
'Dalbergia cochinchinensis ':'Dalbergia cochinchinensis',\
'Dalbergia cochinchinensis *':'Dalbergia cochinchinensis',\
'Dalbergia cultrata':'Dalbergia cultrata',\
'Dalbergia frutescens':'Dalbergia frutescens var.tomentosa',\
'Dalbergia frutescens ':'Dalbergia frutescens var.tomentosa',\
'Dalbergia frutescens var.tomentosa':'Dalbergia frutescens var.tomentosa',\
'Dalbergia fusca':'Dalbergia fusca',\
'Dalbergia granadillo':'Dalbergia granadillo',\
'Dalbergia greveana':'Dalbergia greveana',\
'Dalbergia latifolia':'Dalbergia latifolia',\
'Dalbergia melanoxylon':'Dalbergia melanoxylon',\
'Dalbergia  nigra':'Dalbergia nigra',\
'Dalbergia odorifera':'Dalbergia odorifera',\
'Dalbergia oliver':'Dalbergia oliveri',\
'Dalbergia oliveri':'Dalbergia oliveri',\
'Dalbergia oliveri Gamble':'Dalbergia oliveri',\
'Dalbergia retusa':'Dalbergia retusa',\
'Dalbergia spruceana':'Dalbergia spruceana',\
'Dalbergia stevensonii':'Dalbergia stevensonii',\
'Dalbergia tucurensis':'Dalbergia tucurensis',\
'Dalbergia  tucurensis':'Dalbergia tucurensis',\
'Diospyros celebica':'Diospyros celebica',\
'Diospyros celebica*':'Diospyros celebica',\
'Diospyros celehica':'Diospyros celebica',\
'Diospyros crassiflora':'Diospyros crassiflora',\
'Diospyros crassiflora hiern':'Diospyros crassiflora',\
'Diospyros crassiflorides':'Diospyros crassiflora',\
'Diospyros crassiflova':'Diospyros crassiflora',\
'Diospyros crossiflora':'Diospyros crassiflora',\
'Diospyros ebenum':'Diospyros ebenum',\
'Diospyros philippensis':'Diospyros philippensis',\
'Diospyros philippinensis':'Diospyros philippensis',\
'Diospyros pilosanthera':'Diospyros pilosanthera',\
'Ebenaceae spp.':'Ebenaceae spp.',\
'Fraxinus  mandshurica':'Fraxinus mandshurica',\
'Fraxinus mandshurica':'Fraxinus mandshurica',\
'Guaiacum  sanctum':'Guaiacum sanctum',\
'Mesua  ferrea':'Mesua ferrea',\
'Mille tia leucan tha':'Millettia leucantha',\
'Milleia leucantha':'Millettia leucantha',\
'Milletia laurentii':'Millettia leucantha',\
'Milletia leucantha':'Millettia leucantha',\
'Millettia Leucantha':'Millettia leucantha',\
'Millettia ieucantha':'Millettia leucantha',\
'Millettia laurentii':'Millettia laurentii',\
'Millettia laurentii*':'Millettia laurentii',\
'Millettia leucantha':'Millettia leucantha',\
'Millettia pendula':'Millettia leucantha',\
'PERICOPSIS ELATA':'Pericopsis elata',\
'Pericopsis  elata':'Pericopsis elata',\
'Pericopsis elata':'Pericopsis elata',\
'Pinus  koraiensis':'Pinus koraiensis',\
'Pinus koraiensis':'Pinus koraiensis',\
'Platymiscium pleiostachyum':'Platymiscium pleiostachyum',\
'Prunus  africana':'Prunus africana',\
'Pterocarpus  indicus':'Pterocarpus indicus',\
'Pterocarpus  santalinus':'Pterocarpus santalinus',\
'Pterocarpus Pedatus':'Pterocarpus pedatus',\
'Pterocarpus barisnsis':'Dalbergia bariensis',\
'Pterocarpus barisnsis（拉丁名应为Dalbergia bariensis）':'Dalbergia bariensis',\
'Pterocarpus cambodianus':'Pterocarpus cambodianus',\
'Pterocarpus cambodianus pierre':'Pterocarpus cambodianus',\
' Pterocarpus erinaceus':'Pterocarpus erinaceus',\
'Pterocarpus erinaceus':'Pterocarpus erinaceus',\
'Pterocarpus indicus':'Pterocarpus indicus',\
'Pterocarpus macarocarpus':'Pterocarpus macarocarpus',\
'Pterocarpus macrocarpus':'Pterocarpus macarocarpus',\
'Pterocarpus macrocarpus ':'Pterocarpus macarocarpus',\
'Pterocarpus macrocarpus Kurz':'Pterocarpus macarocarpus',\
'Pterocarpus macrocarpus*':'Pterocarpus macarocarpus',\
'Pterocarpus marsupium':'Pterocarpus marsupium',\
'Pterocarpus pedatus':'Pterocarpus pedatus',\
'Pterocarpus pedatus ':'Pterocarpus pedatus',\
'Pterocarpus pedatus pierre':'Pterocarpus pedatus',\
'Quercus  mongolica':'Quercus mongolica',\
'Senna siamea（此为商品名）':'Cassia siamea',\
'Swietenia  macrophylla':'Swietenia macrophylla',\
'Swietenia  mahagoni':'Swietenia mahagoni',\
'Swietenia Macrophylla':'Swietenia macrophylla',\
'Swietenia macrophylla':'Swietenia macrophylla',\
'Swietenia mahagoni':'Swietenia mahagoni',\
'Swietenia mahagoni ':'Swietenia mahagoni',\
'Taxus chinensis':'Taxus chinensis',\
'Taxus  wallichiana':'Taxus wallichiana',\
'Taxus cuspidata':'Taxus cuspidata',\
'Taxus x media':'Taxus x media',\
'Taxus sumatrana':'Taxus sumatrana',\
'dalbergia bariensis':'Dalbergia bariensis',\
'dalbergia latifolia':'Dalbergia latifolia',\
'pterocarpus erinaceus':'Pterocarpus erinaceus',\
'pterocarpus indicus':'Pterocarpus indicus',\
'pterocarpus macrocarpus':'Pterocarpus macarocarpus',\
'Casealpinia echinata':'Casealpinia echinata',\
'undefined':'Undefined',\
}

LatinToChinese = {
'Aquilaria crassna':'沉香',\
'Aquilaria filaria':'丝虫沉香',\
'Aquilaria malaccensis':'沉香',\
'Aquilaria spp.':'沉香',\
'Bulnesia sarmientoi':'南美蒺藜木',\
'Caesalpinia aceae':'铁刀木',\
'Caesalpinia echinata':'巴西苏木',\
'Caesalpinia sappan':'铁刀木',\
'Caesalpinia siamea':'铁刀木',\
'Caesalpinis sappan':'铁刀木',\
'Cassia siamea':'铁刀木',\
'Cedrela odorata':'香洋椿',\
'Dalbergia fusca':'黑黄檀',\
'Dalbergia latifolia':'阔叶黄檀',\
'Dalbergia odorifera':'降香黄檀',\
'Dalbergia oliveri':'奥氏黄檀',\
'Dalbergia retusa':'微凹黄檀',\
'Dalbergia spp.':'黄檀',\
'Dalbergia bariensis':'巴里黄檀',\
'Dalbergia cochinchinensis':'交趾黄檀',\
'Dalbergia baronii':'巴罗尼黄檀',\
'Dalbergia cearensis':'赛州黄檀',\
'Dalbergia cultrata':'刀状黑黄檀',\
'Dalbergia frutescens var.tomentosa':'绒毛黄檀',\
'Dalbergia granadillo':'中美洲黄檀',\
'Dalbergia greveana':'格雷夫黄檀',\
'Dalbergia melanoxylon':'东非黑黄檀',\
'Dalbergia nigra':'巴西黑黄檀',\
'Dalbergia spruceana':'亚马孙黄檀',\
'Dalbergia stevensonii':'伯利兹黄檀',\
'Dalbergia tucurensis':'危地马拉黄檀',\
'Diospyros celebica':'苏拉威西乌木',\
'Diospyros crassiflora':'厚瓣乌木',\
'Diospyros ebenum':'乌木',\
'Diospyros philippensis':'菲律宾乌木',\
'Diospyros pilosanthera':'毛药乌木',\
'Ebenaceae spp.':'黑檀',\
'Fraxinus mandshurica':'水曲柳',\
'Guaiacum sanctum':'神圣愈疮木',\
'Mesua ferrea':'铁力木',\
'Millettia leucantha':'白花崖豆木',\
'Millettia laurentii':'非洲崖豆木',\
'Pericopsis elata':'大美木豆',\
'Pinus koraiensis':'红松',\
'Platymiscium pleiostachyum':'膜荚豆',\
'Prunus africana':'非洲李',\
'Pterocarpus indicus':'印度紫檀',\
'Pterocarpus santalinus':'檀香紫檀',\
'Pterocarpus pedatus':'鸟足紫檀',\
'Pterocarpus cambodianus':'越柬紫檀',\
'Pterocarpus erinaceus':'刺猬紫檀',\
'Pterocarpus macarocarpus':'大果紫檀',\
'Pterocarpus marsupium':'囊状紫檀',\
'Quercus mongolica':'柞木',\
'Swietenia macrophylla':'大叶桃花心木',\
'Swietenia mahagoni':'桃花心木',\
'Taxus chinensis':'红豆杉',\
'Taxus wallichiana':'喜马拉雅红豆杉',\
'Taxus cuspidata':'东北红豆杉',\
'Taxus x media':'曼地亚红豆杉',\
'Taxus sumatrana':'苏门答腊红豆杉',\
'Undefined':'',\
}

Latin = [
'Aquilaria crassna',
'Aquilaria filaria',
'Aquilaria malaccensis',
'Aquilaria spp.',
'Bulnesia sarmientoi',
'Caesalpinia aceae',
'Caesalpinia echinata',
'Caesalpinia sappan',
'Caesalpinia siamea',
'Caesalpinis sappan',
'Cassia siamea',
'Cedrela odorata',
'Dalbergia fusca',
'Dalbergia latifolia',
'Dalbergia odorifera',
'Dalbergia oliveri',
'Dalbergia retusa',
'Dalbergia spp.',
'Dalbergia bariensis',
'Dalbergia cochinchinensis',
'Dalbergia baronii',
'Dalbergia cearensis',
'Dalbergia cultrata',
'Dalbergia frutescens var.tomentosa',
'Dalbergia granadillo',
'Dalbergia greveana',
'Dalbergia melanoxylon',
'Dalbergia nigra',
'Dalbergia spruceana',
'Dalbergia stevensonii',
'Dalbergia tucurensis',
'Diospyros celebica',
'Diospyros crassiflora',
'Diospyros ebenum',
'Diospyros philippensis',
'Diospyros pilosanthera',
'Ebenaceae spp.',
'Fraxinus mandshurica',
'Guaiacum sanctum',
'Mesua ferrea',
'Millettia leucantha',
'Millettia laurentii',
'Pericopsis elata',
'Pinus koraiensis',
'Platymiscium pleiostachyum',
'Prunus africana',
'Pterocarpus indicus',
'Pterocarpus santalinus',
'Pterocarpus pedatus',
'Pterocarpus cambodianus',
'Pterocarpus erinaceus',
'Pterocarpus macarocarpus',
'Pterocarpus marsupium',
'Quercus mongolica',
'Swietenia macrophylla',
'Swietenia mahagoni',
'Taxus chinensis',
'Taxus cuspidata',
'Taxus sumatrana',
'Taxus wallichiana',
'Taxus x media',
'Undefined',
]

Hongmu=[
'Dalbergia granadillo',
'Pterocarpus cambodianus',
'Pterocarpus indicus',
'Dalbergia spruceana',
'Diospyros ebenum',
'Dalbergia retusa',
'Caesalpinia aceae',
'Caesalpinia sappan',
'Caesalpinia siamea',
'Caesalpinis sappan',
'Cassia siamea',
'Pterocarpus santalinus',
'Diospyros celebica',
'Dalbergia cearensis',
'Dalbergia frutescens var.tomentosa',
'Pterocarpus pedatus',
'Pterocarpus marsupium',
'Diospyros pilosanthera',
'Dalbergia latifolia',
'Dalbergia cochinchinensis',
'Dalbergia odorifera',
'Dalbergia spp.',
'Diospyros crassiflora',
'Dalbergia fusca',
'Diospyros philippensis',
'Millettia laurentii',
'Dalbergia melanoxylon',
'Dalbergia cultrata',
'Pterocarpus macarocarpus',
'Pterocarpus erinaceus',
'Dalbergia stevensonii',
'Millettia leucantha',
'Dalbergia bariensis',
'Dalbergia oliveri',
'Dalbergia nigra',
]

Zhenxi=[
'Dalbergia granadillo',
'Quercus mongolica',
'Cedrela odorata',
'Taxus wallichiana',
'Dalbergia retusa',
'Dalbergia tucurensis',
'Swietenia mahagoni',
'Pterocarpus santalinus',
'Aquilaria filaria',
'Fraxinus mandshurica',
'Guaiacum sanctum',
'Bulnesia sarmientoi',
'Platymiscium pleiostachyum',
'Dalbergia cochinchinensis',
'Pinus koraiensis',
'Millettia leucantha',
'Dalbergia greveana',
'Prunus africana',
'Taxus cuspidata',
'Swietenia macrophylla',
'Pericopsis elata',
'Aquilaria crassna',
'Aquilaria malaccensis',
'Aquilaria spp.',
'Caesalpinia echinata',
'Casealpinia echinata',
'Taxus chinensis',
'Dalbergia nigra',
'Taxus sumatrana',
]

density={
"Aquilaria crassna":0.4,\
"Aquilaria filaria":0.4,\
"Aquilaria malaccensis":0.4,\
"Aquilaria spp.":0.4,\
"Bulnesia sarmientoi":1.05,\
"Caesalpinia echinata":1.2,\
"Caesalpinia aceae":0.82,\
"Caesalpinia sappan":0.82,\
"Caesalpinia siamea":0.82,\
"Caesalpinis sappan":0.82,\
"Cassia siamea":0.82,\
"Cedrela odorata":0.47,\
"Dalbergia bariensis":1.08,\
"Dalbergia baronii":0.83,\
"Dalbergia cearensis":1.2,\
"Dalbergia cochinchinensis":1.05,\
"Dalbergia cultrata":1.52,\
"Dalbergia frutescens var.tomentosa":1.0,\
"Dalbergia fusca":1.12,\
"Dalbergia granadillo":1.1,\
"Dalbergia greveana":1.2,\
"Dalbergia latifolia":0.84,\
"Dalbergia melanoxylon":1.17,\
"Dalbergia nigra":0.94,\
"Dalbergia odorifera":0.88,\
"Dalbergia oliveri":1.0,\
"Dalbergia retusa":1.1,\
"Dalbergia spp.":0.8,\
"Dalbergia spruceana":0.9,\
"Dalbergia stevensonii":1.06,\
"Dalbergia tucurensis":1.03,\
"Diospyros celebica":1.09,\
"Diospyros crassiflora":1.05,\
"Diospyros ebenum":1.01,\
"Diospyros philippensis":0.94,\
"Diospyros pilosanthera":0.94,\
"Fraxinus mandshurica":0.66,\
"Guaiacum sanctum":1.3,\
"Millettia laurentii":0.8,\
"Millettia leucantha":1.02,\
"Pericopsis elata":0.69,\
"Pinus koraiensis":0.44,\
"Platymiscium pleiostachyum":0.95,\
"Prunus africana":0.6,\
"Pterocarpus cambodianus":0.98,\
"Pterocarpus erinaceus":0.85,\
"Pterocarpus indicus":0.74,\
"Pterocarpus macarocarpus":0.83,\
"Pterocarpus marsupium":0.78,\
"Pterocarpus pedatus":0.99,\
"Pterocarpus santalinus":1.16,\
"Quercus mongolica":0.76,\
"Swietenia macrophylla":0.62,\
"Swietenia mahagoni":0.74,\
"Taxus cuspidata":0.55,\
"Taxus chinensis":0.69,\
"Taxus sumatrana":0.67,\
"Taxus wallichiana":0.66,\
"Taxus x media":0.65,\
"Mesua ferrea":1.05,\
"Ebenaceae spp.":0.85,\
"Undefined":0.88,\
}