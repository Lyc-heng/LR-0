# 对输入串进行分析
def ana_input(grammar, action, goto, VT, VN, input_str):
    # 初始化状态栈、符号栈,输入串
    state_shed = []
    state_shed.append("0")
    symbol_shed = []
    symbol_shed.append("#")
    istr = list(reversed(input_str))
    # 用于打印过程
    count = 1
    print("------------对输入串%s的LR(0)分析过程------------"%(input_str))
    print("%s%8s%10s%12s%12s%8s"%("步骤","状态栈","符号栈","输入串","ACTION","GOTO"))
    while(True):
        print("(%d)"%count,end="")
        count+=1
        print("\t%8s"%("".join(state_shed)),end="")
        print("%12s"%("".join(symbol_shed)),end="")
        print("%14s"%("".join(list(reversed(istr)))),end="")
        # 若为S跳转,记录表内对应的跳转符号为Si还是ri
        table_symbol = action[int(state_shed[-1])][find_symbolVT_index(VT,istr[-1])]
        # 如果action表为空
        if table_symbol == "":
            print("出错，对输入串%s无法进行规约" % (input_str))
            break
        # 当遇到action中的S符号时
        if table_symbol[0] == "s":
            state_shed.append(table_symbol[1:])
            symbol_shed.append(istr[-1])
            istr.pop()
            print("%12s"%("".join(table_symbol)),end="")
        elif table_symbol[0] == "r":
            print("%12s" % ("".join(table_symbol)), end="")

            temp = str(grammar[int(table_symbol[1:])]).split("->")
            for x in range(len(temp[1])):
                symbol_shed.pop()
                state_shed.pop()
            symbol_shed.extend(str(temp[0]))
            # 如果goto表为空
            if goto[int(state_shed[-1])][find_symbolVN_index(VN,str(temp[0]))] == -1:
                print("出错，对输入串%s无法进行规约"%(input_str))
                break
            else:
                print("%10s"%(str(goto[int(state_shed[-1])][find_symbolVN_index(VN,str(temp[0]))])),end="")
                state_shed.append(str(goto[int(state_shed[-1])][find_symbolVN_index(VN,str(temp[0]))]))
        elif table_symbol[0] == "a":
            print("%12s"%("acc"))
            print("\n对字符串%s规约成功"%(input_str))
            break
        print("")



# 返回其在VT中的位置
def find_symbolVT_index(VT,symbol):
    for i in range(len(VT)):
        if symbol == str(VT[i]):
            return i

# 返回其在VN中的位置
def find_symbolVN_index(VN,symbol):
    for i in range(len(VN)):
        if symbol == str(VN[i]):
            return i