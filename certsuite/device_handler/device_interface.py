# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


import mozdevice

class DeviceInterface(object):

    def __init__(self, device):
        self.device = device
        pass

    """
    Please implement the following functions if your devices is not support android debug bridge
    """
    # Check the device is ready for executing testing
    def check_device_is_ready(self):
        self.check_network()

    # Check the device environment setting is good to go
    def check_device_environment_setting(self, version="v2.2"):
        if self.__marionette or not super().check_marionette_installed():
            self.__marionette = super().install_marionette(version)
        super().check_device_environment_setting()

    # Restart the device
    def reboot(self):
        super().restart_device()
    """
    End of interface function
    """

    def check_adb():
        pass

    def check_root():
        pass

    def install_marionette(device, version):
        pass


    def check_network(device):
        try:
            device.wait_for_net()
            return True
        except adb_b2g.WaitTimeout:
            logger.critical("Failed to get a network connection")
            return False

    def ensure_settings(device):
        test_settings = {"screen.automatic-brightness": False,
                         "screen.brightness": 1.0,
                         "screen.timeout": 0.0}
        logger.info("Setting up device for testing")
        with MarionetteSession(device) as marionette:
            settings = gaiautils.Settings(marionette)
            for k, v in test_settings.iteritems():
                settings.set(k, v)
        return True

    def check_preconditions(config):
        check_marionette_installed = lambda device: install_marionette(device, config['version'])

        device = check_adb()
        if not device:
            sys.exit(1)

        for precondition in [check_root,
                             check_marionette_installed,
                             ensure_settings,
                             check_network,
                             check_server]:
            try:
                passed = precondition(device)
            except:
                logger.critical("Error during precondition check:\n%s" % traceback.format_exc())
                passed = False
            if not passed:
                device.reboot()
                sys.exit(1)

        logger.info("Passed precondition checks")


    def install_marionette(self, device, version):
        try:
            logger.info("Installing marionette extension")
            try:
                marionette_install(version)
            except AlreadyInstalledException:
                logger.info("Marionette is already installed")
        except subprocess.CalledProcessError:
            logger.critical(
                "Error installing marionette extension:\n%s" % traceback.format_exc())
            raise
        except subprocess.CalledProcessError as e:
            logger.critical('Error installing marionette extension: %s' % e)
            logger.critical(traceback.format_exc())
            return False
        except adb_b2g.WaitTimeout:
            logger.critical("Timed out waiting for device to become ready")
            return False
        device.restart()
        return True