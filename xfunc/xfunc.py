# coding:utf-8


def sleep(t: int):
    import time
    import xprint as xp
    xp.wr(xp.Fore.LIGHTBLUE_EX +
          ' - [' + '-' * t + '] sleep 0/%s s' % t + '\r')
    xp.fi()

    for i in range(1, t + 1):
        time.sleep(1)
        xp.wr(xp.Fore.LIGHTBLUE_EX +
              ' - [' + '>' * i + '-' * (t - i) + '] sleep %s/%s s' % (i, t) + '\r')
        xp.fi()

    xp.fi(inline=False)


def get_dict_by_keys(source, keys: list):
    r = {}
    for key in keys:
        if key in source.keys(): r[key] = source[key]
    return r
