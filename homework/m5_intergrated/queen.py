# https://blog.csdn.net/Hackbuteer1/article/details/6657109
# 目前最快的N皇后递归解决方法
# N Queens Problem
# 试探-回溯算法，递归实现
import time

# total用来记录皇后放置成功的不同布局数；upperlim用来标记所有列都已经放置好了皇后。
total = 0
upperlim = 1

def test(row, ld, rd):
    # // row，ld，rd进行“或”运算，求得所有可以放置皇后的列, 对应位为0，
    # // 然后再取反后“与”上全1的数，来求得当前所有可以放置皇后的位置，对应列改为1
    # // 也就是求取当前哪些列可以放置皇后
    print('1.{:04b}\t'.format(row))
    print('1.{:04b}\t'.format(upperlim))
    if (row != upperlim):
        print('2.{:04b}\t'.format(upperlim))
        print('2.{:04b}\t'.format(row))
        print('2.{:04b}\t'.format(ld))
        print('2.{:04b}\t'.format(rd))
        print('2.{:04b}\t'.format((row | ld | rd)))
        print('2.{:05b}\t'.format(~(row | ld | rd)))
        pos = upperlim & ~(row | ld | rd)
        print('2.{:04b}\t'.format(pos))
        while pos:
            # // 拷贝pos最右边为1的bit，其余bit置0
            # // 也就是取得可以放皇后的最右边的列
            p = pos & -pos
            print('3.{:05b}'.format(pos))
            print('3.{:05b}'.format(-pos))
            print('3.{:05b}'.format(p))
            # // 将pos最右边为1的bit清零
            # // 也就是为获取下一次的最右可用列使用做准备，
            # // 程序将来会回溯到这个位置继续试探
            print('4.{:04b}'.format(pos))
            pos -= p
            print('4.{:05b}'.format(-p))
            print('4.{:04b}'.format(pos))
            # // row + p，将当前列置1，表示记录这次皇后放置的列。
            # // (ld + p) << 1，标记当前皇后左边相邻的列不允许下一个皇后放置。
            # // (ld + p) >> 1，标记当前皇后右边相邻的列不允许下一个皇后放置。
            # // 此处的移位操作实际上是记录对角线上的限制，只是因为问题都化归
            # // 到一行网格上来解决，所以表示为列的限制就可以了。显然，随着移位
            # // 在每次选择列之前进行，原来N×N网格中某个已放置的皇后针对其对角线
            # // 上产生的限制都被记录下来了
            print('5.{:04b}'.format(row + p))
            print('5.{:04b}'.format((ld + p) << 1))
            print('5.{:04b}'.format((rd + p) >> 1))
            test(row + p, (ld + p) << 1, (rd + p) >> 1)
    else:
        global total
        total += 1
        print('6.')

def main():
    n = 4
    print("{}皇后".format(n))
    tm = time.process_time()

    global upperlim
    upperlim = (upperlim << n) - 1
    test(0, 0, 0)
    print("共有{}种排列, 计算时间{:.5f}秒".format(total, time.process_time() - tm))


main()