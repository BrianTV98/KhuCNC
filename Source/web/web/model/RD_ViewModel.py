import  math
class RD_ViewModel:
    def __init__(self, TEN_DN, NAM, TY_LE_CHI_PHI_RD, TY_LE_DH_TREN_DH_THAM_GIA_RD, KINH_PHI=0):
        if math.isnan(float(TY_LE_CHI_PHI_RD)):
            TY_LE_CHI_PHI_RD = 0
        else:
            self.TY_LE_CHI_PHI_RD = TY_LE_CHI_PHI_RD
        self.TEN_DN = TEN_DN
        self.NAM = NAM

        self.TY_LE_DH_TREN_DH_THAM_GIA_RD = TY_LE_DH_TREN_DH_THAM_GIA_RD
        self.KINHPHI = KINH_PHI
