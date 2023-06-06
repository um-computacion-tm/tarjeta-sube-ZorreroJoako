class NoHaySaldoException(Exception):
    pass
class UsuarioDesactivadoException(Exception):
    pass
class EstadoNoExistenteException(Exception):
    pass

PRECIO_TICKET = 70
PRIMARIO = "primario"
SECUNDARIO = "secundario"
UNIVERSITARIO = "universitario"
JUBILADO = "jubilado"
ACTIVADO = "activado"
DESACTIVADO = "desactivado"
PENDIENTE = "pendiente"

DESCUENTOS = {
    PRIMARIO: 0.5,
    SECUNDARIO: 0.6,
    UNIVERSITARIO: 0.7,
    JUBILADO: 0.25,}

class Sube:
    def __init__(self):
        self.saldo = 0
        self.estado = ACTIVADO
        self.grupo_beneficiario = None

    def obtener_precio_ticket(self):
        if self.grupo_beneficiario in DESCUENTOS.keys():
            return PRECIO_TICKET * DESCUENTOS.get(self.grupo_beneficiario)
        else:
            return PRECIO_TICKET
        
    def pagar_pasaje(self):
        if self.estado == DESACTIVADO:
            raise UsuarioDesactivadoException()
        else:
            if self.grupo_beneficiario in DESCUENTOS.keys():
                if self.saldo >= (PRECIO_TICKET * DESCUENTOS.get(self.grupo_beneficiario)):
                    self.saldo-= (PRECIO_TICKET * DESCUENTOS.get(self.grupo_beneficiario))
                else:
                    raise NoHaySaldoException()
            else:
                if self.saldo>=PRECIO_TICKET:
                    self.saldo-=PRECIO_TICKET
                else:
                    raise NoHaySaldoException()
            
    def cambiar_estado(self,estado):
        validos=[ACTIVADO,DESACTIVADO]
        if not estado in validos:
            raise EstadoNoExistenteException()
        else:
            self.estado=estado