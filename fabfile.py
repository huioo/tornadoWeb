#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

from fabric.api import env, run, task, execute, sudo
from fabric.context_managers import cd, settings, hide
from fabric.decorators import roles, hosts
from fabric.tasks import Task
from fabric.colors import red, green

env.roledefs = {
    'python': ['heiniu@47.92.93.236'],
    'nginx': ['heiniu@47.92.145.34'],
    'piwik': ['heiniu@47.92.104.74'],
    'laituia': ['heiniu@47.92.52.151'],
    'redis': ['heiniu@47.92.101.15', 'heiniu@47.92.142.121'],
}
env.passwords = {
    'root@121.40.176.186:22': 'Y&3wdgLq-+m3',
    'heiniu@47.92.104.74:22': 'Heiniu@89bc524f@#$',
    'heiniu@47.92.93.236:22': 'Heiniu@89bc524f@#$',
    'heiniu@47.92.145.34:22': 'Heiniu@89bc524f@#$',
    'heiniu@47.92.52.151:22': 'Heiniu@89bc524f@#$',
    'heiniu@47.92.101.15:22': 'heiniu@redis@master',
    'heiniu@47.92.142.121:22': 'heiniu@redis@slave',
    'root@47.92.142.121': 'root Heiniu@3724718f@#$',
}

STORAGE_ROLES = ['python', 'nginx', 'piwik', 'laituia', 'redis']


class MyFabricUtils(object):
    @staticmethod
    def info(msg):
        out_msg = '[{}] {}\n'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), msg)
        print green(out_msg)

    def error(self, result):
        self.print_separator()
        out_msg = '[{}] {}\n请查看服务器下/root/workspace/log/supervisord.log文件'.format(
            datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            result)
        print red(out_msg)
        self.print_separator()

    @staticmethod
    def print_separator():
        print('-------------------------------------------------------')


class StorageManager(Task):
    name = "storage_manager"

    def __init__(self):
        super(StorageManager, self).__init__()
        self._util = MyFabricUtils()
        self.df_h_column_info = ['Filesystem', 'Size', 'Used', 'Avail', 'Use%', 'Mounted on']

    def run(self):
        execute(self.check_free)

    def check_free(self):
        for role in STORAGE_ROLES:
            for host_item in env.roledefs[role]:
                with settings(
                        hide('warnings', 'running', 'stdout', 'stderr'),
                        host_string=host_item,
                        clean_revert=True
                        # warn_only=True
                ):
                    storage_info = run('df -h')
                    infos = storage_info.strip().splitlines()
                    for line in infos[1:]:
                        disk_use_info = [i for i in line.split(' ') if i]
                        if int(disk_use_info[4].strip('%')) > 70:
                            msg = '### {} ### {} ### Avail:{} ### Mounted on:{}'.format(
                                role, host_item.split('@')[1], *disk_use_info[4:]
                            )
                            self._util.info(msg)


class PublishProject(Task):
    name = 'publish'

    def __init__(self):
        super(PublishProject, self).__init__()
        self._util = MyFabricUtils()
        self.project_groups = {
            '1': self.python,
            '2': self.laituia,
        }

    def run(self, groups):
        for i in groups.split(';'):
            execute(self.project_groups[i])

    @hosts('heiniu@47.92.52.151')
    def laituia(self):
        with settings(
                # hide('warnings', 'running', 'stdout', 'stderr'),
                # cd('~/redisdata'),
                clean_revert=True,
        ):
            # sudo('bash -x /root/fls_reload.sh')
            run('ls')

    @hosts('heiniu@47.92.93.236')
    def python(self):
        with settings(
                # hide('warnings', 'running', 'stdout', 'stderr'),
                # cd('~/redisdata'),
                clean_revert=True,
        ):
            # sudo('bash -x /root/muxiulin_conf/reload_web.sh ')
            run('ls')


storage_manager = StorageManager()
publish = PublishProject()
"""
fab publish:groups=1;2
fab storage_manager
"""