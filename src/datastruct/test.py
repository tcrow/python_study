# -*- coding:UTF-8 -*-

file = open("d:/111.sql", 'r', encoding='utf-8')
strArr = []
sql = 'INSERT INTO PRGTJNL (`JRN_NO`, `BAT_NO`, `USR_NO`, `DEAL_FLG`, `DEAL_TXN_TYP`, `DEAL_TXN_DESC`, `SELF_AC_NO`, `PRG_NO`, `DEAL_AMT`, `DEAL_CNL`, `DEAL_STS`, `OPPO_USR_NO`, `OPPO_AC_NO`, `AC_DT`, `TM_SMP`, `PAY_JRN_NO`, `PRG_RFD_NO`, `TRANS_JRN_NO`, `FLOW_TYPE`, `COUPON_TYPE`) VALUES'
try:
    for line in file.readlines():
        line = line[1:len(line) - 2]
        line_sp = line.split(',')
        i = 0
        str = ''
        while i < 20:
            str += line_sp[i] + ','
            i += 1
        str = '(' + str[:-1] + ');'
        strArr.append(str)
finally:
    file.close()
write = open("d:/ttt.sql", "w", encoding='utf-8')
try:
    for line in strArr:
        write.write(sql + ' ' + line + '\n')
finally:
    write.close()
