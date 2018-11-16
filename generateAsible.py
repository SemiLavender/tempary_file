from os import mkdir


def genDirStructure(path='\.', name='demo'):
    '''
    生成正式的ansible inventory模版
    :param path: 需要生成ansible项目的路径，此路径必须存在
    :param name: 项目的名字
    :return:
    '''

    local_path = path.replace('\\', '/')+'\\'+name
    demo_dict = {
        'filter_plugins': 1,  # 自定义 filter 插件存放目录
        'fooapp': 1,  # Fooapp 片色目录 ( 与 common 角色目录平级)
        'group_vars': 1,  # 自定义组变量文件
        'host_vars': 1,  # 自定义全局变量文件
        'library': 1,  # 自定义模块存放目录
        'monitoring': 1,  # Monitoring 角色目录 ( 与 common 角色目录平级)
        'roles': 1,  # Role 存放目录
        'site.yml': 0,  # Playbook 统一入口文件
        'stage': 0,  # stage 环境的 inventory 文件
        'webservers.yml': 0,  # 特殊的playbook文件
        'webtier': 1  # webtier 角色目录 ( 与 common 角色目录平级)
    }
    mkdir(local_path)
    for k, v in demo_dict.items():
        if v == 0:
            f = open(local_path+'\\'+k, "w+")
            f.write("# This is a demo")
            f.close()
        else:
            mkdir(local_path+'\\'+k)

def genRolesModule(name='demo'):
    '''
    生成roles模块
    :param name: roles的名字
    :return: null
    '''
    path = ''

