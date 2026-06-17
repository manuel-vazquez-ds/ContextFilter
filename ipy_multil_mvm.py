# en: ===== PART FOR MULTI-LINGUAL =====
# es: ===== PARTE PARA MULTI-IDIOMA =====
# ca: ===== PART PER MULTI-IDIOMA =====


# en: Create dictionary for language selection
# es: Crear diccionario para selección de idioma
# ca: Crear diccionari per selecció d'idioma

languages = {
    'English': {"barrencar_desc": "Start", "baturar_desc": "Stop",
    "estat_lbl":{"funcionament":"🟢 ContextFilter is running ({laUrl})","aturat":"🔴 Stopped ContextFilter","API_off":"🔴 API is off"},
    "info_lbl":{"funcionament": "⚠️ ContextFilter is already up and running", "iniciat": "🚀 ContextFilter started","aturant":"⛔ Stopping ContextFilter",
    "waiting": "...waiting","inactiu": "⚠️ ContextFilter is not active.","awaiting": "...awaiting orders", "curl": "curl request made",
    "requests": "Requests request made", "ok": "Review evaluation with ipywidgets processed correctly",
    "error": "Error evaluating the review with ipywidgets",
    "fich_ok":"File received and processed correctly. Records: {records}, flagged: {flagged}, average coefficient: {average_coefficient}. Saving the received file...",
    "error_status":"Error status code: {status_code}", "fnotfound":"File not found {filename}",
    "evalfileok":"File evaluation with ipywidgets processed correctly", "evalfileerror":"Error evaluating the file with ipywidgets"},
    "review_desc": "Review","review_placeholder": "Enter the review here", "threshold_desc": "Threshold", "threshold_placeholder": "Between 0 and 1",
    "llista_desc": "List", "llista_placeholder": "List format [[\"text\",\"text\"],...]", "add_desc": "Add", "send_desc": "Send review",
    "opcions_ad_desc": "Additional options",
    "file":{"SelectedNone":"No file selected","Selected":"File selected: {nom}"},"send_file_desc": "Send file", "retorn_desc": "Return"},
    'Español': {"barrencar_desc": "Iniciar", "baturar_desc": "Detener",
    "estat_lbl":{"funcionament":"🟢 ContextFilter está funcionando ({laUrl})","aturat":"🔴 ContextFilter detenido","API_off":"🔴 API apagada"},
    "info_lbl":{"funcionament": "⚠️ ContextFilter ya está activo", "iniciat": "🚀 ContextFilter iniciado","aturant":"⛔ Deteniendo ContextFilter",
    "waiting": "...en espera", "inactiu": "⚠️ ContextFilter no está activo","awaiting": "...esperando órdenes", "curl": "petición curl realizada",
    "requests": "petición Requests realizada", "ok": "Evaluación de reseña con ipywidgets procesada correctamente",
    "error": "Error evaluando la reseña con ipywidgets",
    "fich_ok":"Archivo recibido y procesado correctamente. Registros: {records}, marcados: {flagged}, coeficiente promedio: {average_coefficient}. Guardando el archivo recibido...",
    "error_status":"Error código de status: {status_code}", "fnotfound":"Archivo no encontrado: {filename}",
    "evalfileok":"Evaluación de archivo con ipywidgets procesada correctamente", "evalfileerror":"Error evaluando el archivo con ipywidgets"},
    "review_desc": "Reseña","review_placeholder": "Introduce la reseña aquí", "threshold_desc": "Coeficiente", "threshold_placeholder": "Entre 0 y 1",
    "llista_desc": "Lista", "llista_placeholder": "Formato de lista [[\"texto\",\"texto\"],...]", "add_desc": "Añadir", "send_desc": "Enviar reseña",
    "opcions_ad_desc": "Opciones adicionales",
    "file":{"SelectedNone":"Ningún fichero seleccionado","Selected":"Fichero seleccionado: {nom}"},"send_file_desc": "Enviar archivo", "retorn_desc": "Retorno"},
    'Català': {"barrencar_desc": "Arrencar", "baturar_desc": "Aturar",
    "estat_lbl":{"funcionament":"🟢 ContextFilter està funcionant ({laUrl})","aturat":"🔴 ContextFilter aturat","API_off":"🔴 API aturada"},
    "info_lbl":{"funcionament": "⚠️ ContextFilter ja està actiu", "iniciat": "🚀 ContextFilter iniciat", "aturant":"⛔ Aturant ContextFilter",
    "waiting": "...en espera", "inactiu": "⚠️ ContextFilter no està actiu","awaiting": "...esperant ordres", "curl": "petició curl realitzada",
    "requests": "petició Requests realitzada", "ok": "Evaluació de ressenya amb ipywidgets processada correctament",
    "error": "Error avaluant la ressenya amb ipywidgets",
    "fich_ok":"Arxiu rebut i processat correctament. Registres: {records}, marcats: {flagged}, coeficient mitjà: {average_coefficient}. Guardant el fitxer rebut...",
    "error_status":"Error codi de status: {status_code}", "fnotfound":"Fitxer no trobat: {filename}",
    "evalfileok":"Avaluació de fitxer amb ipywidgets processada correctament", "evalfileerror":"Error avaluant el fitxer amb ipywidgets"},
    "review_desc": "Ressenya","review_placeholder": "Introdueix la resenya aquí", "threshold_desc": "Llindar", "threshold_placeholder": "Entre 0 i 1",
    "llista_desc": "Llista", "llista_placeholder": "Format de llista [[\"text\",\"text\"],...]", "add_desc": "Afegir", "send_desc": "Enviar ressenya",
    "opcions_ad_desc": "Opcions addicionals",
    "file":{"SelectedNone":"Cap fitxer seleccionat","Selected":"Fitxer seleccionat: {nom}"},"send_file_desc": "Enviar fitxer", "retorn_desc": "Retorn"}
}

caches = {
    "English": {"info_lbl": "", "estat_lbl": ""},
    "Español": {"info_lbl": "", "estat_lbl": ""},
    "Català": {"info_lbl": "", "estat_lbl": ""}
}

def actualitzar_ctls(idioma: str, elControl: str, clau: str, **params):
    for llengua in ["English", "Español", "Català"]:
        caches[llengua][elControl] = languages[llengua][elControl][clau].format(**params)
    # return languages[idiomaActual][clau].format(**params)
    return caches[idioma][elControl]
