def t_me(s):
    'asdffddssafgggftyhhjooopiyyygg'
    'sdffddssfgggftyhhjooopiyyygg'
    'ababdfdfdfdff'  # abab
    'aaabccbdbdbdfdfdfdfdff'  # bdbdbd

    'beabeefeab'
    'eaeefea'
    max_counter = 0
    deleted_chars = []
    if len(s) == 2 and s[0] != s[1]:
        print(2)
        return
    for char in s:
        if char not in deleted_chars:
            candidate_string = [x for x in s if x != char]
            temp_counter = 0
            if not candidate_string or len(candidate_string) < 2:
                break
            candidate_string = ''.join(candidate_string)
            pair = candidate_string[:2]
            while (candidate_string.find(pair) > -1 ):
                candidate_string=candidate_string[candidate_string.find(pair) + 2:]
                temp_counter += 2
            if temp_counter > 0 and pair[0] in candidate_string:
                temp_counter += 1
            if temp_counter > max_counter:
                max_counter=temp_counter
                print('###################')
                print(pair)
                print(max_counter)
                print('###################')
        deleted_chars.append(char)
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print(max_counter)


t_me('beabeefeab')
# t_me('asdffddssafgggftyhhjooopiyyygg')
# t_me('')
# t_me('aaa')
# t_me('ab')
t_me('ezfnjymgqtjnmstbadgdsrxvntnacwljnkgchtjeaoivfcindgxipmrjuqmmcpntpotplodjhijxqpogjmzipygacfdjgmewechuebxvcbnakszzcxkozxwavzgmesrvysonomhvufezislfntgncspthcpneyminpbjildobozfirvcgdratdpmmpkujcywvtzkdytzyfejbytsobvudvutfueveevgrqnxjiwpkrvllsjxmqhotlnpgjxkjnobxfqodlyiqsisdeuwqmntxouzdtisgutdafostmwticvncjwldpknuodmfksusaqpsoosgpiveyxipfklmhypdxpdncpgaswpycoxsuxasqduojpblctcyvyxldcgzevedvxiwinfppkjbtifuuapickknwxxjmjmtxlpfalxdgepmekaxijuphqfafrnezyldokwcnzenhpibktlfuxjfmeqajmvopbhuslnnnlmkmoteceiwbytjhhxqnkuazevswrkaofggfrnapciuoexqogscugzspwuvzkyrdfkhixcaqctfwadewpqksxxvqiigvjjpagvqikuojlwhfyztu')
