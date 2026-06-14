# PhonIQ - 理論データ
# Phase 1: 発音記号・つながりパターンの学習コンテンツ

# ===== Layer A: 文字のつながりから学ぶ層 =====
# YouTube再生リストの分類を参考に構成

SPELLING_CATEGORIES = [
    {
        "id": "single_vowels",
        "title": "単独母音の発音",
        "description": "a, e, i, o, u それぞれの基本発音を学びます。短母音と長母音の違いが英語発音の核心です。",
        "icon": "🔤",
        "rules": [
            {
                "letter": "a",
                "sound_short": "æ（キャット の a）",
                "sound_long": "eɪ（ケーキ の a）",
                "rule": "子音+a+子音 → 短母音 /æ/ \n子音+a+子音+e（マジックe）→ 長母音 /eɪ/",
                "examples_short": [
                    {"word": "cat",  "ipa": "kæt"},
                    {"word": "hat",  "ipa": "hæt"},
                    {"word": "man",  "ipa": "mæn"},
                    {"word": "map",  "ipa": "mæp"}
                ],
                "examples_long": [
                    {"word": "cake", "ipa": "keɪk"},
                    {"word": "name", "ipa": "neɪm"},
                    {"word": "late", "ipa": "leɪt"}
                ],
                "exceptions": [
                    {"word": "want",  "ipa": "wɑnt",  "note": "w の後の a は /ɑ/ になることが多い"},
                    {"word": "was",   "ipa": "wɑz",   "note": "w の後の a は /ɑ/ になることが多い"},
                    {"word": "water", "ipa": "ˈwɔːtər", "note": "w の後の a は /ɔː/ になることも"}
                ]
            },
            {
                "letter": "e",
                "sound_short": "ɛ（ベッド の e）",
                "sound_long": "iː（ミー の ee と同じ感覚）",
                "rule": "子音+e+子音 → 短母音 /ɛ/ \n子音+e（語末）→ 発音しない（マジックe の e 自体は無音）",
                "examples_short": [
                    {"word": "bed",  "ipa": "bɛd"},
                    {"word": "red",  "ipa": "rɛd"},
                    {"word": "ten",  "ipa": "tɛn"}
                ],
                "examples_long": [
                    {"word": "be",   "ipa": "biː"},
                    {"word": "she",  "ipa": "ʃiː"},
                    {"word": "me",   "ipa": "miː"}
                ],
                "exceptions": [
                    {"word": "the",  "ipa": "ðə / ðiː", "note": "弱形はシュワー /ə/、母音前では /ðiː/"}
                ]
            },
            {
                "letter": "i",
                "sound_short": "ɪ（ビット の i）",
                "sound_long": "aɪ（バイト の i）",
                "rule": "子音+i+子音 → 短母音 /ɪ/ \n子音+i+子音+e → 長母音 /aɪ/",
                "examples_short": [
                    {"word": "bit",  "ipa": "bɪt"},
                    {"word": "sit",  "ipa": "sɪt"},
                    {"word": "ship", "ipa": "ʃɪp"}
                ],
                "examples_long": [
                    {"word": "bite",  "ipa": "baɪt"},
                    {"word": "site",  "ipa": "saɪt"},
                    {"word": "night", "ipa": "naɪt"}
                ],
                "exceptions": [
                    {"word": "ski",    "ipa": "skiː",  "note": "語末の i が /iː/ になる外来語"},
                    {"word": "machine", "ipa": "məˈʃiːn", "note": "フランス語由来: i → /iː/"}
                ]
            },
            {
                "letter": "o",
                "sound_short": "ɑ（ハット の a に近い）",
                "sound_long": "oʊ（ゴー の o）",
                "rule": "子音+o+子音 → 短母音 /ɑ/ \n子音+o+子音+e → 長母音 /oʊ/",
                "examples_short": [
                    {"word": "hot",  "ipa": "hɑt"},
                    {"word": "not",  "ipa": "nɑt"},
                    {"word": "pot",  "ipa": "pɑt"}
                ],
                "examples_long": [
                    {"word": "home", "ipa": "hoʊm"},
                    {"word": "note", "ipa": "noʊt"},
                    {"word": "rope", "ipa": "roʊp"}
                ],
                "exceptions": [
                    {"word": "do",   "ipa": "duː",  "note": "語末 o が /uː/ になる高頻度語"},
                    {"word": "who",  "ipa": "huː",  "note": "who の o は /uː/"},
                    {"word": "women", "ipa": "ˈwɪmɪn", "note": "o が /ɪ/ という特殊な例外"}
                ]
            },
            {
                "letter": "u",
                "sound_short": "ʌ（カップ の u）",
                "sound_long": "juː（ユー）",
                "rule": "子音+u+子音 → 短母音 /ʌ/ \n子音+u+子音+e → 長母音 /juː/ または /uː/",
                "examples_short": [
                    {"word": "cup",  "ipa": "kʌp"},
                    {"word": "bus",  "ipa": "bʌs"},
                    {"word": "run",  "ipa": "rʌn"}
                ],
                "examples_long": [
                    {"word": "cute",  "ipa": "kjuːt"},
                    {"word": "mule",  "ipa": "mjuːl"},
                    {"word": "rule",  "ipa": "ruːl"}
                ],
                "exceptions": [
                    {"word": "put",  "ipa": "pʊt",  "note": "u が /ʊ/ になる高頻度語"},
                    {"word": "full",  "ipa": "fʊl",  "note": "u が /ʊ/ になる高頻度語"},
                    {"word": "bull",  "ipa": "bʊl",  "note": "u が /ʊ/ になる高頻度語"}
                ]
            }
        ]
    },
    {
        "id": "vowel_combinations",
        "title": "母音が重なる時の発音",
        "description": "ea, ee, oo, ou など2つの母音が並んだ時の読み方を学びます。法則を覚えると一気にスペルから発音が予測できるようになります。",
        "icon": "🔗",
        "rules": [
            {
                "pattern": "ea",
                "rule": "原則として /iː/（長い ee の音）",
                "examples_rule": [
                    {"word": "eat",   "ipa": "iːt"},
                    {"word": "sea",   "ipa": "siː"},
                    {"word": "read",  "ipa": "riːd"},
                    {"word": "bean",  "ipa": "biːn"}
                ],
                "exceptions": [
                    {"word": "dead",  "ipa": "dɛd",  "note": "ea → /ɛ/（短い e）"},
                    {"word": "bread", "ipa": "brɛd", "note": "ea → /ɛ/（短い e）"},
                    {"word": "head",  "ipa": "hɛd",  "note": "ea → /ɛ/（短い e）"},
                    {"word": "great", "ipa": "ɡreɪt", "note": "ea → /eɪ/ という珍しいパターン"}
                ]
            },
            {
                "pattern": "ee",
                "rule": "常に /iː/（例外ほぼなし）",
                "examples_rule": [
                    {"word": "see",   "ipa": "siː"},
                    {"word": "tree",  "ipa": "triː"},
                    {"word": "feet",  "ipa": "fiːt"},
                    {"word": "green", "ipa": "ɡriːn"}
                ],
                "exceptions": []
            },
            {
                "pattern": "oo",
                "rule": "長音 /uː/（food）か短音 /ʊ/（book）の2パターン",
                "examples_rule": [
                    {"word": "food",  "ipa": "fuːd",  "note": "長音"},
                    {"word": "moon",  "ipa": "muːn",  "note": "長音"},
                    {"word": "book",  "ipa": "bʊk",   "note": "短音"},
                    {"word": "look",  "ipa": "lʊk",   "note": "短音"}
                ],
                "exceptions": [
                    {"word": "blood", "ipa": "blʌd", "note": "oo → /ʌ/ という例外"},
                    {"word": "flood", "ipa": "flʌd", "note": "oo → /ʌ/ という例外"}
                ]
            },
            {
                "pattern": "ou / ow",
                "rule": "二重母音 /aʊ/（house, now）または長音 /oʊ/（soul, low）",
                "examples_rule": [
                    {"word": "out",   "ipa": "aʊt",   "note": "/aʊ/"},
                    {"word": "house", "ipa": "haʊs",  "note": "/aʊ/"},
                    {"word": "now",   "ipa": "naʊ",   "note": "/aʊ/"},
                    {"word": "low",   "ipa": "loʊ",   "note": "/oʊ/"},
                    {"word": "soul",  "ipa": "soʊl",  "note": "/oʊ/"}
                ],
                "exceptions": [
                    {"word": "could", "ipa": "kʊd", "note": "ou → /ʊ/（could, would, should）"},
                    {"word": "four",  "ipa": "fɔːr", "note": "ou → /ɔː/"}
                ]
            },
            {
                "pattern": "ai / ay",
                "rule": "常に /eɪ/（二重母音）",
                "examples_rule": [
                    {"word": "rain",  "ipa": "reɪn"},
                    {"word": "wait",  "ipa": "weɪt"},
                    {"word": "day",   "ipa": "deɪ"},
                    {"word": "say",   "ipa": "seɪ"}
                ],
                "exceptions": [
                    {"word": "said",  "ipa": "sɛd",  "note": "ai → /ɛ/ という重要な例外"}
                ]
            }
        ]
    },
    {
        "id": "vowel_r",
        "title": "母音 + r の組み合わせ",
        "description": "英語では母音の後に r が来ると、その母音の音が変わります（R-colored vowels）。アメリカ英語では特に重要なパターンです。",
        "icon": "🌀",
        "rules": [
            {
                "pattern": "ar",
                "sound": "ɑːr",
                "rule": "ar → /ɑːr/（car の ar）",
                "examples_rule": [
                    {"word": "car",  "ipa": "kɑːr"},
                    {"word": "farm", "ipa": "fɑːrm"},
                    {"word": "star", "ipa": "stɑːr"},
                    {"word": "hard", "ipa": "hɑːrd"}
                ],
                "exceptions": [
                    {"word": "warm",  "ipa": "wɔːrm", "note": "w の後の ar は /ɔːr/"},
                    {"word": "war",   "ipa": "wɔːr",  "note": "w の後の ar は /ɔːr/"}
                ]
            },
            {
                "pattern": "er / ir / ur",
                "sound": "ɜːr",
                "rule": "er, ir, ur はすべて同じ /ɜːr/ の音（アメリカ英語）",
                "examples_rule": [
                    {"word": "her",  "ipa": "hɜːr",  "note": "er"},
                    {"word": "bird", "ipa": "bɜːrd", "note": "ir"},
                    {"word": "burn", "ipa": "bɜːrn", "note": "ur"},
                    {"word": "word", "ipa": "wɜːrd", "note": "or（特殊）"}
                ],
                "exceptions": [
                    {"word": "were", "ipa": "wɜːr",  "note": "過去形 were も同じ音"},
                    {"word": "iron", "ipa": "ˈaɪərn", "note": "ir が二重母音になる例"}
                ]
            },
            {
                "pattern": "or",
                "sound": "ɔːr",
                "rule": "or → /ɔːr/（force の or）",
                "examples_rule": [
                    {"word": "for",  "ipa": "fɔːr"},
                    {"word": "more", "ipa": "mɔːr"},
                    {"word": "corn", "ipa": "kɔːrn"},
                    {"word": "sport", "ipa": "spɔːrt"}
                ],
                "exceptions": [
                    {"word": "word",  "ipa": "wɜːrd", "note": "w の後の or は /ɜːr/"},
                    {"word": "world", "ipa": "wɜːrld", "note": "w の後の or は /ɜːr/"}
                ]
            }
        ]
    },
    {
        "id": "schwa",
        "title": "アクセントのない音節（シュワー）",
        "description": "英語最頻出の音・シュワー /ə/ を学びます。アクセントがない音節ではどの母音も /ə/ に近い「あいまい母音」になります。これを知るとリスニングが劇的に向上します。",
        "icon": "😌",
        "rules": [
            {
                "pattern": "語頭の弱い音節（a-, e-, o-, ...）",
                "sound": "ə",
                "rule": "アクセントのない語頭の母音はシュワー /ə/ になりやすい",
                "examples_rule": [
                    {"word": "about",  "ipa": "əˈbaʊt",  "note": "a → /ə/"},
                    {"word": "ago",    "ipa": "əˈɡoʊ",   "note": "a → /ə/"},
                    {"word": "along",  "ipa": "əˈlɔːŋ",  "note": "a → /ə/"}
                ],
                "exceptions": []
            },
            {
                "pattern": "語末の -er, -or, -ar（非アクセント）",
                "sound": "ər",
                "rule": "アクセントのない語末の -er/-or/-ar はすべて /ər/ になる",
                "examples_rule": [
                    {"word": "teacher",  "ipa": "ˈtiːtʃər",  "note": "-er → /ər/"},
                    {"word": "doctor",   "ipa": "ˈdɑktər",   "note": "-or → /ər/"},
                    {"word": "dollar",   "ipa": "ˈdɑlər",    "note": "-ar → /ər/"}
                ],
                "exceptions": []
            },
            {
                "pattern": "語末の -on, -en, -an（非アクセント）",
                "sound": "ən",
                "rule": "アクセントのない -on/-en/-an は /ən/ になる",
                "examples_rule": [
                    {"word": "button", "ipa": "ˈbʌtən", "note": "-on → /ən/"},
                    {"word": "lesson", "ipa": "ˈlɛsən", "note": "-on → /ən/"},
                    {"word": "open",   "ipa": "ˈoʊpən", "note": "-en → /ən/"},
                    {"word": "garden", "ipa": "ˈɡɑːrdən", "note": "-en → /ən/"}
                ],
                "exceptions": []
            }
        ]
    }
]


# ===== Layer B: 発音記号から学ぶ層 =====
# IPA 記号の分類と解説

IPA_SYMBOLS = {
    "why_ipa": {
        "title": "発音記号を学ぶ意義",
        "points": [
            {
                "title": "初見の単語の発音がすぐわかる",
                "detail": "英語の最大の難点の一つは、スペルと発音が一致しないことです。たとえば 'read' は現在形では /riːd/、過去形では /rɛd/ と読み、スペルだけでは判断できません。発音記号を知っていれば、辞書を引いた瞬間に正確な音がわかります。",
                "icon": "📖"
            },
            {
                "title": "音で単語を覚えられる",
                "detail": "単語を視覚（スペル）だけで暗記すると、リスニングで聞いた音と結びつきにくくなります。発音記号を使って音のイメージと一緒に覚えると、スピーキングでもリスニングでも自然に使えるようになります。",
                "icon": "🎧"
            },
            {
                "title": "他の言語にも応用できる",
                "detail": "IPA（国際音声記号）は英語だけでなく、フランス語・スペイン語・中国語・日本語など世界中の言語の発音を表記するために使われます。一度 IPA を習得すれば、どの言語の辞書でも発音を読み取れるようになります。",
                "icon": "🌍"
            },
            {
                "title": "ネイティブに近い発音に近づく",
                "detail": "日本語にない音（/θ/, /ð/, /æ/, /ɪ/ など）は、カタカナで覚えるだけでは再現できません。発音記号で口の形・舌の位置を意識することで、より正確な英語の音が身につきます。",
                "icon": "🗣️"
            },
            {
                "title": "発音とスペルのパターンが見えてくる",
                "detail": "英語のスペルと発音には複雑なルールがありますが、発音記号を介することで規則性が見えやすくなります。たとえば 'ea' というつながりが /iː/ になるのか /ɛ/ になるのかが、IPA 表記を通じて整理できます。",
                "icon": "🔍"
            }
        ]
    },
    "categories": [
        {
            "id": "vowels_short",
            "title": "短母音",
            "color": "#4A90D9",
            "symbols": [
                {"symbol": "æ",  "name": "ash",       "japanese": "ア（口を横に広げる）", "example_word": "cat",  "example_ipa": "kæt",  "tongue": "前舌・低", "lips": "横に開く",   "tips": "日本語の『ア』より口を横に大きく引いて発音"},
                {"symbol": "ɛ",  "name": "epsilon",   "japanese": "エ",               "example_word": "bed",  "example_ipa": "bɛd",  "tongue": "前舌・中低", "lips": "やや開く",  "tips": "日本語の『エ』に近いが、口をもう少し開く"},
                {"symbol": "ɪ",  "name": "small cap I", "japanese": "イ（短く弱く）",  "example_word": "bit",  "example_ipa": "bɪt",  "tongue": "前舌・高", "lips": "やや狭める", "tips": "日本語の『イ』を短く力を抜いて発音"},
                {"symbol": "ɑ",  "name": "script a",  "japanese": "アー（のどを開く）", "example_word": "hot",  "example_ipa": "hɑt",  "tongue": "後舌・低", "lips": "大きく開く", "tips": "口を大きく開けて、のどの奥から出す音"},
                {"symbol": "ɔ",  "name": "open O",    "japanese": "オー（丸く開く）",  "example_word": "law",  "example_ipa": "lɔː",  "tongue": "後舌・中低", "lips": "丸く開く",  "tips": "日本語の『オ』より口を丸く大きく開く"},
                {"symbol": "ʊ",  "name": "upsilon",  "japanese": "ウ（短く弱く）",   "example_word": "book", "example_ipa": "bʊk",  "tongue": "後舌・高", "lips": "丸める",    "tips": "日本語の『ウ』を短く力を抜いて"},
                {"symbol": "ʌ",  "name": "wedge",     "japanese": "ア（中央で弱く）",  "example_word": "cup",  "example_ipa": "kʌp",  "tongue": "中舌・中", "lips": "やや開く",  "tips": "『ア』と『オ』の中間。力を抜いて中央で発音"},
                {"symbol": "ə",  "name": "schwa",     "japanese": "ア（あいまい）",   "example_word": "about", "example_ipa": "əˈbaʊt", "tongue": "中舌・中", "lips": "自然に",   "tips": "最もよく出てくる音。アクセントのない音節で力を抜いて"}
            ]
        },
        {
            "id": "vowels_long",
            "title": "長母音・二重母音",
            "color": "#E67E22",
            "symbols": [
                {"symbol": "iː", "name": "long I",    "japanese": "イー（長く強く）",  "example_word": "see",  "example_ipa": "siː",  "tongue": "前舌・高", "lips": "横に引く",  "tips": "日本語の『イ』を長く、唇を強く横に引いて"},
                {"symbol": "uː", "name": "long U",    "japanese": "ウー（長く丸く）",  "example_word": "food", "example_ipa": "fuːd", "tongue": "後舌・高", "lips": "丸く前に出す", "tips": "唇を前に突き出して強く丸めて発音"},
                {"symbol": "ɔː", "name": "long O",    "japanese": "オー（長く）",      "example_word": "law",  "example_ipa": "lɔː",  "tongue": "後舌・中低", "lips": "丸く開く", "tips": "口を丸く大きく開けたまま長く"},
                {"symbol": "ɑː", "name": "long A",    "japanese": "アー（長く）",      "example_word": "car",  "example_ipa": "kɑːr", "tongue": "後舌・低", "lips": "大きく開く", "tips": "のどを大きく開けて長く発音"},
                {"symbol": "eɪ", "name": "diphthong", "japanese": "エイ（二重母音）",  "example_word": "cake", "example_ipa": "keɪk", "tongue": "前舌・動く", "lips": "動かす",  "tips": "/e/ から /ɪ/ へ口を動かしながら"},
                {"symbol": "aɪ", "name": "diphthong", "japanese": "アイ（二重母音）",  "example_word": "bite", "example_ipa": "baɪt", "tongue": "低→高",   "lips": "開→閉",   "tips": "口を大きく開けた『ア』から素早く『イ』へ"},
                {"symbol": "aʊ", "name": "diphthong", "japanese": "アウ（二重母音）",  "example_word": "out",  "example_ipa": "aʊt",  "tongue": "低→高後", "lips": "開→丸",   "tips": "『ア』から素早く唇を丸めて『ウ』へ"},
                {"symbol": "oʊ", "name": "diphthong", "japanese": "オウ（二重母音）",  "example_word": "go",   "example_ipa": "ɡoʊ",  "tongue": "後舌・動く", "lips": "丸→すぼめ", "tips": "『オ』から素早く唇をすぼめて『ウ』へ"}
            ]
        },
        {
            "id": "consonants_key",
            "title": "重要子音",
            "color": "#27AE60",
            "symbols": [
                {"symbol": "θ",  "name": "theta",     "japanese": "ス（舌先を歯の間に）",  "example_word": "think", "example_ipa": "θɪŋk", "tongue": "歯間",    "lips": "自然に",   "tips": "舌先を上下の歯の間に軽く挟んで息を出す"},
                {"symbol": "ð",  "name": "eth",       "japanese": "ズ（舌先を歯の間に）",  "example_word": "the",  "example_ipa": "ðə",   "tongue": "歯間",    "lips": "自然に",   "tips": "/θ/ と同じ口の形で声帯を震わせる"},
                {"symbol": "ʃ",  "name": "esh",       "japanese": "シュ",               "example_word": "she",  "example_ipa": "ʃiː",  "tongue": "口蓋寄り", "lips": "丸める",  "tips": "日本語の『シュ』に近いが唇をより丸める"},
                {"symbol": "ʒ",  "name": "ezh",       "japanese": "ジュ（有声）",        "example_word": "vision", "example_ipa": "ˈvɪʒən", "tongue": "口蓋寄り", "lips": "丸める", "tips": "/ʃ/ と同じ口の形で声帯を震わせる"},
                {"symbol": "tʃ", "name": "affricate", "japanese": "チュ",               "example_word": "chip",  "example_ipa": "tʃɪp",  "tongue": "口蓋",    "lips": "丸める",  "tips": "日本語の『チ』に近い"},
                {"symbol": "dʒ", "name": "affricate", "japanese": "ヂュ（有声）",        "example_word": "job",   "example_ipa": "dʒɑb",  "tongue": "口蓋",    "lips": "丸める",  "tips": "日本語の『ジ』に近い"},
                {"symbol": "ŋ",  "name": "eng",       "japanese": "ング（語末のn）",     "example_word": "sing",  "example_ipa": "sɪŋ",   "tongue": "軟口蓋",  "lips": "自然に",  "tips": "日本語の『ング』の鼻音だけ。口を開かずに鼻から音を出す"},
                {"symbol": "v",  "name": "vee",       "japanese": "ヴ（唇に歯を当てる）", "example_word": "very",  "example_ipa": "ˈvɛri", "tongue": "自由",    "lips": "上の歯を下唇に当てる", "tips": "上の歯を下唇に軽く当てて声を出す（/b/ と混同しないこと）"}
            ]
        },
        {
            "id": "r_colored",
            "title": "R性母音",
            "color": "#8E44AD",
            "symbols": [
                {"symbol": "ɜːr", "name": "r-colored mid central", "japanese": "アー（r音化）", "example_word": "bird", "example_ipa": "bɜːrd", "tongue": "中舌・反り上げ", "lips": "やや丸める", "tips": "舌先を反り上げながら、のどの奥で唸るような音"},
                {"symbol": "ər",  "name": "r-colored schwa",       "japanese": "ア（弱いr）",   "example_word": "teacher", "example_ipa": "ˈtiːtʃər", "tongue": "中舌・弱く反る", "lips": "自然に", "tips": "アクセントのない音節でのr音化シュワー"}
            ]
        }
    ]
}
