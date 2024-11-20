import os
import fasttext
import langid
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException
import stanza
from googletrans import Translator
import pronouncing
import sqlite3

# 设置语言检测的确定性
DetectorFactory.seed = 0

# 下载并加载德语模型
stanza.download('de')
nlp = stanza.Pipeline('de')

# 检查fasttext模型文件路径
model_path = 'lid.176.bin'
if not os.path.isfile(model_path):
    print(f"模型文件 {model_path} 不存在，请检查路径。")
    model = None
else:
    try:
        model = fasttext.load_model(model_path)
    except ValueError as e:
        print(f"FastText模型加载失败: {e}")
        model = None

# 初始化翻译器
translator = Translator()

# 创建或连接数据库
conn = sqlite3.connect('german_pronunciation.db')
cursor = conn.cursor()

# 创建表
cursor.execute('''
CREATE TABLE IF NOT EXISTS Pronunciation (
    word TEXT PRIMARY KEY,
    german_ipa TEXT,
    english_ipa TEXT
)
''')
conn.commit()

# 语言代码与语言名称的映射
language_dict = {
    'ko': '韩语',
    'ja': '日语',
    'en': '英语',
    'zh-cn': '中文',
    'de': '德语',
    'la': '拉丁语',
    'eo': '世界语',
    'fr': '法语',
    'el': '希腊语',
    'grc': '古希腊语',
    'ltz': '古拉丁语'
}

def detect_language(text):
    detection_results = {}

    try:
        detected_lang, confidence = langid.classify(text)
        detection_results['langid'] = (language_dict.get(detected_lang, '未知语言'), abs(confidence))
    except Exception as e:
        print(f"LangID检测失败: {e}")
        detection_results['langid'] = ('未知语言', '无')

    try:
        detected_lang = detect(text)
        detection_results['langdetect'] = (language_dict.get(detected_lang, '未知语言'), '高')
    except LangDetectException:
        detection_results['langdetect'] = ('未知语言', '无')

    if model:
        try:
            fasttext_result = model.predict(text)
            detected_lang = fasttext_result[0][0].split("__label__")[1]
            detection_results['fasttext'] = (language_dict.get(detected_lang, '未知语言'), abs(fasttext_result[1][0]))
        except Exception as e:
            print(f"FastText检测失败: {e}")
            detection_results['fasttext'] = ('未知语言', '无')
    else:
        detection_results['fasttext'] = ('未知语言', '无')

    return detection_results

def replace_unknown_languages(detection_results):
    if not detection_results:
        return detection_results

    known_languages = {lang for method, (lang, _) in detection_results.items() if lang != '未知语言'}
    if not known_languages:
        return detection_results

    for method in detection_results:
        if detection_results[method][0] == '未知语言':
            for known_lang in known_languages:
                detection_results[method] = (known_lang, '交叉验证替代')
                break

    return detection_results

def aggregate_detection_results(results):
    if not results:
        return '未知语言'

    lang_counts = {}
    weighted_counts = {}

    for method, (lang, confidence) in results.items():
        if lang != '未知语言':
            if lang not in lang_counts:
                lang_counts[lang] = 0
            lang_counts[lang] += 1

            if lang not in weighted_counts:
                weighted_counts[lang] = 0
            try:
                confidence_score = float(confidence) if confidence != '无' else 0
                weighted_counts[lang] += confidence_score
            except ValueError:
                continue

    if weighted_counts:
        most_common_lang = max(weighted_counts, key=weighted_counts.get)
    elif lang_counts:
        most_common_lang = max(lang_counts, key=lang_counts.get)
    else:
        most_common_lang = '未知语言'

    return most_common_lang

# 定义词性标签和对应的中文说明
pos_labels = {
    'ADJ': '形容词',
    'ADP': '介词',
    'ADV': '副词',
    'AUX': '助动词',
    'CONJ': '连词',
    'CCONJ': '并列连词',
    'DET': '限定词',
    'INTJ': '感叹词',
    'NOUN': '名词',
    'NUM': '数词',
    'PART': '小品词',
    'PRON': '代词',
    'PROPN': '专有名词',
    'PUNCT': '标点符号',
    'SCONJ': '从属连词',
    'SYM': '符号',
    'VERB': '动词',
    'X': '其他'
}

# 德语音标规则（不包括具体单词）
german_ipa_rules = {
    'a': 'a', 'ä': 'ɛ', 'e': 'e', 'i': 'i', 'o': 'o', 'ö': 'ø', 'u': 'u', 'ü': 'y',
    'ch': 'ç', 'sch': 'ʃ', 'ei': 'aɪ', 'ie': 'iː', 'au': 'aʊ', 'eu': 'ɔʏ'
}

# 更全面的德语国际音标(包括具体单词)
german_ipa_dict = {
    'Der': 'deːr', 'Shincho': 'ʃɪnʧo', 'Bunko': 'bʊnko', 'Verlag': 'fɛrlaːk',
    'in': 'ɪn', 'Japan': 'japaːn', 'veröffentlicht': 'fɛʁˈʔœfnɪçt', 'den': 'deːn',
    'Roman': 'roːman', 'The': 'ðə', 'Dizzy': 'dɪzi', 'Man': 'mæn',
    'berühmten': 'bəˈʁyːmtn̩', 'japanischen': 'japaːnɪʃən', 'Autorin': 'aʊˈtoːʁɪn',
    'Sawako': 'zaːʋako', 'Ariyoshi': 'aʁiˈjoːʃi', 'Dieser': 'diːzəʁ',
    'Altenpflege': 'ʔaltənˌpfleːɡə', 'beschreibt': 'bəˈʃʁaɪ̯pt', 'von': 'fɔn',
    'dem': 'deːm', 'renommierten': 'ʁenoˈmiːʁtn̩', 'Regisseur': 'ʁeˈɡɪsøːɐ̯',
    'Shiro': 'ʃiːʁo', 'Tani': 'taːni', 'verfilmt': 'fɛɐ̯ˈfɪlmt', 'Es': 'ɛs',
    'war': 'vaːʁ', 'dieser': 'diːzəʁ', 'Sozial': 'zoˈtsi̯aːl', 'und': 'ʊnt',
    'Altenpflegepolitik': 'ʔaltənˌpfleːɡəˈpoːliˌtiːk', 'Regierung': 'ʁeˈɡiːʁʊŋ',
    'für': 'fyːɐ̯', 'ihre': 'ˈiːʁə', 'Bürger': 'ˈbʏʁɡɐ', 'veränderte': 'fɛɐ̯ˈʔɛndɐtə',
    'zivilisiert': 'tsiˈviˌliːziːɐ̯t', 'eine': 'ˈaɪ̯nə', 'sein': 'zaɪ̯n',
    'wenn': 'vɛn', 'Politik': 'poˈliːtiːk', 'durch': 'dʊʁç', 'einen': 'ˈaɪ̯nen', 
    'werden': 'ˈveːɐ̯dn̩', 'kann': 'kan', 'Die': 'diː', 'heutige': 'ˈhɔʏ̯tɪɡə',
    'führt': 'fyːɐ̯t', 'Menschheit': 'ˈmɛnʃˌhaɪ̯t', 'Richtung': 'ˈʁɪçtuŋ',
    'größerer': 'ˈɡʁøːsəʁɐ', 'Zivilisation': 'tsiˈviˌliˈzaːt͡si̯oːn'
}

# 使用ARPAbet到IPA的转换表
arpabet_to_ipa_dict = {
    'AA': 'ɑ', 'AE': 'æ', 'AH': 'ʌ', 'AO': 'ɔ', 'AW': 'aʊ', 'AY': 'aɪ',
    'B': 'b', 'CH': 'tʃ', 'D': 'd', 'DH': 'ð', 'EH': 'ɛ', 'ER': 'ɝ',
    'EY': 'eɪ', 'F': 'f', 'G': 'ɡ', 'HH': 'h', 'IH': 'ɪ', 'IY': 'i',
    'JH': 'dʒ', 'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'NG': 'ŋ',
    'OW': 'oʊ', 'OY': 'ɔɪ', 'P': 'p', 'R': 'ɹ', 'S': 's', 'SH': 'ʃ',
    'T': 't', 'TH': 'θ', 'UH': 'ʊ', 'UW': 'u', 'V': 'v', 'W': 'w',
    'Y': 'j', 'Z': 'z', 'ZH': 'ʒ'
}

# 德语音标到英式音标的转换规则（根据德语音标拼写规则模拟英式音标）
german_to_english_ipa_dict = {
    'a': 'ɑ', 'ɛ': 'e', 'e': 'e', 'i': 'ɪ', 'o': 'o', 'ø': 'ɜː', 'u': 'ʊ', 'y': 'ʏ',
    'ç': 'ʃ', 'ʃ': 'ʃ', 'aɪ': 'aɪ', 'iː': 'iː', 'aʊ': 'aʊ', 'ɔʏ': 'ɔɪ'
}

def arpabet_to_ipa(arpabet):
    ipa = []
    for phone in arpabet.split():
        phone = ''.join([char for char in phone if not char.isdigit()])  # 移除数字
        if phone in arpabet_to_ipa_dict:
            ipa.append(arpabet_to_ipa_dict[phone])
        else:
            ipa.append(phone)
    return ''.join(ipa)

def get_english_pronunciation(word):
    # 将德语单词直接传给 pronouncing 库进行拼读
    pronunciations = pronouncing.phones_for_word(word)
    if not pronunciations:
        return '[无拼音]'

    ipa = arpabet_to_ipa(pronunciations[0]) if pronunciations else '[无拼音]'
    return ipa

def convert_german_to_english_ipa(german_ipa):
    english_ipa = []
    i = 0
    while i < len(german_ipa):
        if i + 1 < len(german_ipa) and german_ipa[i:i+2] in german_to_english_ipa_dict:
            english_ipa.append(german_to_english_ipa_dict[german_ipa[i:i+2]])
            i += 2
        elif german_ipa[i] in german_to_english_ipa_dict:
            english_ipa.append(german_to_english_ipa_dict[german_ipa[i]])
            i += 1
        else:
            english_ipa.append(german_ipa[i])
            i += 1
    return ''.join(english_ipa)

def save_pronunciation_to_db(word, german_ipa, english_ipa):
    cursor.execute('''
    INSERT OR REPLACE INTO Pronunciation (word, german_ipa, english_ipa)
    VALUES (?, ?, ?)
    ''', (word, german_ipa, english_ipa))
    conn.commit()

def pos_tagging(text):
    doc = nlp(text)

    for sentence in doc.sentences:
        for word in sentence.words:
            pos_chinese = pos_labels.get(word.upos, '标点/未知词性')
            translation = translator.translate(word.text, src='de', dest='zh-cn').text

            # 获取德语和英语音标
            german_ipa = german_ipa_dict.get(word.text, '[手动添加德语音标]')
            if german_ipa == '[手动添加德语音标]':
                german_ipa = get_german_ipa(word.text)
            
            if german_ipa != '[手动添加德语音标]':
                english_ipa = convert_german_to_english_ipa(german_ipa)
            else:
                english_ipa = '[手动添加英式音标]'

            # 检查并替换 [N/A]
            if german_ipa == '[手动添加德语音标]' or english_ipa == '[无拼音]':
                if german_ipa == '[手动添加德语音标]':
                    german_ipa = '[手动添加德语音标]'
                if english_ipa == '[无拼音]':
                    english_ipa = '[手动添加英式音标]'

            # 存储到数据库
            save_pronunciation_to_db(word.text, german_ipa, english_ipa)

            # 打印结果
            print(f"{word.text}: {word.upos} ({pos_chinese}) - {translation} - [{german_ipa}] [{english_ipa}]")

def get_german_ipa(word):
    if word in german_ipa_dict:
        return german_ipa_dict[word]
    
    ipa = []
    i = 0
    while i < len(word):
        if i + 1 < len(word) and word[i:i+2] in german_ipa_rules:
            ipa.append(german_ipa_rules[word[i:i+2]])
            i += 2
        elif word[i] in german_ipa_rules:
            ipa.append(german_ipa_rules[word[i]])
            i += 1
        else:
            ipa.append(word[i])
            i += 1
    return ''.join(ipa)

if __name__ == "__main__":
    # 用户输入文本
    user_text = input("请输入一段德文字或一句话: ")

    detection_results = detect_language(user_text)
    detection_results = replace_unknown_languages(detection_results)
    print("检测结果:")
    for method, (lang, confidence) in detection_results.items():
        print(f"{method}: 语言: {lang}, 置信度: {confidence}")
    final_language = aggregate_detection_results(detection_results)
    print(f"最终检测语言: {final_language}")

    # 词性标注
    if final_language == '德语':
        print("\n词性标注结果/汉语意义/德语音标/德语的英式发音国际音标:")
        pos_tagging(user_text)
    else:
        print("对不起，我的程序当前仅支持对德语文本进行词性标注。")

# 关闭数据库连接
conn.close()
