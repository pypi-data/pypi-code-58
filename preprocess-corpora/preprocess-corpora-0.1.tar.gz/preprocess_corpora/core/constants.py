GERMAN = 'de'
ENGLISH = 'en'
SPANISH = 'es'
FRENCH = 'fr'
ITALIAN = 'it'
DUTCH = 'nl'
RUSSIAN = 'ru'
CATALAN = 'ca'
SWEDISH = 'sv'
PORTUGUESE = 'pt'
BRETON = 'br'

RIOPLATENSE = 'ar'
MEXICAN = 'mx'
VARIETIES = {RIOPLATENSE: SPANISH, MEXICAN: SPANISH}

LANGUAGES = [GERMAN, ENGLISH, SPANISH, FRENCH, ITALIAN, DUTCH, RUSSIAN, CATALAN, SWEDISH, PORTUGUESE, BRETON] \
            + list(VARIETIES.keys())
