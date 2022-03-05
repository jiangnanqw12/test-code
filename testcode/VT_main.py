#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
##主界面函数，将会使用UI.py来实现界面显示。
##创建线程实现事件响应
##


import sys
import os
import time
import traceback

import platform

plfm = platform.platform()

VT_path_abs = os.path.abspath(sys.argv[0])
VT_dir = os.path.split(VT_path_abs)[0]

if 'WINDOWS' in plfm.upper():
    print 'In Windows Platform!'
    lib_name = VT_dir.split('\\')[-1].replace('_vt','_lib')
    lib_dir_parent = os.path.join(VT_dir,'..\..\..\lib\python')
    lib_dir = os.path.join(lib_dir_parent,'{0}'.format(lib_name))
    arg_file_dir = os.path.join(lib_dir,'arg_file')
elif 'LINUX' in plfm.upper():
    print 'In Liunx Platform!'
    lib_name = VT_dir.split('/')[-1].replace('_vt','_lib')
    lib_dir_parent = os.path.join(VT_dir,'../../../lib/python')
    lib_dir = os.path.join(lib_dir_parent,'{0}'.format(lib_name))
    arg_file_dir = os.path.join(lib_dir,'arg_file')


sys.path.append(lib_dir_parent)

exec('from {0} import *'.format(lib_name))

from threading import Thread

from PyQt4 import QtCore, QtGui

logger = log.getLogger()

global g_UI        #UI对象

'''当前选中的接口'''
g_selected_interface=''

'''执行的接口对应的参数xml文件{interface:xml_arg_file_path}'''
xmlarg_filepath_dic={}

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class PGB_COL(object):
    _min=0
    _max=100
    _step=0.0
    @classmethod
    def setRange(clc,_min_,_max_):
        clc._min = _min_
        clc._max = _max_
        clc._step=(clc._max-clc._min)/100.0
        #print 'set range {0},{1},step {2}'.format(clc._min,clc._max,clc._step)
    @classmethod
    def setVal(clc,val):
        g_UI.pgb.setValue(clc._min + int(val*clc._step))
        #print 'set value {0}, PGB value {1}'.format(val,int(g_UI.pgb.value()))
        

class Tree_control(object):
    '''
    把数据显示到界面
    记录每一个节点的行列值，用以赋值的时候可以索引
    '''
    def __init__(self):
        self.elem_dic={}
        self.treedata=[]
        self.elem_map_data={} #{elem,data}
        self.xml_operator = xml_map_ui.Xml_Operator()
        
    def __add_elem(self,row,column,elem):
        tem_dic_column={}
        tem_dic_column[column]=elem
        self.elem_dic[row]=tem_dic_column
        
    def get_elem(self,row,column):
        return self.elem_dic[row][column]
    
    def show_xml_to_tree_ui(self,xml_file_path):
        '''清除保存的数据'''
        self.elem_dic = {}
        self.treedata = []
        self.elem_map_data = {}
        
        '''读取arg_xml文件，设置TreeWdiget界面'''
        g_UI.paramTree.clear()
        self.treedata = self.xml_operator.get_data_tree(xml_file_path)#[[class LeafData],[class LeafData]...]
        '''
        记录距离当前最近的各个层级
        e.g.
        top
            level1
                level2
            level_1
                level_2
                    level3
                    
        tree_node_list=[top,level_1,level_2,level3]        
        '''
        tree_node_list=['']*100
        tree_node_list[0]=g_UI.paramTree

        length = len(self.treedata)
        if length !=0:
            step = 100.0/length
            #print 'step=',step
        
        for row,each in enumerate(self.treedata):
            PGB_COL.setVal(int((row)*step))
            ''' 
            tree title  1,      2,      3,      4
                        name,   type,   inout,  value
            '''
            temitem = QtGui.QTreeWidgetItem(tree_node_list[each.level-1])
            temitem.setText(0,each.name)
            if each.type in ['struct']:
                temitem.setText(1,each.typename)
            elif each.type in ['union']:
                temitem.setText(1,each.typename)
                temitem.setText(2,each.inout)
                temitem.setText(3,each.value)
            elif each.type in ['enum']:
                temitem.setText(1,each.typename)
                temitem.setText(2,each.inout)
                temitem.setText(3,each.value)
            elif each.type in ['arraytype']:
                temitem.setText(1,each.type)
                temitem.setText(3,each.value)
            else:
                temitem.setText(1,each.type)
                temitem.setText(2,each.inout)
                temitem.setText(3,each.value)
                
            tree_node_list[each.level]=temitem
            self.__add_elem(row,each.level,temitem)
            self.elem_map_data[temitem] = each
        PGB_COL.setVal(100)

    def save_tree_ui_to_xml(self,xml_file_path):
        '''保存数据到xml文件'''
        elem_dic_count = len(self.elem_dic.keys())
        logger.debug('elem dic count: {0}'.format(elem_dic_count))
        
        treedata_count = len(self.treedata)
        logger.debug('treedata count:{0}'.format(treedata_count))
        
        g_element_data_count = len(self.xml_operator.g_element_data)
        logger.debug('g_element_data_dout:{0}'.format(g_element_data_count))

        if not elem_dic_count == treedata_count == g_element_data_count:
            print 'verify data ERROR'
            logger.error('verify data ERROR')
        
        PGB_COL.setVal(50)
        if elem_dic_count == treedata_count == g_element_data_count:
            for row,each in enumerate(self.treedata):
                self.treedata[row].value=self.get_elem(row,each.level).text(3)
            for row,each in enumerate(self.treedata):
                if self.xml_operator.g_element_data[row].hasAttribute('value'):
                    self.xml_operator.g_element_data[row].setAttribute('value',each.value)
            self.xml_operator.save_data_tree()
        else:
            logger.error('data checkout failed!')
        PGB_COL.setVal(100)

            
tree_control = Tree_control()

def show_msg(s=''):
    '''设置到输出显示框'''
    g_UI.performButton.setEnabled(True)
    cursor=g_UI.outputEdit.textCursor()
    cursor.insertText(s)
    
def _worker(exe_fun_msg):
    '''
    调用接口执行线程
    '''
    lib_interface.CN_Init()
    result = lib_interface.exe_fun(exe_fun_msg)
    lib_interface.CN_Exit()
    return result
    

class MyThread(Thread):
    '''加入对返回数据的显示'''
    def __init__(self):
        Thread.__init__(self)
        self.param_dic={}
        self.fun_name=''
        self.result=[]
        self.value=-1
        self.temresult=[]
        self.out_result={}
        self.out_prm_str=''

    def setparam(self,param_dic,fun_name):
        '''设置线程参数'''
        self.param_dic=param_dic
        self.fun_name=fun_name

    def setresult(self):
        '''结果写入XML文件，更新界面显示'''
        xml_arg_operator.set_args(str(xmlarg_filepath_dic[g_selected_interface]),self.out_result)
        tree_control.show_xml_to_tree_ui(xmlarg_filepath_dic[g_selected_interface])

        
    #线程执行函数，调用接口并返回数据
    def run(self):
        try:
            fun_exe_msg = lib_interface.FUN_EXE_MSG(g_selected_interface,self.param_dic)
            
            self.temresult=_worker(fun_exe_msg)
            logger.debug('call lib_interface result:')
            logger.debug(str(self.temresult.rtn)+' '+str(self.temresult.in_param_dic)+' '+str(self.temresult.out_param_dic))
            self.out_result = self.temresult.out_param_dic #单个接口执行
            logger.debug(self.out_result)
            
            for each in (self.out_result):
                self.out_prm_str =self.out_prm_str+each+'=self.out_result["'+each+'"],'
            logger.debug(self.out_prm_str)
            
            s='ERROR'
            if self.temresult.rtn == 0:
                s = 'call [ {0}() ] successed!!'.format(self.fun_name)
                self.setresult()
            else:
                result = self.temresult.rtn
                try:
                    result = long(result)
                    result = hex(result)
                except Exception:
                    pass
                s = 'call [ {0}() ] failed,result = [{1}]!!'.format(self.fun_name,self.temresult.rtn)
            show_msg(s)
                
        except Exception,e:
            logger.error(e)
            logger.error(traceback.format_exc())
            show_msg(str(e))


def performButton_action():
    if g_selected_interface!="":
        PGB_COL.setRange(0,40)
        g_UI.outputEdit.clear()
        tree_control.save_tree_ui_to_xml(xmlarg_filepath_dic[g_selected_interface])
        g_UI.saveXmlButton.setEnabled(False)
        '''禁用perform按钮'''
        g_UI.performButton.setEnabled(False)
        PGB_COL.setRange(40,60)
        param_dic = eval(str('xml_arg_operator.get_args(r"'+xmlarg_filepath_dic[g_selected_interface]+'")'))
        PGB_COL.setVal(100)
        PGB_COL.setRange(60,100)
        '''创建并启动线程'''
        thd=MyThread()
        thd.setparam(param_dic,g_selected_interface) 
        thd.start()
        thd.join()
        PGB_COL.setVal(100)
    else:
        print 'select interface first'

def searchEdit_action():
    '''
    实现接口列表搜索功能
    '''
    try:
        for index in range(g_UI.interfaceList.count()):
            if str(g_UI.searchEdit.text()).upper() in str(g_UI.interfaceList.item(index).text()).upper() or len(str(g_UI.searchEdit.text()))==0:
                g_UI.interfaceList.setRowHidden(index,False)
            else:
                g_UI.interfaceList.setRowHidden(index,True)
    except Exception:
        pass

def selectXmlButton_action():
    '''选择一个xml文件，作为当前接口使用的参数文件'''
    if g_selected_interface =="":
        pass
    else:
        filename_full = QtGui.QFileDialog.getOpenFileName(g_UI, 'Open File', os.path.join(lib_dir,'arg_file'), '*{0}*;;XML File (*.xml)'.format(g_selected_interface))
        if filename_full:
            filename_full = str(filename_full)
            g_UI.xmlPathEdit.setText(filename_full)
            PGB_COL.setRange(0,50)
            '''保存界面的内容到xml'''
            tree_control.save_tree_ui_to_xml(xmlarg_filepath_dic[g_selected_interface])
            PGB_COL.setRange(50,100)
            '''载入新的xml到界面'''
            xmlarg_filepath_dic[g_selected_interface]=filename_full
            tree_control.show_xml_to_tree_ui(xmlarg_filepath_dic[g_selected_interface])
            

    #print tree_control.get_elem(1,2).text(3)
    #tree_control.get_elem(2,2).setText(3,'345')
    #print g_UI.paramTree.topLevelItem(1).text(0)
    #tree_control.save_tree_ui_to_xml()


def saveXmlButton_action():
    '''把接口参数的更改保存到xml文件中'''
    tree_control.save_tree_ui_to_xml(xmlarg_filepath_dic[g_selected_interface])
    g_UI.saveXmlButton.setEnabled(False)
    
def interfaceList_select_action(item):
    g_UI.pgb.setValue(0)
    '''接口列表动作'''
    global g_selected_interface
    if g_selected_interface !="":
        PGB_COL.setRange(0,50)
        tree_control.save_tree_ui_to_xml(xmlarg_filepath_dic[g_selected_interface])
        PGB_COL.setRange(50,100)
    else:
        PGB_COL.setRange(0,100)
    g_selected_interface = str(item.text())
    g_UI.xmlPathEdit.setText(xmlarg_filepath_dic[g_selected_interface])
    tree_control.show_xml_to_tree_ui(xmlarg_filepath_dic[g_selected_interface])#要用interfacd：xmlpath 来选择xmlpath
    

class MainWindow(QtGui.QMainWindow,VT.Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.paramTree.setColumnWidth(0,300)
        self.paramTree.setColumnWidth(1,300)

        self.xmlPathEdit.setStyleSheet("background-color:white;")
        
        QtCore.QObject.connect(self.performButton, QtCore.SIGNAL(_fromUtf8("clicked()")), performButton_action)
        QtCore.QObject.connect(self.selectXmlButton, QtCore.SIGNAL(_fromUtf8("clicked()")), selectXmlButton_action)
        QtCore.QObject.connect(self.saveXmlButton, QtCore.SIGNAL(_fromUtf8("clicked()")), saveXmlButton_action)
        QtCore.QObject.connect(self.paramTree, QtCore.SIGNAL(_fromUtf8("itemDoubleClicked(QTreeWidgetItem*,int)")), self.edit_value)
        QtCore.QObject.connect(self.interfaceList, QtCore.SIGNAL(_fromUtf8("currentItemChanged(QListWidgetItem*,QListWidgetItem*)")), interfaceList_select_action)
        QtCore.QObject.connect(self.searchEdit, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), searchEdit_action)
        '''用配置文件初始化接口列表'''
        self.interfaceList.addItems(config.interfaces)
        for each in config.interfaces:
            xmlarg_filepath_dic[each]=os.path.join(arg_file_dir,'{0}.xml'.format(each))
        
        
    def edit_value(self,item,column):
        '''
        双击VALUE列，如符合条件，可以编辑
        enum和union类型弹出下拉框供选择
        '''
        if column==3 and item.text(2) in ['IN','INOUT']:
            source_data = tree_control.elem_map_data[item]
            if source_data.type in ['enum']:
                self.show_enum_menu(source_data.itemList)
            elif source_data.type in ['union']:
                self.show_union_menu(source_data.itemList)
            else:
                item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            g_UI.saveXmlButton.setEnabled(True)
        else:
            item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)

    def _enum_menu_select_action(self,item):
        '''枚举项的选择设置'''
        s = str(item.text())
        val = s.split('_')[-1].replace('[','').replace(']','')
        self.paramTree.currentItem().setText(3,val)
    
    def show_enum_menu(self,items):
        '''菜单 枚举列表'''
        popMenu = QtGui.QMenu()
        popMenu.triggered.connect(self._enum_menu_select_action)
        for each in items:
            popMenu.addAction(QtGui.QAction(each,self))
        popMenu.exec_(QtGui.QCursor.pos())

    def _union_menu_select_action(self,item):
        '''联合体成员的选择设置'''
        s = str(item.text())
        self.paramTree.currentItem().setText(3,s)

    def show_union_menu(self,items):
        '''菜单 联合体成员列表'''
        popMenu = QtGui.QMenu()
        popMenu.triggered.connect(self._union_menu_select_action)
        for each in items:
            popMenu.addAction(QtGui.QAction(each,self))
        popMenu.exec_(QtGui.QCursor.pos())
            
if __name__ == "__main__":
    global g_UI
    app = QtGui.QApplication(sys.argv)
    g_UI= MainWindow()
    g_UI.show()
    
    try:
        sys.exit(app.exec_())
    except:
        pass
    
