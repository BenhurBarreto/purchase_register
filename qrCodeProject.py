from le_qrCode import LeQrCode
from consultaNF import ConsultaNF

leQrCode = LeQrCode()
consultaNF = ConsultaNF(leQrCode.inicia_captura())
consultaNF.coleta_dados_da_NF()
