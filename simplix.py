def user_word(prompt = '', words_to_match = []):
    if len(words_to_match) == 0:
        return strip_inputs_alpha(prompt)
    else:
        started = False
        user_in = ''
        while (user_in not in words_to_match) or not started:
            user_in = strip_inputs_alpha(prompt)
            started = True
        return user_in


def strip_inputs_alpha(prompt = ''):
    good_flag = False
    u_in = ''
    while not good_flag:
        u_in = input(prompt).lower().strip()
        good_flag = u_in.isalpha() and (len(u_in) != 0)
    return u_in