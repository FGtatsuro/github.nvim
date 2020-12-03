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

    def parse_origin_url(self):
        # Support origin URL like git@github.com:FGtatsuro/github.nvim.git
        origin_url = subprocess.run(
            'git config --local --get remote.origin.url'.split(),
            capture_output=True,
            text=True).stdout.strip().split(':')

        host = origin_url[0].split('@')[1]
        # Cover github.com/gitlab.com
        if host.endswith('.com'):
            base = f'https://{host}'
        else:
            base = 'https://github.com'

        repo = origin_url[1]
        if repo.endswith('.git'):
            repo = repo[:-4]
        org, repo = repo.split('/')

        return base, org, repo

    def open_github_webpage(self, _range):
        base, org, repo = self.parse_origin_url()
        branch = 'master'

        # Root directory may have a different name from repository name.
        root = subprocess.run(
            'git rev-parse --show-toplevel'.split(),
            capture_output=True,
            text=True).stdout.strip()
        root = pathlib.Path(root)
        current = self.nvim.command_output('echo expand("%:p")').strip()
        current = pathlib.Path(current)

        url = f'{base}/{org}/{repo}/tree/{branch}/{current.relative_to(root)}'
        if current.is_file():
            if _range[0] == _range[1]:
                url = f'{url}#L{_range[0]}'
            else:
                if base == 'https://github.com':
                    url = f'{url}#L{_range[0]}-L{_range[1]}'
                else:
                    # Now, Supporting gitlab requires this format.
                    url = f'{url}#L{_range[0]}-{_range[1]}'
        self.browser.open(url)

# https://wiki.python.org/moin/Vim
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
