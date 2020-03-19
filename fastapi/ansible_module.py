# 版权许可
# !/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# 模块信息
ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

# metadata_version是ANSIBLE_METADATA模式的版本，而不是模块的版本。
# 升级模块status或supported_by状态只能由Ansible核心团队的成员来完成。


# 文档描述
DOCUMENTATION = '''
---
module: backup
short_description: get backup_version from /usr/local/{{ project }}/.version
version_added: "2.4"
author: lin.jiang
'''

# 使用举例
EXAMPLES = '''
- name: get last version from .version
  backup: role={{ project }} version={{ app_version }}-{{ conf_hash }}
'''

# 运行流程
from ansible.module_utils.basic import AnsibleModule

# 1. 传入的格式，ansible有自己的传入模式，传入的格式为json的形式

class BaseModule(object):
    # 设置默认参数
    def __init__(self,module):
        self.module = module
        self.prefix = self.module.parmas['prefix']

    def run_module():
    # 设置默认参数列表
        module_args = dict(
        name=dict(type='str', required=True),
        new=dict(type='bool', required=False, default=False)
    )


    # 返回结果
    result = dict(
        changed=False,
        original_message='',
        message=''
    )

    # 如果参数检测通过，则返回结果
    # if module.check_mode:
    #     return result

    # 对输入的参数进行操作
    # if module.params['name'] == 'fail me':
    #   module.fail_json(msg='You requested this to fail', **result)

    # 返回内容
    # module.exit_json(**result)


# 使用
def main():

    # 初始化json
    module_ages = dict(
        prefix_path = dict(
            type = 'str',default='usr/local'),
        role = dict(
            type = 'str',require=True),
        version = dict(
            type = 'str', require=True),
         update = dict(
            type = 'bool', require=True),
        replace = dict(
            type = 'bool', default=False),
    )
    # 参数检测
    module = AnsibleModule(argument_spec=module_ages,supports_check_mode=True)
    print(module)
    factor = BaseModule(module)


if __name__ == '__main__':
    main()