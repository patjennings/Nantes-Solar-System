import os

mapniklibpath = '/usr/local/lib/mapnik'
mapniklibpath = os.path.normpath(mapniklibpath)
inputpluginspath = os.path.join(mapniklibpath,'input')
fontscollectionpath = os.path.join(mapniklibpath,'fonts')
__all__ = [mapniklibpath,inputpluginspath,fontscollectionpath]
