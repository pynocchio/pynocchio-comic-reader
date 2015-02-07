# coding=UTF-8
#
# Copyright (C) 2015  Michell Stuttgart

# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.

# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

import rarfile
from PyQt4.QtCore import QCoreApplication

from loader import Loader
import progress_dialog
from page import Page
from utility import Utility


class RarLoader(Loader):
    _entity_ = 'rar'

    def __init__(self):
        super(RarLoader, self).__init__()

    def load(self, file_name):

        file_name = str(file_name)

        if not self.is_rar_file(file_name):
            return False

        try:
            rar = rarfile.RarFile(file_name, 'r')
        except rarfile.RarOpenError, err:
            print '%20s  %s' % (file_name, err)
            return False

        name_list = rar.namelist()
        name_list.sort()

        # dlg = progress_dialog.ProgressDialog("Please Wait", "Cancel", 0,
        #                                      len(name_list))
        # dlg.setWindowTitle('Loading Comic File')
        # dlg.show()

        # count_page = 1
        for name in name_list:
            file_extension = Utility.get_file_extension(name.encode('utf-8'))

            # dlg.setValue(name_list.index(name))
            # QCoreApplication.instance().processEvents()
            # if dlg.wasCanceled():
            #     raise GeneratorExit

            if not rar.getinfo(name).isdir():

                if Utility.get_file_extension(name).lower() in self.extension:
                    self.data.append({'data': rar.read(name), 'name': name})
                    # count_page += 1

        rar.close()
        return True

    # def _load_core(self, pages, file_name):
    #
    #     file_name = str(file_name)
    #     try:
    #         rar = rarfile.RarFile(file_name, 'r')
    #     except rarfile.RarOpenError, err:
    #         print '%20s  %s' % (file_name, err)
    #         return
    #
    #     name_list = rar.namelist()
    #     name_list.sort()
    #
    #     dlg = progress_dialog.ProgressDialog("Please Wait", "Cancel", 0,
    #                                          len(name_list))
    #     dlg.setWindowTitle('Loading Comic File')
    #     dlg.show()
    #
    #     count_page = 1
    #     for name in name_list:
    #         _, file_extension = os.path.splitext(name)
    #
    #         dlg.setValue(name_list.index(name))
    #         QCoreApplication.instance().processEvents()
    #         if dlg.wasCanceled():
    #             raise GeneratorExit
    #
    #         if not rar.getinfo(
    #                 name).isdir() and file_extension.lower() in self.extension:
    #             pages.append(Page(rar.read(name), name, count_page))
    #             count_page += 1
    #
    #     rar.close()

    @staticmethod
    def is_rar_file(file_name):
        return rarfile.is_rarfile(str(file_name))
