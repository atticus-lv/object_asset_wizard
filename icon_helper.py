# Copyright (C) 2019 h0bB1T
#

import bpy
from .t3dn_bip import previews


class IconHelper:

    icons = None

    @staticmethod
    def init():
        IconHelper.icons = previews.new()

    
    @staticmethod
    def dispose():
        previews.remove(IconHelper.icons)


    @staticmethod
    def get_icon(path: str):
        if path not in IconHelper.icons:
            IconHelper.icons.load(path, path, 'IMAGE')
        return IconHelper.icons[path].icon_id

        