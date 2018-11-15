# 构造NFA
def make_nfa(doted_grammar, VN):
    NFA = []
    grammar_id = []

    for i in range(10):
        grammar_id.append('')

    NFA = init_nfa(NFA, doted_grammar)

    i = 0
    for grammar_i in doted_grammar:
        pos_point = (grammar_i[0]).find('.')
        if not pos_point + 1 == len(grammar_i[0]):
            NFA[i][i + 1] = grammar_i[0][pos_point + 1]
            # 点后面跟着非终结符
            if grammar_i[0][pos_point + 1] in VN:
                j = find_node(grammar_i[0][pos_point + 1], grammar_id, doted_grammar)
                for k in range(j):
                    NFA[i][grammar_id[k]] = '*'
                    NFA = add_more(NFA, i, grammar_id[k], doted_grammar, VN)
        i += 1
    return NFA


# 初始化NFA
def init_nfa(NFA, doted_grammar):
    for row in range(len(doted_grammar)):
        NFA.append([])
        for col in range(len(doted_grammar)):
            NFA[row].append('')
    return NFA


# 查找以start开头，以'.'开始的文法,返回个数
def find_node(start, grammar_id, doted_grammar):
    num = 0
    for i in doted_grammar:
        if is_start(i, start):
            grammar_id[num] = doted_grammar.index(i)
            num += 1
    return num


# 文法是否以start开头，以'.'开始
def is_start(grammar_i, start):
    if grammar_i[0].find(start, 0, 1) + grammar_i[0].find('.', 3, 4) == 3:
        return True
    else:
        return False


# 查找关联
def add_more(NFA, i, j, doted_grammar, VN):
    grammar_id = []
    for k in range(10):
        grammar_id.append('')
    pos_point = (doted_grammar[j][0]).find('.')
    if not pos_point + 1 == len(doted_grammar[j][0]):
        if doted_grammar[j][0][pos_point + 1] in VN:
            j = find_node(doted_grammar[j][0][pos_point + 1], grammar_id, doted_grammar)
            for k in range(j):
                NFA[i][grammar_id[k]] = '*'
                NFA = add_more(NFA, i, grammar_id[k], doted_grammar, VN)
    return NFA


# ===================================================DFA相关函数============================= #
# 构造DFA
def make_dfa(NFA, doted_grammar):
    DFA = []
    DFA_node = []
    DFA = init_dfa(DFA, doted_grammar)
    for i in range(len(doted_grammar)):
        DFA_node.append([])
        for j in range(len(doted_grammar)):
            DFA_node[i].append("")
    for i in range(len(doted_grammar)):
        if doted_grammar[i][1] == 'false':
            k = 0
            DFA_node[i][k] = doted_grammar[i][0]
            k += 1
            doted_grammar[i][1] = 'true'
            for j in range(len(doted_grammar)):
                if NFA[i][j] == '*':  # 有ε弧
                    DFA_node[i][k] = doted_grammar[j][0]
                    k += 1
                    doted_grammar[j][1] = 'true'
                    DFA = add_state(i, j, NFA, DFA, doted_grammar)
    return DFA, DFA_node


# 初始化DFA
def init_dfa(DFA, doted_grammar):
    for row in range(len(doted_grammar)):
        DFA.append([])
        for col in range(len(doted_grammar)):
            DFA[row].append('')
    return DFA


# 连接
def add_state(to, fro, NFA, DFA, doted_grammar):
    for i in range(len(doted_grammar)):
        if not NFA[to][i] == '' and not NFA[to][i] == '*':
            DFA[to][i] = NFA[to][i]
        if not NFA[fro][i] == '' and not NFA[fro][i] == '*':  # from可连接的点
            DFA[to][i] = NFA[fro][i]
    return DFA
