def simular_apd(transiciones, estado_inicial, acepta_por, estados_finales, palabra):
    pila = ['R']  # Símbolo inicial de la pila
    estado_actual = estado_inicial
    palabra = palabra.copy()  # Evita modificar la lista original

    while True:
        simbolo_entrada = palabra[0] if palabra else ''
        tope_pila = pila[-1] if pila else ''

        # Buscar una transición válida
        transicion_valida = None
        for t in transiciones:
            (e_actual, s_entrada, s_pila, e_nuevo, s_apilar) = t
            if e_actual == estado_actual and \
               (s_entrada == simbolo_entrada or s_entrada == '') and \
               (s_pila == tope_pila or s_pila == ''):
                transicion_valida = t
                break

        if not transicion_valida:
            break  # No hay transición válida, detener simulación

        # Ejecutar transición
        (e_actual, s_entrada, s_pila, e_nuevo, s_apilar) = transicion_valida

        if s_entrada != '':
            palabra.pop(0)
        if s_pila != '':
            pila.pop()
        if s_apilar != '':
            # Nota: puede apilar más de un símbolo (ej: 'AB')
            for simbolo in reversed(s_apilar):
                pila.append(simbolo)

        estado_actual = e_nuevo

    # Criterios de aceptación
    if acepta_por == "estado_final":
        return estado_actual in estados_finales and not palabra
    elif acepta_por == "pila_vacia":
        return not pila and not palabra
    else:
        raise ValueError("Método de aceptación inválido.")