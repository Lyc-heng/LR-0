# 得到LR分析表
def get_LR_table(grammar, doted_grammar, VT2Int, VN2Int, VN, VT, DFA, DFA_node):
    action = []  # action表
    goto = []  # goto表

    action, goto = init_LR_table(doted_grammar, action, goto, VT, VN)
    for i in range(len(doted_grammar)):
        if need_protocol(i, DFA_node):
            num = find_grammar(need_protocol(i, DFA_node), grammar)
            tmp = 'r' + str(num)
            for j in range(len(VT)):
                if i == 1:
                    action[i][VT2Int['#']] = 'acc'
                else:
                    action[i][j] = tmp
        else:
            for j in range(len(doted_grammar)):
                if not DFA[i][j] == '':
                    if DFA[i][j] in VN:
                        goto[i][VN2Int.get(DFA[i][j], -1)] = j
                    else:
                        tmp = 's' + str(j)
                        action[i][VT2Int.get(DFA[i][j], -1)] = tmp
    return action, goto


# 初始化LR分析表
def init_LR_table(doted_grammar, action, goto, VT, VN):
    for i in range(len(doted_grammar)):
        action.append([])
        goto.append([])
        for j in range(len(VT)):
            action[i].append('')
        for j in range(len(VN)):
            goto[i].append(-1)
    return action, goto


# 有无规约项
def need_protocol(point, DFA_node):
    if not DFA_node[point][0] == "":
        for i in range(10):
            if DFA_node[point][i].endswith('.'):
                return DFA_node[point][i]
            else:
                return None
    else:
        return None


# 根据文法内容找到文法编号
def find_grammar(string, grammar):
    tmp = string[0: len(string) - 1]
    for i in range(len(grammar)):
        if tmp == grammar[i]:
            return i


# 显示LR分析表
def show_LR_table(VT, VN, doted_grammar, action, goto):
    # 表头
    print('----LR分析表----')
    print('\t\t|\t', end='')
    print(('%3s' % '') * (len(VT) - 2), end='')
    print('Action', end='')
    print(('%3s' % '') * (len(VT) - 2), end='')
    print('\t|\t', end='')
    print(('%3s' % '') * (len(VN) - 2), end='')
    print('GOTO', end='')
    print(('%3s' % '') * (len(VN) - 2), end='')
    print('\t|')
    print('\t\t\t', end='')
    for i in VT:
        print('%3s\t' % i, end='')
    print('\t|\t', end='')
    k = 0
    for i in VN:
        if not k == 0:
            print('%3s\t' % i, end='')
        k += 1
    print('\t|')
    for i in range(len(doted_grammar)):
        print('-----', end='')
    print()
    # 表体
    for i in range(len(doted_grammar)):
        print('%5d\t|\t' % i, end='')
        # 打印action表
        for j in range(len(VT)):
            print('%4s' % action[i][j], end='')
        print('\t|\t', end='')
        # 打印GOTO表
        for j in range(len(VN)):
            if not j == 0:
                if not goto[i][j] == -1:
                    print('%4s' % goto[i][j], end='')
                else:
                    print('\t', end='')
        print('\t|')
    for i in range(len(doted_grammar)):
        print('-----', end='')
    print()
