#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import webbrowser


class GithubHandler():

    def __init__(self, nvim):
        self.nvim = nvim
        # Ref. https://docs.python.org/3/library/webbrowser.html#webbrowser.register
        self.browser = webbrowser.get('macosx')
        self.base = 'https://github.com'

    def open_github_webpage(self):
        repo = subprocess.run(
            'git config --local --get remote.origin.url'.split(),
            capture_output=True,
            text=True).stdout
        org, repo = repo.split(':')[1].strip().strip('.git').split('/')
        branch = 'master'
        # ToDo: リポジトリ名と違う名前でcloneしている場合に対応する
        path = self.nvim.command_output('echo expand("%:p")').split(repo)[1]
        self.browser.open(f'{self.base}/{org}/{repo}/tree/{branch}/{path}')

# https://wiki.python.org/moin/Vim
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
