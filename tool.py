import os


def create_menu():
    """自动创建菜单"""
    file_list = os.listdir('.')
    readme_file = open('README.MD', 'w', encoding='utf-8')
    readme_list = ['# Self-Taught-Python\n', '> 人生苦短，我选Python;从0-1自学Python。\n\n']
    for file in file_list:
        if file.find('stage') == 0:
            menu = create_item(file)
            readme_list.append(f"- [{menu}]({file}/README.MD)\n")
    print(readme_list)
    readme_file.writelines(readme_list)
    readme_file.close()


def create_item(file_dir):
    """
    更新阶段目录，返回阶段名称
    :param file_dir: 阶段目录
    :return: 阶段名称
    """
    doc_list = os.listdir(f'{file_dir}/doc')
    readme_file = open(f'{file_dir}/README.MD', 'r', encoding='utf-8')
    readme_list = readme_file.readlines()[:1]
    readme_list.append('\n')
    for doc in doc_list:
        readme_list.append(f"- [{doc.replace('.MD', '')}](doc/{doc})\n")
        print(f"- [{doc.replace('.MD', '')}](doc/{doc})")
    readme_list.append('\n\n- [返回主菜单](../README.MD)')
    readme_file.close()
    readme_file = open(f'{file_dir}/README.MD', 'w', encoding='utf-8')
    readme_file.writelines(readme_list)
    readme_file.close()
    return readme_list[0].replace('# ', '').replace('\n', '')


if __name__ == '__main__':
    create_menu()
