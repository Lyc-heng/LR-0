# 在字符串某个位置加点
def add_char2str(grammar_i, i):
    grammar_i = grammar_i[0:i] + '.' + grammar_i[i:len(grammar_i)]
    return grammar_i


# 给文法加点
def add_dot(grammar):
    # 加点后的文法
    doted_grammar = []
    j = 0
    n = 0
    for i in grammar:
        for k in range(len(i) - 2):
            doted_grammar.append([])
            doted_grammar[n].append(add_char2str(i, k + 3))
            doted_grammar[n].append('false')
            n += 1
        j += 1
    return doted_grammar


# 显示加点后的文法
def print_doted_grammar(doted_grammar):
    print('----加点后的文法----')
    j = 1
    for i in doted_grammar:
        print('%d.%s' % (j, i[0]))
        j += 1


# 显示读入文法
def print_read_grammar(grammar):
    print('----读入的文法----')
    j = 0
    for i in grammar:
        print('(%d)%s' % (j, i))
        j += 1


# 找到终结符和非终结符
def find_term_non(grammar):
    # 非终结符
    VN = []
    # 终结符
    VT = []
    # 非终结符映射
    VN2Int = {}
    # 终结符映射
    VT2Int = {}
    n = int(len(grammar))
    temp_vt = []
    # 标记映像序号
    l = 0
    # 循环寻找非终结符号
    for i in range(n):
        X, Y = grammar[i].split('->')
        # 若非终结符号不在集合中，加入集合
        if X not in VN:
            VN.append(X)
            VN2Int.update({X: l})
            l += 1
        # 暂存终结符号
        for Yi in Y:
            temp_vt.append(Yi)
    # 标记映像的序号
    m = 0
    # 循环查找终结符号
    for i in temp_vt:
        if i not in VN and i not in VT:
            VT.append(i)
            VT2Int.update({i: m})
            m += 1
    VT.append('#')
    VT2Int.update({'#': m})

    return VN, VN2Int, VT, VT2Int


# 初始化文法
# 接受一个文法，返回它的加点符号集、终结符号集合、非终结符号集合
def ini_GS(GS):
    doted_grammar = add_dot(GS)
    print_read_grammar(GS)
    print_doted_grammar(doted_grammar)
    VN, VN2Int, VT, VT2Int = find_term_non(GS)
    return doted_grammar, VN, VN2Int, VT, VT2Int
