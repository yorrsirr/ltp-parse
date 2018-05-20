# -*- coding:utf-8 -*-

import os
from pyltp import Segmentor
from pyltp import Postagger
from pyltp import Parser

LTP_DATA_DIR = '/home/yorrsirr/下载/ltp_data'  # ltp模型目录的路径
par_model_path = os.path.join(LTP_DATA_DIR, 'parser.model')  # 依存句法分析模型路径，模型名称为`parser.model`

def seg(sentenses):
    cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model') #分词模型路径，模型名称为`cws.model`
    segmentor = Segmentor()
    segmentor.load(cws_model_path)
    words = segmentor.segment(sentenses)
    segmentor.release()
    return words

def pos(sentences):
    pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')
    postagger = Postagger()
    postagger.load(pos_model_path)
    postags = postagger.postag(seg(sentences))
    return postags

def par(sentences):
    par_model_path = os.path.join(LTP_DATA_DIR, 'parser.model')
    parser = Parser()
    parser.load(par_model_path)
    parsers = parser.parse(seg(sentences), pos(sentences))
    parser.release()
    return parsers

# sentences = '生活就像海洋，只有意志坚定的人，才能到达彼岸'
#
# print "\t".join(seg(sentences))
# print '\t'.join(pos(sentences))
# print "\t".join("%d:%s" % (arc.head, arc.relation) for arc in par(sentences))
