# -*- coding: gbk -*-
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
'Dalbergia cultrata':'Dalbergia cultrata',\
'Dalbergia frutescens':'Dalbergia frutescens var.tomentosa',\
'Dalbergia frutescens ':'Dalbergia frutescens var.tomentosa',\
'Dalbergia frutescens var.tomentosa':'Dalbergia frutescens var.tomentosa',\
'Dalbergia fusca':'Dalbergia fusca',\
'Dalbergia granadillo':'Dalbergia granadillo',\
'Dalbergia greveana':'Dalbergia greveana',\
'Dalbergia latifolia':'Dalbergia latifolia',\
'Dalbergia melanoxylon':'Dalbergia melanoxylon',\
'Dalbergia odorifera':'Dalbergia odorifera',\
'Dalbergia oliver':'Dalbergia oliveri',\
'Dalbergia oliveri':'Dalbergia oliveri',\
'Dalbergia oliveri Gamble':'Dalbergia oliveri',\
'Dalbergia retusa':'Dalbergia retusa',\
'Dalbergia spruceana':'Dalbergia spruceana',\
'Dalbergia stevensonii':'Dalbergia stevensonii',\
'Dalbergia tucurensis':'Dalbergia tucurensis',\
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
'Pterocarpus barisnsis��������ӦΪDalbergia bariensis��':'Dalbergia bariensis',\
'Pterocarpus cambodianus':'Pterocarpus cambodianus',\
'Pterocarpus cambodianus pierre':'Pterocarpus cambodianus',\
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
'Senna siamea����Ϊ��Ʒ����':'Cassia siamea',\
'Swietenia  macrophylla':'Swietenia macrophylla',\
'Swietenia  mahagoni':'Swietenia mahagoni',\
'Swietenia Macrophylla':'Swietenia macrophylla',\
'Swietenia macrophylla':'Swietenia macrophylla',\
'Swietenia mahagoni':'Swietenia mahagoni',\
'Swietenia mahagoni ':'Swietenia mahagoni',\
'Taxus  wallichiana':'Taxus wallichiana',\
'Taxus cuspidata':'Taxus cuspidata',\
'Taxus x media':'Taxus x media',\
'dalbergia bariensis':'Dalbergia bariensis',\
'dalbergia latifolia':'Dalbergia latifolia',\
'pterocarpus erinaceus':'Pterocarpus erinaceus',\
'pterocarpus indicus':'Pterocarpus indicus',\
'pterocarpus macrocarpus':'Pterocarpus macarocarpus',\
'undefined':'Undefined',\
}

LatinToChinese = {'Aquilaria crassna':'����',\
'Aquilaria filaria':'˿�����',\
'Aquilaria malaccensis':'����',\
'Aquilaria spp.':'����',\
'Bulnesia sarmientoi':'������޼ľ',\
'Caesalpinia aceae':'����ľ',\
'Caesalpinia echinata':'������ľ',\
'Caesalpinia sappan':'����ľ',\
'Caesalpinia siamea':'����ľ',\
'Caesalpinis sappan':'����ľ',\
'Casealpinia echinata':'������ľ',\
'Cassia siamea':'����ľ',\
'Cedrela odorata':'����',\
'Dalbergia fusca':'�ڻ�̴',\
'Dalbergia latifolia':'��Ҷ��̴',\
'Dalbergia odorifera':'�����̴',\
'Dalbergia oliveri':'���ϻ�̴',\
'Dalbergia retusa':'΢����̴',\
'Dalbergia spp.':'��̴',\
'Dalbergia bariensis':'�����̴',\
'Dalbergia cochinchinensis':'��ֺ��̴',\
'Dalbergia baronii':'�������̴',\
'Dalbergia cearensis':'���ݻ�̴',\
'Dalbergia cultrata':'��״�ڻ�̴',\
'Dalbergia frutescens var.tomentosa':'��ë��̴',\
'Dalbergia granadillo':'�����޻�̴',\
'Dalbergia greveana':'���׷��̴',\
'Dalbergia melanoxylon':'���Ǻڻ�̴',\
'Dalbergia spruceana':'�������̴',\
'Dalbergia stevensonii':'�����Ȼ�̴',\
'Dalbergia tucurensis':'Σ��������̴',\
'Diospyros celebica':'����������ľ',\
'Diospyros crassiflora':'�����ľ',\
'Diospyros ebenum':'��ľ',\
'Diospyros philippensis':'���ɱ���ľ',\
'Diospyros pilosanthera':'ëҩ��ľ',\
'Ebenaceae spp.':'��̴',\
'Fraxinus mandshurica':'ˮ����',\
'Guaiacum sanctum':'��ʥ����ľ',\
'Mesua ferrea':'����ľ',\
'Millettia leucantha':'�׻��¶�ľ',\
'Millettia laurentii':'�����¶�ľ',\
'Millettia leucantha':'���¶�ľ',\
'Pericopsis elata':'����ľ��',\
'Pinus koraiensis':'����',\
'Platymiscium pleiostachyum':'Ĥ�Զ�',\
'Prunus africana':'������',\
'Pterocarpus indicus':'ӡ����̴',\
'Pterocarpus santalinus':'̴����̴',\
'Pterocarpus pedatus':'������̴',\
'Pterocarpus cambodianus':'Խ����̴',\
'Pterocarpus erinaceus':'�����̴',\
'Pterocarpus macarocarpus':'�����̴',\
'Pterocarpus marsupium':'��״��̴',\
'Quercus mongolica':'��ľ',\
'Swietenia macrophylla':'��Ҷ�һ���ľ',\
'Swietenia mahagoni':'�һ���ľ',\
'Taxus wallichiana':'ϲ�����ź춹ɼ',\
'Taxus cuspidata':'�����춹ɼ',\
'Taxus x media':'�����Ǻ춹ɼ',\
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
'Casealpinia echinata',
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
'Taxus wallichiana',
'Taxus cuspidata',
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
]