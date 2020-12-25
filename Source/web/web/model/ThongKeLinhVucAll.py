class ThongKeLinhVucAll:
    def __init__(self, MA_CTHTDT, TONGSO, VONDAUTU):
        if MA_CTHTDT is None:
            self.MA_CTHTDT = "",
        else:self.MA_CTHTDT = MA_CTHTDT
        self.TONGSO = TONGSO
        self.VONDAUTU = VONDAUTU