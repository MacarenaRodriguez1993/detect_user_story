import datetime

TIEMPO_MAX_INACTIVIDAD = datetime.timedelta(minutes=5)


def detectar_historias_generales(eventos):
    historias = []
    historia_actual = None
    formato_fecha = "%Y-%m-%dT%H:%M:%S.%fZ"
    for evento in eventos:
        timestamp = datetime.datetime.strptime(evento.timestamp, formato_fecha)
        url_actual = evento.current_url
        event_type = evento.event_type
        elemento = evento.element_text

        
        if historia_actual is None:
            historia_actual = {
                "inicio": timestamp,
                "eventos": [evento],
                "contexto": url_actual 
            }
        else:          
            timestamp_ultimo_evento = datetime.datetime.strptime(historia_actual['eventos'][-1].timestamp, formato_fecha)
            
            tiempo_entre_eventos = timestamp - timestamp_ultimo_evento

            if url_actual == historia_actual["contexto"] and tiempo_entre_eventos < TIEMPO_MAX_INACTIVIDAD:
                historia_actual['eventos'].append(evento)
            else:
                historia_actual['fin'] = historia_actual['eventos'][-1].timestamp
                historias.append(historia_actual)
            
                historia_actual = {
                    "inicio": timestamp,
                    "eventos": [evento],
                    "contexto": url_actual
                }


    if historia_actual:
        historia_actual['fin'] = historia_actual['eventos'][-1].timestamp
        historias.append(historia_actual)
    return historias
