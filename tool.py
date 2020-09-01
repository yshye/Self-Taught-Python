import os
import datetime


class MdFileModel(object):
    def __init__(self, url: str, name: str):
        """
        初始化
        :param url: 文件路径
        """
        self._url = url
        self._name = name
        self._create_time = os.path.getctime(url)
        self._modify_time = os.path.getmtime(url)

    def create_time(self):
        time = datetime.datetime.fromtimestamp(self._create_time)
        date = time.date()
        return date.strftime('%Y-%m-%d')

    def modify_time(self):
        time = datetime.datetime.fromtimestamp(self._modify_time)
        date = time.date()
        return date.strftime('%Y-%m-%d')

    def __str__(self):
        return {"创建时间": self.create_time(), "修改时间": self.modify_time(), "文件名称": self._name}.__str__()


def create_menu():
    """自动创建菜单"""
    file_list = os.listdir('.')
    readme_file = open('README.MD', 'w', encoding='utf-8')
    stage_list = ['# Self-Taught-Python\n', '> 人生苦短，我选Python；从0-1自学Python！\n', '\n', '## 学习路线\n']
    other_list = ['\n', '## 拓展内容\n']
    for file in file_list:
        if file.find('stage') == 0:
            menu, menu_list = create_item(file)
            if menu is None:
                continue
            stage_list.extend(menu_list)
        elif file.find('z-other') == 0:
            menu, menu_list = create_item(file, short_by_time=True)
            if menu is None:
                continue
            other_list.extend(menu_list)
    for item in stage_list + other_list:
        print(item.replace('\n', ''))
    # for item in other_list:
    #     print(item.replace('\n', ''))

    readme_file.writelines(stage_list + other_list)
    readme_file.close()


def create_other_menu():
    path = f'./z_other'
    file_list = os.listdir(path)
    readme_file = open('./z_other/README.MD', 'w', encoding='utf-8')
    other_list = ['# 拓展内容\n', '> 记录自学过程中的涉及到的其它内容，以及个人的所思所想！\n', '\n', '[<< 返回主目录](../README.MD)\n', '\n']
    m_list = []
    for file in file_list:
        menu, menu_list = create_item(f"z_other/{file}")
        if menu is None:
            continue
        m_list.append(f"  - [{menu}](z_other/{file}/README.MD)\n")
        other_list.extend([item.replace('z_other/', '') for item in menu_list])
    readme_file.writelines(other_list)
    readme_file.close()
    return '拓展内容', m_list


def create_item(file_dir, short_by_time=False):
    """
    更新阶段目录，返回阶段名称
    :param short_by_time: 是否按照修改时间排序
    :param file_dir: 阶段目录
    :return: 阶段名称
    """
    if not os.path.isdir(file_dir):
        return None, None
    doc_path = f'{file_dir}/doc'
    if not os.path.exists(doc_path):
        return None, None
    doc_list = os.listdir(doc_path)
    if short_by_time:
        doc_list = sorted(doc_list, key=lambda _name: os.path.getctime(os.path.join(doc_path, _name)), reverse=True)
    readme_file = open(f'{file_dir}/README.MD', 'r', encoding='utf-8')

    readme_list = readme_file.readlines()[:1]
    readme_list.append('\n')
    readme_list.append('[<< 返回主目录](../README.MD)\n')
    readme_list.append('\n')
    title = readme_list[0].replace('\n', '').replace('# ', '')
    menu = [f"- [{title}]({file_dir}/README.MD)\n"]
    # print(f"- [{title}]({file_dir}/README.MD)")
    for doc in doc_list:
        if doc.endswith('.MD'):
            file_title = doc.replace(".MD", '')
            ctime_long = os.path.getctime(f'{file_dir}/doc/{doc}')
            ctime = datetime.datetime.fromtimestamp(ctime_long)
            mtime_long = os.path.getmtime(f'{file_dir}/doc/{doc}')
            mtime = datetime.datetime.fromtimestamp(mtime_long)
            ntime = datetime.datetime.now()
            file_icon = ''
            if ctime.date() == ntime.date():
                file_icon = ':blue_book:'
            elif mtime.date() >= ntime.date() - datetime.timedelta(days=1):
                file_icon = ':pencil2:'

            # 24小时内
            if short_by_time:
                ttt_str = ctime.strftime('%Y-%m-%d')
                file_title = f"{ttt_str} 《{file_title}》"
            readme_list.append(f"- {file_icon}[{file_title}](doc/{doc})\n")
            menu.append(f"  - {file_icon}[{file_title}]({file_dir}/doc/{doc})\n")
            # print(f"  └ - [{doc.replace('.MD', '')}]({file_dir}/doc/{doc})")
    readme_file.close()
    readme_file = open(f'{file_dir}/README.MD', 'w', encoding='utf-8')
    readme_file.writelines(readme_list)
    readme_file.close()
    return readme_list[0].replace('# ', '').replace('\n', ''), menu


if __name__ == '__main__':
    create_menu()
