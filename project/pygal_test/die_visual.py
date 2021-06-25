from die import Die
import pygal
import time


def main():
    # 投掷几次骰子,将结果存入一个列表中

    die_1 = Die()
    die_2 = Die()
    print("开始计时...")
    time_start = time.time()

    results = []
    for roll_num in range(100000000):
        result = die_1.roll() + die_2.roll()
        results.append(result)

    # print(results)

    frequencies = []
    max_result = die_1.num_sides + die_2.num_sides
    for value in range(2, max_result+1):
        frequency = results.count(value)
        frequencies.append(frequency)

    # print(frequencies)\

    time_end = time.time()
    print("结束计时...")
    time_run = time_end - time_start
    # 对结果进行可视化
    hist = pygal.Bar()

    hist.title = "测试投掷 100,000,000 次骰子的结果\n运行时间:%ss" % time_run
    hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    hist.x_title = "总和"
    hist.y_title = "总和的频率"

    hist.add('骰子1+骰子2', frequencies)

    hist.render_to_file('die_visual.svg')
    print("退出")


if __name__ == "__main__":
    main()
