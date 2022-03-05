#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os


import platform

plfm = platform.platform()

script_path_abs = os.path.abspath(sys.argv[0])
script_dir = os.path.split(script_path_abs)[0]

if 'WINDOWS' in plfm.upper():
    print 'In Windows Platform!'
    lib_name = script_dir.split('\\')[-1].replace('_vt','_lib')
    lib_dir_parent = os.path.join(script_dir,'..\..\..\lib\python')
    lib_dir = os.path.join(lib_dir_parent,'{0}'.format(lib_name))
    arg_file_dir = os.path.join(lib_dir,'arg_file')
elif 'LINUX' in plfm.upper():
    print 'In Liunx Platform!'
    lib_name = script_dir.split('/')[-1].replace('_vt','_lib')
    lib_dir_parent = os.path.join(script_dir,'../../../lib/python')
    lib_dir = os.path.join(lib_dir_parent,'{0}'.format(lib_name))
    arg_file_dir = os.path.join(lib_dir,'arg_file')
    
sys.path.append(lib_dir)

import lib_interface
import xml_arg_operator

#------------------------以上内容，不必修改------------------------------------------

'''
xml参数文件放在VT/lib/python/arg_file/文件夹下，可以省略路径和后缀
'''


xml_file_name_list = ['SA4A_request_dynamic_exposure_part(10_1).xml',
             'SA4A_request_dynamic_exposure_part(10_2).xml',]
             #'SA4A_request_dynamic_exposure_part(10_2_against).xml']  #参数文件路径

path_list=[]
for each in xml_file_name_list:
    path_list.append(os.path.join(arg_file_dir,each))



'''读xml获取参数'''
print '\n******get param to fun[0]******'
param_10_1 = xml_arg_operator.get_args(path_list[0])
print '\n******get param to fun[1]******'
param_10_2 = xml_arg_operator.get_args(path_list[1])
#param_10_against = xml_arg_operator.get_args(path_list[2])

'''创建执行对象'''
fun1 = lib_interface.FUN_EXE_MSG('SA4A_request_dynamic_exposure',param_10_1)
fun2 = lib_interface.FUN_EXE_MSG('SA4A_request_dynamic_exposure',param_10_2)
#fun3 = lib_interface.FUN_EXE_MSG('SA4A_request_dynamic_exposure',param_10_against)

'''加入列表中'''
exe_list=[]
exe_list.append(fun1)
exe_list.append(fun2)
#exe_list.append(fun3)

'''执行列表中的接口'''
lib_interface.CN_Init()  #初始化CN通信

result = []
for i,each in enumerate(exe_list):
    print '\n******start  exec fun [{0}]******\n'.format(i),each.name
    result.append(lib_interface.exe_fun(each))   #执行，并将结果记录到result

lib_interface.CN_Exit()  #终止CN通信


'''处理结果'''
print '\n******output result******'
for i,each in enumerate(result):
    print '\n',each.rtn,each.in_param_dic,each.out_param_dic
    if each.rtn == 0:
        xml_arg_operator.set_args(path_list[i],each.out_param_dic)  #保存结果到xml文件
print '\n******END******\n'





        
