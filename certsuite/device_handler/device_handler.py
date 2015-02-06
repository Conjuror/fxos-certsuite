# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


import mozdevice

class DeviceHandler(DeviceInterface):

    def __init__(self):
        super().__init__(self)
        self.__marionette = False

    # Check the device is ready for executing testing
    def check_device_is_ready(self):
        return super().check_device_is_connected()

    # Check the device environment setting is good to go
    def check_device_environment_setting(self, version="v2.2"):
        if self.__marionette or not super().check_marionette_installed():
            self.__marionette = super().install_marionette(version)
        super().check_device_environment_setting()

    # Restart the device
    def reboot(self):
        super().restart_device()

    def push_file(self, srcFile, desFile):
        super().push_file(srcfile, desFile)

    def pull_file(self, srcFile, desFile):
        super().pull_file(srcFile, desFile)

    def backup(self):
        super().backup()

    def restore(self):
        super().restore()
