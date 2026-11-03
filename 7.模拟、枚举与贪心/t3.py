import sys

s = sys.stdin.read()

result = []
i = 0
quote = None

while i < len(s):

    # 当前字符
    ch = s[i]

    # 判断是否遇到引号
    if ch == '"' or ch == "'":

        # 统计引号前面连续反斜杠的数量
        cnt = 0
        j = i - 1

        while j >= 0 and s[j] == '\\':
            cnt += 1
            j -= 1

        # 奇数个反斜杠表示引号被转义
        escaped = (cnt % 2 == 1)

        if not escaped:
            if quote is None:
                quote = ch
            elif quote == ch:
                quote = None

        result.append(ch)
        i += 1
        continue

    # 不在字符串内部，才检查注释
    if quote is None and s[i:i+2] == '/*':

        # 寻找第一个 */
        end = s.find('*/', i + 2)

        if end != -1:
            # 删除整个注释
            i = end + 2
            continue
        else:
            # 没有匹配的 */，保留 /*
            result.append('/')
            result.append('*')
            i += 2
            continue

    # 普通字符原样保留
    result.append(ch)
    i += 1

# 输出结果，不额外添加换行
sys.stdout.write(''.join(result))