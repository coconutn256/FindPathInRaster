# -*- coding: utf-8 -*-
"""
/***************************************************************************
 RasterShortestPath
                                 A QGIS plugin
 Calculate the shortest path between two points on a raster
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-11-08
        copyright            : (C) 2019 by CoolGroup
        email                : noway@noway.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load RasterShortestPath class from file RasterShortestPath.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .raster_shortest_path import RasterShortestPath
    return RasterShortestPath(iface)
