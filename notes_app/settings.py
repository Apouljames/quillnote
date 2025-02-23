class Settings:
    def __init__(self, store, defaults):
        self.defaults = defaults
        self.store = store(filename=self.defaults.DEFAULT_SETTINGS_STORE_FILE_NAME)
        self._set_missing_store_defaults()
        
        self.DROPBOX_API_TOKEN = "sl.u.AFitSdWeSY5Z1dL8Txei0E-yF27jko7XFQtWHmJ2GBVbufsytppl6CZ59rd0BCpBBrpCbcBBrKu4tispcRh3_bZaFlTEfDylpa1QHYrNscJMLYedNZ9RJjfyXjnOs3TacmZW8Hgj54jJHu43NPg1xS-FUzItKJ2pvW-FpUfq-veh1Ku4ITqgLgQaBsAIl2EBp4dmgRWG62prjXw4p6-7tIviR2cB50mlDNrfCeYXlPCbsx1Lw6GBUk6CxnTsTvFBExfZrQPGbhWDKc5dHsX7Tne3yXYaVa0IZ27aFyk9xF2qKfv290uqPxONRrPgvG2KPv1QEWGPoaGZ4-FUhpiVvnu3scOr0CLyPLbeXKfmV6OU1K6L-MvbwQW_UShGM2u1WxhCs-29JGHCvipEL_HHycjF-gcjC9gZvYz8T2aP1CQW8k_CNBwsZ9WUXjJdf5ffcFJSq2MjUf5aC6w__JD-Sqr_OHFP0lvK4DNV8uvGfKQRT_7dNFU_Uv7p55uH9KNreERteprYl04Eyd57OxaSFN9gWGIjLRiI7SYXzPZ7moUDnsIwjhuZT5R03bCjto_2wUvSLtunBYc70s0E3BMNsATxf12O-cn9WLdvhncoGAav8n_7T-MjAZblqe-ExRhPb1lMBQAiuppkh_jt9YP_DLf9kS9MpMN5I9td329rBhAZ8hq92HXttoRbhhw-Tj3-O_3NcmcHdCJG4ErgSlPjO1mcZrAXYArawf7BZKbmd_jnvVD9j2nD2hawhELbq67zRCRO2z8SA6Ri1fL6QZqgD6c0XTd-_E2V7sHoaM4nKr2MN7FiOI4Es1eGYRUc-NSYx2juzcjsi-CaG2xMaeFQVHrWYSlJt_TxQbjf1LjyvGidR2Jguu9xvtO4MKfavu-9UUjZZMEp-IsXDbr54AGn0fPkFA0E_LC-cZlhp_szhXgMoToVENBqhGuuNzLKTdZJzxNkI4sXmQllfZGRUBSyRP7aZzKsgCSFqzUvJ0RA6ITqrMgDky66CYyiIMqu1qJu3YV6HxwO2sjP1LsZo3WlN2QEtdRysnzXt1OXwLCKHQWGXAeBC_-WGTp5ZlqL5zf2M2IO6zScgWtC55tbRGCDvY8MLkblXjZgeZd75Qgm0HcS4tFV1e6XPOoYZUa2yPRj2rrUoiZLDxCW_nSYGnCRCeMHZ5SIrmMyJaS_DPzRgbkAyGinLYl7IPN4ZWkg9zYeSBzRR4_GLR_Vh5RdpIOP-2fh2y6D5npxSSE5O2uTwEb7GS3187fUArM0lDgTFlfPF-tBWKK6UKQE-l9pk_YpQg5H6UjS9IsomO2APfaXT0dCXbugLWegxnnRElwz15_Lk9F8d0dZBf2UghH-yGJCnW4GP7InRC2mpSUHC-z48inX_nGjATl3cXM-ZD8zY_DWTiF8sPuoxRpcnGcKUKDY-yoeoD3g4O1_178jLAEeX3bDog"

        self._font_name = self.store.get("font_name")["value"]
        self._font_size = self.store.get("font_size")["value"]
        self._background_color = self.store.get("background_color")["value"]
        self._foreground_color = self.store.get("foreground_color")["value"]

    def _set_missing_store_defaults(self):
        if (
            not self.store.exists("font_name")
            or self.store.get("font_name")["value"] is None
        ):
            self.store.put(
                "font_name", value=self.defaults.DEFAULT_SETTINGS_VALUE_FONT_NAME
            )

        if (
            not self.store.exists("font_size")
            or self.store.get("font_size")["value"] is None
        ):
            self.store.put(
                "font_size", value=self.defaults.DEFAULT_SETTINGS_VALUE_FONT_SIZE
            )

        if (
            not self.store.exists("background_color")
            or self.store.get("background_color")["value"] is None
        ):
            self.store.put(
                "background_color",
                value=self.defaults.DEFAULT_SETTINGS_VALUE_BACKGROUND_COLOR,
            )

        if (
            not self.store.exists("foreground_color")
            or self.store.get("foreground_color")["value"] is None
        ):
            self.store.put(
                "foreground_color",
                value=self.defaults.DEFAULT_SETTINGS_VALUE_FOREGROUND_COLOR,
            )

    @property
    def font_name(self):
        return self._font_name

    @font_name.setter
    def font_name(self, value):
        self._font_name = str(value)

    @property
    def font_size(self):
        return self._font_size

    @font_size.setter
    def font_size(self, value):
        self._font_size = str(value)

    @property
    def background_color(self):
        return self._background_color

    @background_color.setter
    def background_color(self, value):
        self._background_color = str(value)

    @property
    def foreground_color(self):
        return self._foreground_color

    @foreground_color.setter
    def foreground_color(self, value):
        self._foreground_color = str(value)

    def dump(self):
        self.store.put("font_name", value=self._font_name)
        self.store.put("font_size", value=self._font_size)
        self.store.put("background_color", value=self._background_color)
        self.store.put("foreground_color", value=self._foreground_color)
