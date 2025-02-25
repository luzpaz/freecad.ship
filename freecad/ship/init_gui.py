#***************************************************************************
#*                                                                         *
#*   Copyright (c) 2011, 2016 Jose Luis Cercos Pita <jlcercos@gmail.com>   *
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU Lesser General Public License (LGPL)    *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   This program is distributed in the hope that it will be useful,       *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Library General Public License for more details.                  *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with this program; if not, write to the Free Software   *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#***************************************************************************

import FreeCADGui as Gui
import FreeCAD as App
import os

class ShipWorkbench(Gui.Workbench):
    """Ships design workbench."""
    def __init__(self):
        _dir = os.path.dirname(__file__)
        self.__class__.Icon = os.path.join(_dir, "resources", "icons", "Ship_Workbench.svg")
        self.__class__.MenuText = "Ship"
        self.__class__.ToolTip = "Ship module provides some of the commonly used tool to design ship forms"

    from . import ShipGui

    def Initialize(self):
        from PySide import QtCore, QtGui

        try:
            import FreeCAD.Plot
        except ImportError:
            try:
                import freecad.plot
            except ImportError:
                msg = QtGui.QApplication.translate(
                    "ship_console",
                    "freecad.plot is disabled, tools cannot graph output curves, install freecad.plot with addon-manager",
                    None)
                App.Console.PrintWarning(msg + '\n')
        # ToolBar
        shiplist = ["Ship_LoadExample",
                    "Ship_CreateShip",
                    "Ship_AreasCurve",
                    "Ship_Hydrostatics"]
        weightslist = ["Ship_Weight",
                       "Ship_Tank",
                       "Ship_Capacity",
                       "Ship_LoadCondition",
                       "Ship_SinkAndTrim",
                       "Ship_GZ"]
        seakeepinglist = ["Seakeeping_SetMesh",
                          "Seakeeping_RAOs"]

        self.appendToolbar(
            str(QtCore.QT_TRANSLATE_NOOP("Ship", "Ship design")),
            shiplist)
        self.appendToolbar(
            str(QtCore.QT_TRANSLATE_NOOP("Ship", "Weights")),
            weightslist)
        self.appendToolbar(
            str(QtCore.QT_TRANSLATE_NOOP("Ship", "Seakeeping")),
            seakeepinglist)
        self.appendMenu(
            str(QtCore.QT_TRANSLATE_NOOP("Ship", "Ship design")),
            shiplist)
        self.appendMenu(
            str(QtCore.QT_TRANSLATE_NOOP("Ship", "Weights")),
            weightslist)
        self.appendMenu(
            str(QtCore.QT_TRANSLATE_NOOP("Ship", "Seakeeping")),
            seakeepinglist)

Gui.addWorkbench(ShipWorkbench())
