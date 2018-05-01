# 数据约定

每个时钟周期:

1. 每个阶段以阶段名为字典
    info['F'].update()
    内部变量用_name的形式, 阶段寄存器直接用本来的名字name
    把所有变量传出来. 还有赋值情况.
2. info['reg'] = {regName : value(BigEndian)}
3. info['mem'] = {addr: value(4 bites, none trival)}
4. info['stat'] = SAOK|SHLT|...
5. info['cyc'] = clock_cycle
