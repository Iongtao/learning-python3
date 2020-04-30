

# 模拟一个点餐 （内容是是否需要薯条）
def order(name: str, isNeed: bool):
    # 需要 则isNeed 设置为 True
    if isNeed:
        print(name + '来一份薯条')
    # 否则 不需要
    else:
        print(name + '不要')


order('huamulan', 'aa')  # 'aa' 会被隐式转成bool类型 转化后的结果是 True
order('lejin', 0)  # 0 => False
order('jiaxu', 1)  # 1 => True
order('lvmeng', True)  # True

# 默认表示False的关键字或值有 0, 0.0, '', "", False, None, (), [], {}
# 其他任何值 都会隐式转化为 True
