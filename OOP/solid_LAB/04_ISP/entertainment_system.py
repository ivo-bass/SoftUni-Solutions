class ConnectViaHdmiMixin:
    def connect_to_device_via_hdmi_cable(self, device): pass


class ConnectViaRcaMixin:
    def connect_to_device_via_rca_cable(self, device): pass


class ConnectViaEthernetMixin:
    def connect_to_device_via_ethernet_cable(self, device): pass


class ConnectViaPowerCableMixin:
    def connect_device_to_power_outlet(self): pass


class EntertainmentDevice(ConnectViaPowerCableMixin):
    def plug_in_power(self):
        self.connect_device_to_power_outlet()


class Television(EntertainmentDevice, ConnectViaRcaMixin, ConnectViaHdmiMixin):
    def connect_to_dvd(self, dvd_player):
        self.connect_to_device_via_rca_cable(dvd_player)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_hdmi_cable(game_console)


class DVDPlayer(EntertainmentDevice, ConnectViaHdmiMixin):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)


class GameConsole(EntertainmentDevice, ConnectViaHdmiMixin, ConnectViaEthernetMixin):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)

    def connect_to_router(self, router):
        self.connect_to_device_via_ethernet_cable(router)


class Router(EntertainmentDevice, ConnectViaEthernetMixin):
    def connect_to_tv(self, television):
        self.connect_to_device_via_ethernet_cable(television)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_ethernet_cable(game_console)
