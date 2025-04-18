FLUJO_ETAPAS = ["tecnico", "supervisor", "seguridad", "almacen"]

def etapas_previas(tipo):
    if tipo not in FLUJO_ETAPAS:
        return []
    index = FLUJO_ETAPAS.index(tipo)
    return FLUJO_ETAPAS[:index]
