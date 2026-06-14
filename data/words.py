# PhonIQ - 単語データベース
# 各単語には発音記号、音節分割、アクセント位置、類似単語グループを持たせる

# word: 英単語
# ipa: 発音記号 (IPA)
# syllables: 音節リスト（各音節のIPA）
# stress: アクセントのある音節のインデックス (0始まり)
# category: 発音パターンのカテゴリID（Phaseとの連携用）
# similar_group: 似た発音を持つグループID（選択肢生成に使用）

WORDS = [
    # --- 単母音 a (short) ---
    {"word": "cat",    "ipa": "kæt",       "syllables": ["kæt"],         "stress": 0, "category": "short_a", "similar_group": "short_a_1"},
    {"word": "hat",    "ipa": "hæt",       "syllables": ["hæt"],         "stress": 0, "category": "short_a", "similar_group": "short_a_1"},
    {"word": "bat",    "ipa": "bæt",       "syllables": ["bæt"],         "stress": 0, "category": "short_a", "similar_group": "short_a_1"},
    {"word": "man",    "ipa": "mæn",       "syllables": ["mæn"],         "stress": 0, "category": "short_a", "similar_group": "short_a_2"},
    {"word": "can",    "ipa": "kæn",       "syllables": ["kæn"],         "stress": 0, "category": "short_a", "similar_group": "short_a_2"},
    {"word": "map",    "ipa": "mæp",       "syllables": ["mæp"],         "stress": 0, "category": "short_a", "similar_group": "short_a_2"},

    # --- 単母音 a (long: a_e pattern) ---
    {"word": "cake",   "ipa": "keɪk",      "syllables": ["keɪk"],        "stress": 0, "category": "long_a",  "similar_group": "long_a_1"},
    {"word": "make",   "ipa": "meɪk",      "syllables": ["meɪk"],        "stress": 0, "category": "long_a",  "similar_group": "long_a_1"},
    {"word": "name",   "ipa": "neɪm",      "syllables": ["neɪm"],        "stress": 0, "category": "long_a",  "similar_group": "long_a_1"},
    {"word": "late",   "ipa": "leɪt",      "syllables": ["leɪt"],        "stress": 0, "category": "long_a",  "similar_group": "long_a_2"},
    {"word": "fate",   "ipa": "feɪt",      "syllables": ["feɪt"],        "stress": 0, "category": "long_a",  "similar_group": "long_a_2"},

    # --- 単母音 e (short) ---
    {"word": "bed",    "ipa": "bɛd",       "syllables": ["bɛd"],         "stress": 0, "category": "short_e", "similar_group": "short_e_1"},
    {"word": "red",    "ipa": "rɛd",       "syllables": ["rɛd"],         "stress": 0, "category": "short_e", "similar_group": "short_e_1"},
    {"word": "ten",    "ipa": "tɛn",       "syllables": ["tɛn"],         "stress": 0, "category": "short_e", "similar_group": "short_e_1"},
    {"word": "pen",    "ipa": "pɛn",       "syllables": ["pɛn"],         "stress": 0, "category": "short_e", "similar_group": "short_e_2"},
    {"word": "net",    "ipa": "nɛt",       "syllables": ["nɛt"],         "stress": 0, "category": "short_e", "similar_group": "short_e_2"},

    # --- 単母音 i (short) ---
    {"word": "bit",    "ipa": "bɪt",       "syllables": ["bɪt"],         "stress": 0, "category": "short_i", "similar_group": "short_i_1"},
    {"word": "sit",    "ipa": "sɪt",       "syllables": ["sɪt"],         "stress": 0, "category": "short_i", "similar_group": "short_i_1"},
    {"word": "him",    "ipa": "hɪm",       "syllables": ["hɪm"],         "stress": 0, "category": "short_i", "similar_group": "short_i_1"},
    {"word": "ship",   "ipa": "ʃɪp",       "syllables": ["ʃɪp"],         "stress": 0, "category": "short_i", "similar_group": "short_i_2"},
    {"word": "chip",   "ipa": "tʃɪp",      "syllables": ["tʃɪp"],        "stress": 0, "category": "short_i", "similar_group": "short_i_2"},

    # --- 単母音 i (long: i_e / igh pattern) ---
    {"word": "bite",   "ipa": "baɪt",      "syllables": ["baɪt"],        "stress": 0, "category": "long_i",  "similar_group": "long_i_1"},
    {"word": "site",   "ipa": "saɪt",      "syllables": ["saɪt"],        "stress": 0, "category": "long_i",  "similar_group": "long_i_1"},
    {"word": "night",  "ipa": "naɪt",      "syllables": ["naɪt"],        "stress": 0, "category": "long_i",  "similar_group": "long_i_1"},

    # --- 単母音 o (short) ---
    {"word": "hot",    "ipa": "hɑt",       "syllables": ["hɑt"],         "stress": 0, "category": "short_o", "similar_group": "short_o_1"},
    {"word": "not",    "ipa": "nɑt",       "syllables": ["nɑt"],         "stress": 0, "category": "short_o", "similar_group": "short_o_1"},
    {"word": "pot",    "ipa": "pɑt",       "syllables": ["pɑt"],         "stress": 0, "category": "short_o", "similar_group": "short_o_1"},

    # --- 単母音 u (short) ---
    {"word": "cup",    "ipa": "kʌp",       "syllables": ["kʌp"],         "stress": 0, "category": "short_u", "similar_group": "short_u_1"},
    {"word": "bus",    "ipa": "bʌs",       "syllables": ["bʌs"],         "stress": 0, "category": "short_u", "similar_group": "short_u_1"},
    {"word": "run",    "ipa": "rʌn",       "syllables": ["rʌn"],         "stress": 0, "category": "short_u", "similar_group": "short_u_1"},
    {"word": "sun",    "ipa": "sʌn",       "syllables": ["sʌn"],         "stress": 0, "category": "short_u", "similar_group": "short_u_2"},
    {"word": "fun",    "ipa": "fʌn",       "syllables": ["fʌn"],         "stress": 0, "category": "short_u", "similar_group": "short_u_2"},

    # --- 母音重複 ea ---
    {"word": "eat",    "ipa": "iːt",       "syllables": ["iːt"],         "stress": 0, "category": "ea",      "similar_group": "ea_1"},
    {"word": "sea",    "ipa": "siː",       "syllables": ["siː"],         "stress": 0, "category": "ea",      "similar_group": "ea_1"},
    {"word": "read",   "ipa": "riːd",      "syllables": ["riːd"],        "stress": 0, "category": "ea",      "similar_group": "ea_1"},
    {"word": "heat",   "ipa": "hiːt",      "syllables": ["hiːt"],        "stress": 0, "category": "ea",      "similar_group": "ea_2"},
    {"word": "bean",   "ipa": "biːn",      "syllables": ["biːn"],        "stress": 0, "category": "ea",      "similar_group": "ea_2"},
    {"word": "dead",   "ipa": "dɛd",       "syllables": ["dɛd"],         "stress": 0, "category": "ea_exception", "similar_group": "ea_exc_1"},
    {"word": "bread",  "ipa": "brɛd",      "syllables": ["brɛd"],        "stress": 0, "category": "ea_exception", "similar_group": "ea_exc_1"},
    {"word": "head",   "ipa": "hɛd",       "syllables": ["hɛd"],         "stress": 0, "category": "ea_exception", "similar_group": "ea_exc_1"},

    # --- 母音重複 oo ---
    {"word": "food",   "ipa": "fuːd",      "syllables": ["fuːd"],        "stress": 0, "category": "oo_long", "similar_group": "oo_1"},
    {"word": "moon",   "ipa": "muːn",      "syllables": ["muːn"],        "stress": 0, "category": "oo_long", "similar_group": "oo_1"},
    {"word": "cool",   "ipa": "kuːl",      "syllables": ["kuːl"],        "stress": 0, "category": "oo_long", "similar_group": "oo_1"},
    {"word": "book",   "ipa": "bʊk",       "syllables": ["bʊk"],         "stress": 0, "category": "oo_short", "similar_group": "oo_2"},
    {"word": "cook",   "ipa": "kʊk",       "syllables": ["kʊk"],         "stress": 0, "category": "oo_short", "similar_group": "oo_2"},
    {"word": "look",   "ipa": "lʊk",       "syllables": ["lʊk"],         "stress": 0, "category": "oo_short", "similar_group": "oo_2"},

    # --- 母音重複 ou / ow ---
    {"word": "out",    "ipa": "aʊt",       "syllables": ["aʊt"],         "stress": 0, "category": "ou_ow",   "similar_group": "ou_1"},
    {"word": "house",  "ipa": "haʊs",      "syllables": ["haʊs"],        "stress": 0, "category": "ou_ow",   "similar_group": "ou_1"},
    {"word": "now",    "ipa": "naʊ",       "syllables": ["naʊ"],         "stress": 0, "category": "ou_ow",   "similar_group": "ou_1"},
    {"word": "soul",   "ipa": "soʊl",      "syllables": ["soʊl"],        "stress": 0, "category": "ou_ow",   "similar_group": "ou_2"},
    {"word": "low",    "ipa": "loʊ",       "syllables": ["loʊ"],         "stress": 0, "category": "ou_ow",   "similar_group": "ou_2"},

    # --- 母音+r (ar, er, ir, or, ur) ---
    {"word": "car",    "ipa": "kɑːr",      "syllables": ["kɑːr"],        "stress": 0, "category": "ar",      "similar_group": "ar_1"},
    {"word": "farm",   "ipa": "fɑːrm",     "syllables": ["fɑːrm"],       "stress": 0, "category": "ar",      "similar_group": "ar_1"},
    {"word": "star",   "ipa": "stɑːr",     "syllables": ["stɑːr"],       "stress": 0, "category": "ar",      "similar_group": "ar_1"},
    {"word": "her",    "ipa": "hɜːr",      "syllables": ["hɜːr"],        "stress": 0, "category": "er",      "similar_group": "er_1"},
    {"word": "bird",   "ipa": "bɜːrd",     "syllables": ["bɜːrd"],       "stress": 0, "category": "ir",      "similar_group": "er_1"},
    {"word": "word",   "ipa": "wɜːrd",     "syllables": ["wɜːrd"],       "stress": 0, "category": "or",      "similar_group": "er_1"},
    {"word": "for",    "ipa": "fɔːr",      "syllables": ["fɔːr"],        "stress": 0, "category": "or",      "similar_group": "or_1"},
    {"word": "more",   "ipa": "mɔːr",      "syllables": ["mɔːr"],        "stress": 0, "category": "or",      "similar_group": "or_1"},
    {"word": "burn",   "ipa": "bɜːrn",     "syllables": ["bɜːrn"],       "stress": 0, "category": "ur",      "similar_group": "er_1"},

    # --- シュワー（強勢なし音節） ---
    {"word": "about",  "ipa": "əˈbaʊt",    "syllables": ["ə", "baʊt"],   "stress": 1, "category": "schwa",   "similar_group": "schwa_1"},
    {"word": "ago",    "ipa": "əˈɡoʊ",     "syllables": ["ə", "ɡoʊ"],    "stress": 1, "category": "schwa",   "similar_group": "schwa_1"},
    {"word": "sofa",   "ipa": "ˈsoʊfə",    "syllables": ["soʊ", "fə"],   "stress": 0, "category": "schwa",   "similar_group": "schwa_2"},
    {"word": "button", "ipa": "ˈbʌtən",    "syllables": ["bʌt", "ən"],   "stress": 0, "category": "schwa",   "similar_group": "schwa_2"},
    {"word": "lesson", "ipa": "ˈlɛsən",    "syllables": ["lɛs", "ən"],   "stress": 0, "category": "schwa",   "similar_group": "schwa_2"},
    {"word": "garden", "ipa": "ˈɡɑːrdən",  "syllables": ["ɡɑːrd", "ən"], "stress": 0, "category": "schwa",   "similar_group": "schwa_3"},
    {"word": "open",   "ipa": "ˈoʊpən",    "syllables": ["oʊp", "ən"],   "stress": 0, "category": "schwa",   "similar_group": "schwa_3"},

    # --- 多音節語（アクセント練習） ---
    {"word": "table",      "ipa": "ˈteɪbəl",     "syllables": ["teɪ", "bəl"],        "stress": 0, "category": "schwa",   "similar_group": "stress_2syl"},
    {"word": "window",     "ipa": "ˈwɪndoʊ",     "syllables": ["wɪn", "doʊ"],       "stress": 0, "category": "ou_ow",   "similar_group": "stress_2syl"},
    {"word": "water",      "ipa": "ˈwɔːtər",     "syllables": ["wɔː", "tər"],       "stress": 0, "category": "or",      "similar_group": "stress_2syl"},
    {"word": "computer",   "ipa": "kəmˈpjuːtər",  "syllables": ["kəm", "pjuː", "tər"], "stress": 1, "category": "schwa",   "similar_group": "stress_3syl"},
    {"word": "banana",     "ipa": "bəˈnænə",     "syllables": ["bə", "næn", "ə"],    "stress": 1, "category": "schwa",   "similar_group": "stress_3syl"},
    {"word": "important",  "ipa": "ɪmˈpɔːrtənt",  "syllables": ["ɪm", "pɔːrt", "ənt"], "stress": 1, "category": "or",      "similar_group": "stress_3syl"},
    {"word": "beautiful",  "ipa": "ˈbjuːtɪfəl",  "syllables": ["bjuː", "tɪ", "fəl"],  "stress": 0, "category": "schwa",   "similar_group": "stress_3syl"},
    {"word": "education",  "ipa": "ˌɛdʒʊˈkeɪʃən", "syllables": ["ɛdʒ", "ʊ", "keɪ", "ʃən"], "stress": 2, "category": "long_a", "similar_group": "stress_4syl"},
    {"word": "information", "ipa": "ˌɪnfərˈmeɪʃən", "syllables": ["ɪn", "fər", "meɪ", "ʃən"], "stress": 2, "category": "long_a", "similar_group": "stress_4syl"},
]

# similar_group が同じ単語はCの選択肢候補として使われる（発音が似ているため引っかかりやすい）
