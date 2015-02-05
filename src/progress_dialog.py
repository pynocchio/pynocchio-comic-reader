# -*- coding:utf-8 -*-
# Copyright (C) 2015  Michell Stuttgart

# This library is free software; you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation; either version 3.0 of the License, or (at
# your option) any later version.

# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public
# License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with this library.  If not, see <http://www.gnu.org/licenses/>.

from PyQt4 import QtGui
from PyQt4 import QtCore


class ProgressDialog(QtGui.QProgressDialog):
    def __init__(self, msg, button, initial_step, final_step, parent=None):
        super(ProgressDialog, self).__init__(msg, button, initial_step,
                                             final_step, parent)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.setAutoReset(True)
        self.setAutoClose(True)
        self.resize(350, 50)