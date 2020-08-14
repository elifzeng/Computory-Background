#!/usr/bin/python
# 网站缓存网页模式——缓存网页URL和网页数据，并将前者映射到后者
"""
cache = {}

def get_page(url):
    if cache.get(url):
        return cache[url] # 返回缓存的数据
    else:
        data = get_page_from_server(url) # 若网页数据没有缓存到本地，就从服务器获取数据，并缓存到本地
        cache[url] = data
        return data
"""

