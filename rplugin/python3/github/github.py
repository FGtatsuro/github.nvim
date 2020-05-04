#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pathlib
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
            text=True).stdout.strip()
        org, repo = repo.split(':')[1].strip('.git').split('/')
        branch = 'master'

        # Root directory may have a different name from repository name.
        root = subprocess.run(
            'git rev-parse --show-toplevel'.split(),
            capture_output=True,
            text=True).stdout.strip()
        root = pathlib.Path(root)
        current = self.nvim.command_output('echo expand("%:p")').strip()
        current = pathlib.Path(current)
        self.browser.open(f'{self.base}/{org}/{repo}/tree/{branch}/{current.relative_to(root)}')

# https://wiki.python.org/moin/Vim
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
