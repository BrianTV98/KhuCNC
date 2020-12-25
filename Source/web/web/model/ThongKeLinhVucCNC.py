class ThongKeLinhVucCNC:
    def __init__(self, MA_LVCNC, DIEN_GIAI,TONGSO, VONDAUTU):
        if MA_LVCNC is None:
            self.MA_LVCNC = '',
        else:
            self.MA_LVCNC = MA_LVCNC
        self.DIEN_GIAI =DIEN_GIAI
        self.TONGSO = TONGSO
        self.VONDAUTU = VONDAUTU