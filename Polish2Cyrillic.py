def polish_to_cyrillic(text):
    """
    !!! NO POLITICS !!! <br/>
    Polish Latin script to Cyrillic script: <br/>
    Russian-styled orthography with minor vowel rearrangement <br/>
    by Lew Noeszczow (Лев Ноэщёв)
    """
    
    
    def replace_a_to_b(rep_map):
        """Replace substrings in text based on a provided replacement map."""
        nonlocal text  
        for a, b in rep_map:
            text = text.replace(a, b)

    def initial_transliteration():
        """Apply transliteration rules to convert Polish characters to Cyrillic."""
        # Sort mappings to prioritize longer replacements
        sorted_map = sorted(translit_map.items(), key=lambda x: -len(x[0]))

        # Apply mappings
        replace_a_to_b(ppe_map.items())
        replace_a_to_b(sorted_map)

    def adjust_yer():
        """Adjust 'ь' and 'ъ' based on surrounding characters."""
        nonlocal text_list
        ad_map = {'а': 'ꙗ', 'ѫ': 'ѭ', 'э': 'е', 'я': 'ѥ', 'о': 'ё', 'у': 'ю', 'ы': 'и'}
        for i in range(len(text_list) - 1):
            if text_list[i] in 'иь' and text_list[i + 1] in ad_map:
                text_list[i] = 'j'
                text_list[i + 1] = ad_map[text_list[i + 1]]
            elif text_list[i] == 'й' and text_list[i + 1] in ad_map:
                text_list[i] = 'ъ'
                text_list[i + 1] = ad_map[text_list[i + 1]]
                
    def adjust_syllable():
        """Adjust impropriate syllables."""
        nonlocal text_list
        for i in range(len(text_list) - 1):
            if text_list[i] in 'цчѕџшщж' and text_list[i + 1] in 'эы':
                text_list[i + 1] = 'еи'['эы'.find(text_list[i + 1])]

    def remove_redundant_yer():
        """Remove redundant 'ь' characters according to specified rules."""
        nonlocal text_list
        que = []
        for i in range(len(text_list) - 1):
            if text_list[i] == 'ь':
                que.append(i)
            elif text_list[i] in 'бцдѕфлмнпрствз':
                continue
            else:
                if text_list[i] not in 'jий' and que:
                    que.pop()

                for ye in que:
                    text_list[ye] = 'j'
                que.clear()

        if que and que[-1] == len(text_list) - 1:
            que.pop()
        for ye in que:
            text_list[ye] = 'j'
            que.clear()
        
    def correct_short_i():
        nonlocal text_list
        for i in range(len(text_list) - 1):
            if text_list[i + 1] == 'й':
                if text_list[i] in 'дтр':
                    text_list[i + 1] = 'ъи'
                elif text_list[i] in 'цѕ':
                    text_list[i + 1] = 'и'
                
    def correct_yeri():
        nonlocal text_list
        for i in range(len(text_list)):
            if text_list[i] != 'ъ':
                continue
            if i == 0 or text_list[i - 1] in 'аꙗѫѭэеяѥоёуюцѕь ':
                text_list[i] = 'j'

    def capitalize_words(positions):
        """Capitalize words at the specified positions."""
        words = text.split()
        for i in positions:
            words[i] = words[i][0].upper() + words[i][1:]
        return ' '.join(words)

    # Identify positions of words with uppercase characters
    import re
    positions = [i for i, word in enumerate(text.split()) if re.search(r'[A-ZĄĆĘŁŃÓŚŹŻ]', word)]
    
    # Convert text to lowercase and apply transliteration
    text = text.lower()
    
    # Define mapping for Polish to Cyrillic transliteration
    translit_map = {
        'a': 'а', 'ą': 'ѫ', 'b': 'б', 'c': 'ц', 'ć': 'ть',
        'cz': 'ч', 'd': 'д', 'dz': 'ѕ', 'dź': 'дь', 'dż': 'џ',
        'e': 'э', 'ę': 'я', 'f': 'ф', 'g': 'г', 'h': 'х', 'ch': 'х',
        'i': 'и', 'j': 'й', 'k': 'к', 'l': 'ль', 'ł': 'л',
        'm': 'м', 'n': 'н', 'ń': 'нь', 'o': 'о', 'ó': 'о', 'p': 'п',
        'r': 'р', 'rz': 'рь', 's': 'с', 'ś': 'сь', 'sz': 'ш', 'szcz': 'щ',
        't': 'т', 'u': 'у', 'w': 'в', 'y': 'ы', 'z': 'з', 'ź': 'зь', 'ż': 'ж'
    }
    ppe_map = {
        'ii': 'ij', 'ió': 'iu',
        'ji': 'jj',
        'ci': 'ći', 'dzi': 'dźi', 'di': 'dj',
        'ti': 'tj', 'ri': 'rj',
        'czo': 'czio', 'dżo': 'dżio', 'szo': 'szio', 'żo': 'żio'
    }

    initial_transliteration()
    text_list = list(text)
    
    def join_list():
        return ''.join(text_list).replace('j', '')
    
    #Customization
    # print('initialized:', join_list())
    adjust_yer()
    # print('adjust_yer:', join_list())
    adjust_syllable()
    # print('adjust_syllable:', join_list())
    remove_redundant_yer()
    # print('remove_redundant_yer:', join_list())
    correct_short_i()
    # print('correct_short_i:', join_list())
    correct_yeri()
    # print('correct_yeri:', join_list())
    
    text = join_list()

    return capitalize_words(positions)

# Test
polish_text = input()
print(polish_to_cyrillic(polish_text))