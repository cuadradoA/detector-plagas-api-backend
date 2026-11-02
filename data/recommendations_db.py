"""
Base de conocimiento agronómica para diagnósticos, tratamientos, prevención y cuidados de plagas y enfermedades.
"""

RECOMMENDATIONS_DATABASE = {
    'spider_mites': {
        'keywords': ['mite', 'spider', 'acaro', 'araña'],
        'diagnostico': 'Ácaros arácnidos de dos manchas (Tetranychus urticae). Son plagas microscópicas que succionan la savia de las hojas, provocando clorosis punteada, telarañas finas en el envés y defoliación acelerada en ambientes secos y cálidos.',
        'tratamiento': [
            'Lava el follaje a presión con agua para desalojar los ácaros físicamente.',
            'Aplica jabón potásico o aceite de neem al 1-2% cada 5-7 días cubriendo muy bien el envés de las hojas.',
            'Introduce enemigos naturales como ácaros depredadores (Phytoseiulus persimilis o Amblyseius swirskii).',
            'En ataques severos, utiliza acaricidas específicos (abamectina o azufre micronizado) rotando modos de acción.'
        ],
        'prevencion': [
            'Mantén una humedad relativa adecuada en el cultivo; los ácaros proliferan con sequedad extrema.',
            'Inspecciona periódicamente el envés de hojas basales con una lupa de 10x o 20x.',
            'Evita fertilizaciones excesivas con nitrógeno que generan tejido tierno muy apetecible.',
            'Mantén el lote libre de malezas hospederas en los bordes y entre surcos.'
        ],
        'cuidados': [
            'Riega con regularidad para evitar estrés hídrico que debilita las defensas de la planta.',
            'Rota los cultivos por familias botánicas para interrumpir el ciclo biológico de la plaga.',
            'Aplica acolchado o mulch orgánico para conservar la humedad del suelo.'
        ],
        'urgencia': 'media'
    },
    'late_blight': {
        'keywords': ['late_blight', 'late blight', 'tizon tardio', 'infestans'],
        'diagnostico': 'Tizón tardío (Phytophthora infestans). Oomiceto altamente destructivo en solanáceas (tomate y papa). Causa manchas acuosas pardas en hojas y tallos, con moho blanco velloso visible bajo alta humedad y pudrición dura en frutos y tubérculos.',
        'tratamiento': [
            'ACCIÓN INMEDIATA: Retira y destruye fuera del lote las partes vegetales severamente afectadas.',
            'Aplica fungicidas protectores a base de cobre (hidróxido o sulfato tribásico) en etapas iniciales.',
            'En brotes avanzados, aplica fungicidas sistémicos (cymoxanil, metalaxil o propamocarb) siguiendo indicaciones técnicas.',
            'Suspende de inmediato el riego por aspersión; utiliza exclusivamente riego por goteo localizado.'
        ],
        'prevencion': [
            'Siembra variedades con resistencia o tolerancia genética reconocidas en la región.',
            'Mantén suficiente distancia entre surcos y plantas (50-70 cm) para máxima ventilación foliar.',
            'No transites por el cultivo con el follaje húmedo para no propagar esporangios.',
            'Aplica tratamientos preventivos de contacto ante pronósticos de alta humedad y temperaturas frescas (15-22 °C).'
        ],
        'cuidados': [
            'Riega temprano por la mañana para que las hojas se sequen durante las horas de sol.',
            'Poda las ramas basales que toquen el suelo para cortar vías de infección ascendente.',
            'Elimina restos de cosechas y tubérculos infectados en vertederos autorizados.'
        ],
        'urgencia': 'alta'
    },
    'early_blight': {
        'keywords': ['early_blight', 'early blight', 'tizon temprano', 'alternaria'],
        'diagnostico': 'Tizón temprano (Alternaria solani). Hongo común que produce manchas foliares circulares con anillos concéntricos oscuros característicos en "diana" o "tiro al blanco", comenzando por las hojas más viejas y causando defoliación progresiva.',
        'tratamiento': [
            'Poda y retira hojas bajeras infectadas para disminuir la carga de esporas.',
            'Aplica fungicidas como clorotalonil, mancozeb o azoxistrobina cada 7-10 días según presión de la enfermedad.',
            'Aplica acolchado plástico o paja sobre el suelo para evitar salpicaduras de esporas con las gotas de lluvia.',
            'Realiza aplicaciones de biofungicidas a base de Bacillus subtilis como alternativa ecológica.'
        ],
        'prevencion': [
            'Rotación de cultivos mínima de 2 a 3 años sin sembrar solanáceas en el mismo terreno.',
            'Utiliza semillas y plántulas certificadas libres de patógenos.',
            'Elimina los rastrojos y residuos de cultivos al final del ciclo productivo.',
            'Mantén un balance nutricional adecuado con suficiente potasio para fortalecer paredes celulares.'
        ],
        'cuidados': [
            'Riega a ras de suelo y nunca mojes el follaje.',
            'Tutora las plantas para mantenerlas erguidas y aireadas.',
            'Evita podas drásticas que provoquen estrés fisiológico innecesario.'
        ],
        'urgencia': 'media'
    },
    'bacterial_spot': {
        'keywords': ['bacterial', 'bacteria', 'xanthomonas', 'pseudomonas'],
        'diagnostico': 'Mancha bacteriana (Xanthomonas spp. / Pseudomonas spp.). Infección que genera pequeñas lesiones oscuras, circulares o angulares, rodeadas por un halo amarillento. Puede causar lesiones costrosas en frutos y pérdida de hojas.',
        'tratamiento': [
            'Elimina inmediatamente plantas enteras que muestren infección sistémica generalizada.',
            'Aplica bactericidas a base de compuestos cúpricos (oxicloruro o hidróxido de cobre) combinados con mancozeb.',
            'Desinfecta minuciosamente tijeras de poda y herramientas con alcohol al 70% o hipoclorito entre cada planta.',
            'Evita toda labor cultural o poda mientras el follaje conserve rocío o agua de lluvia.'
        ],
        'prevencion': [
            'Emplea semillas certificadas tratadas con agua caliente (50 °C por 25 minutos).',
            'Instala riego por goteo subterráneo o superficial; el agua libre es el principal vehículo bacteriano.',
            'Controla insectos masticadores que generan heridas de entrada para las bacterias.',
            'Usa variedades con resistencia genética validada.'
        ],
        'cuidados': [
            'Garantiza un drenaje óptimo en el suelo para evitar encharcamientos continuos.',
            'Monitorea el cultivo cada 48 horas en temporadas cálidas y lluviosas.',
            'Modera el nitrógeno para evitar tejidos hiperhidratados y blandos.'
        ],
        'urgencia': 'media'
    },
    'powdery_mildew_mold': {
        'keywords': ['mildew', 'powdery', 'oidio', 'cenicilla', 'mold', 'moho'],
        'diagnostico': 'Oídio o moho foliar (Erysiphe / Leveillula / Passalora fulva). Formación de un polvo blanquecino o cenizo en haz y envés de las hojas, que reduce la fotosíntesis y marchita prematuramente el follaje.',
        'tratamiento': [
            'Aplica azufre micronizado en polvo mojable en horas tempranas evitando superar los 30 °C.',
            'Aplica bicarbonato de potasio o de sodio (4-5 g/litro) como solución foliar de contacto.',
            'Poda ramas interiores para favorecer la penetración de luz y ventilación natural.',
            'Aplica biofungicidas antagónicos como Trichoderma harzianum.'
        ],
        'prevencion': [
            'Garantiza un mínimo de 6 a 8 horas de radiación solar directa sobre las plantas.',
            'Amplía la densidad de siembra para permitir paso continuo de corrientes de aire.',
            'Limpia estructuras de invernadero y mallas de sombreo con desinfectantes.'
        ],
        'cuidados': [
            'Riega en la base durante la mañana.',
            'Mantén el suelo aireado con podas sanitarias periódicas.'
        ],
        'urgencia': 'baja'
    },
    'septoria': {
        'keywords': ['septoria', 'septoriosis'],
        'diagnostico': 'Septoriosis de la hoja (Septoria lycopersici). Hongo foliar que provoca numerosas manchas circulares pequeñas con centro gris blanquecino y borde pardo oscuro, donde se aprecian puntos negros microscópicos (picnidios).',
        'tratamiento': [
            'Retira de inmediato las hojas bajeras que exhiban síntomas.',
            'Aplica fungicidas como clorotalonil, captan o difenoconazol respetando plazos de seguridad.',
            'Instala coberturas plásticas o mulching sobre los surcos para evitar salpiqueo.'
        ],
        'prevencion': [
            'Rotación obligatoria con cultivos que no sean solanáceas por mínimo 2 campañas.',
            'Destrucción de residuos y desinfección del suelo antes del trasplante.',
            'Desinfección de tutores, estacas e hilos de tutorado.'
        ],
        'cuidados': [
            'Riego estrictamente localizado sin mojar follaje.',
            'Poda sanitaria semanal de hojas basales viejas.'
        ],
        'urgencia': 'media'
    },
    'virus': {
        'keywords': ['virus', 'mosaic', 'mosaico', 'yellow_leaf', 'yellowleaf', 'curl'],
        'diagnostico': 'Infección viral (Virus del mosaico del tomate / Virus del enrollamiento de la hoja amarilla / TMV / TYLCV). Provoca moteado clorótico verde claro/oscuro, hojas acopadas, enanismo severo y deformación en frutos.',
        'tratamiento': [
            'NO EXISTE CURA QUÍMICA: Arranca y destruye de raíz las plantas enfermas en bolsas cerradas para evitar contagio.',
            'Controla exhaustivamente a los insectos vectores: mosca blanca (Bemisia tabaci) y pulgones.',
            'Lava manos con agua y jabón antes de manipular plantas (el TMV se propaga mecánicamente por contacto).',
            'Instala trampas cromotrópicas amarillas pegajosas para captura masiva de vectores.'
        ],
        'prevencion': [
            'Utiliza mallas anti-áfidos y anti-mosca blanca (mallas de 50 mesh o superior) en invernaderos.',
            'Siembra híbridos comerciales resistentes a TYLCV y virus del mosaico.',
            'Elimina malezas de la familia Solanaceae (hierba mora, etc.) en un radio de 50 metros.'
        ],
        'cuidados': [
            'Monitorea la presencia de mosca blanca desde el semillero.',
            'Desinfecta implementos de trabajo con fosfato trisódico al 10% o cloro.'
        ],
        'urgencia': 'alta'
    },
    'target_spot': {
        'keywords': ['target_spot', 'target spot', 'corynespora'],
        'diagnostico': 'Mancha blanco o target spot (Corynespora casiicola). Lesiones foliares con centros necróticos de aspecto acorchado o papiráceo, frecuentemente con halos amarillos circundantes.',
        'tratamiento': [
            'Elimina follaje infectado y aumenta la aireación.',
            'Aplica fungicidas a base de estrobirulinas o triazoles autorizados.',
            'Evita humedad relativa prolongada superior al 85%.'
        ],
        'prevencion': [
            'Mejora el drenaje del suelo y la ventilación del dosel vegetal.',
            'Utiliza semillas sanas y certificadas.'
        ],
        'cuidados': [
            'Manejo de podas y tutorado vertical continuo.'
        ],
        'urgencia': 'media'
    },
    'healthy': {
        'keywords': ['healthy', 'sana', 'sano', 'saludable'],
        'diagnostico': '¡Planta en estado óptimo y saludable! El tejido foliar muestra coloración uniforme, sin manchas necróticas, deformaciones, clorosis patológica ni presencia aparente de plagas o patógenos fúngicos/bacterianos.',
        'tratamiento': [
            'No requiere tratamientos curativos.',
            'Continúa con las prácticas agronómicas actuales que han demostrado ser efectivas.',
            'Mantén el programa preventivo de monitoreo visual semanal.'
        ],
        'prevencion': [
            'Inspecciona periódicamente el haz y envés de las hojas.',
            'Mantén las herramientas limpias y desinfectadas.',
            'Evita encharcamientos y exceso de fertilizantes solubles.'
        ],
        'cuidados': [
            'Riega según la demanda del cultivo y el tipo de suelo (cuando los primeros 2-3 cm de suelo estén secos).',
            'Aplica planes de fertilización balanceados N-P-K con microelementos.',
            'Asegura una iluminación adecuada para una fotosíntesis activa.'
        ],
        'urgencia': 'baja'
    }
}

DEFAULT_RECOMMENDATION = {
    'diagnostico': 'Condición detectada: {disease}. Se recomienda seguimiento cuidadoso y aislamiento de la planta afectada para observar la evolución de los síntomas.',
    'tratamiento': [
        'Aísla la planta afectada para prevenir posible propagación a cultivos vecinos.',
        'Retira de manera preventiva las partes vegetales visiblemente dañadas con herramientas desinfectadas.',
        'Consulta con un extensionista agrícola o agrónomo local para un diagnóstico confirmatorio.'
    ],
    'prevencion': [
        'Mantén un drenaje eficiente en el suelo para evitar anoxia radicular.',
        'Asegura una ventilación generosa entre plantas con podas de aclareo.',
        'Inspecciona rutinariamente el cultivo para detección temprana de plagas.'
    ],
    'cuidados': [
        'Riega en las horas tempranas de la mañana evitando mojar el follaje.',
        'Mantén el área libre de malezas y rastrojos acumulados.',
        'Aplica nutrientes balanceados acordes al estado fenológico del cultivo.'
    ],
    'urgencia': 'media'
}
