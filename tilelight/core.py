# -*- coding: utf-8 -*-
"""瓦片光照传播"""

from dataclasses import dataclass


@dataclass
class TileMap:
    """瓦片地图。"""
    width: int
    height: int
    walls: set


def propagate(map, lights):
    """传播光照"""
    raise NotImplementedError("propagate 尚未实现")


def occluders(map, x, y):
    """取遮挡体"""
    raise NotImplementedError("occluders 尚未实现")


def attenuation(dist):
    """衰减函数"""
    raise NotImplementedError("attenuation 尚未实现")


def load_map(path):
    """读入与落盘辅助"""
    raise NotImplementedError("load_map 尚未实现")

