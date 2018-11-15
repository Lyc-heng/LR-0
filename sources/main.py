from ini import ini_GS
from ndfa import make_nfa, make_dfa
from LR_table import get_LR_table, show_LR_table
from analyze_input import ana_input

if __name__ == '__main__':
    # 测试样例文法1
    # GS = ['Y->S', 'S->BB', 'B->aB', 'B->b']
    # input_str = "abab#"
    # 测试样例文法
    GS = ['S->E', 'E->aA', 'E->bB', 'A->cA', 'A->d', 'B->cB', 'B->d']
    input_str = "bccd#"
    # 对文法进行初始化操作,得到文法加点后的序列，以及终结符号集合和非终结符号集合
    doted_grammar, VN, VN2Int, VT, VT2Int = ini_GS(GS)
    # 将文法转换为nfa
    nfa = make_nfa(doted_grammar, VN)
    # 将文法转换为dfa
    dfa, DFA_node = make_dfa(nfa, doted_grammar)
    # 构造LR分析表
    action, goto = get_LR_table(GS, doted_grammar, VT2Int, VN2Int, VN, VT, dfa, DFA_node)
    # 打印LR分析表
    show_LR_table(VT, VN, doted_grammar, action, goto)
    # 进行输入串的分析
    ana_input(GS, action, goto, VT, VN, input_str)
