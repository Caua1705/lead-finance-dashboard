from datetime import datetime, time

def formatar_periodo(periodo):
    data_inicial = datetime.combine(periodo[0], time.min)
    data_final = datetime.combine(periodo[-1], time.max)
    return data_inicial, data_final
