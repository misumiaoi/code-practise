import enum
import sys # 用于打印错误信息到标准错误
import random, time

# 使用枚举来定义不同的排序类型，提高代码可读性
class SortType(enum.Enum):
    BUBBLE_SORT = 1
    INSERTION_SORT = 2
    SELECTION_SORT = 3
    DEFAULT_SORT = BUBBLE_SORT
    # 你可以在这里添加更多排序类型

    # 添加一个友好的字符串表示，方便打印
    def __str__(self):
        return self.name.replace('_', ' ').title() # 将 BUBBLE_SORT 转换为 "Bubble Sort"

class SortingMachine:
    def __init__(self, sort_type=SortType.BUBBLE_SORT):
        """
        初始化排序机。

        Args:
            sort_type: 指定排序类型，使用 SortType 枚举。
                       默认为 SortType.BUBBLE_SORT。
        """
        self.sort_count = 0 # 初始化排序次数计数器

        # 使用字典来映射排序类型到实际的排序函数
        # 字典的键是 SortType 枚举成员，值是类内部的排序方法（函数对象）
        self._sorting_methods = {
            SortType.BUBBLE_SORT: self._bubble_sort,
            SortType.INSERTION_SORT: self._insertion_sort,
            SortType.SELECTION_SORT: self._selection_sort
            # 在这里添加更多排序类型和对应的函数
        }

        self.current_sort_method = None # 存储当前选定的排序函数
        self._current_sort_type_name = "Unknown" # 存储当前排序方法的名称，方便打印

        self.set_sorting_type(sort_type) # 初始化时设置排序方法

    def set_sorting_type(self, sort_type):
        """
        设置或更改排序机的排序方法。

        Args:
            sort_type: 指定新的排序类型，使用 SortType 枚举。
        Raises:
            ValueError: 如果传入了未知的排序类型。
        """
        if sort_type in self._sorting_methods:
            self.current_sort_method = self._sorting_methods[sort_type]
            self._current_sort_type_name = str(sort_type) # 使用枚举的字符串表示
            print(f"Sorting method set to {self._current_sort_type_name}.")
        else:
            # 处理未知类型 - 可以选择抛出异常或者使用默认值
            print(f"Warning: Unknown sorting type ({sort_type}). Defaulting to {str(SortType.BUBBLE_SORT)}.", file=sys.stderr)
            self.current_sort_method = self._sorting_methods[SortType.BUBBLE_SORT]
            self._current_sort_type_name = str(SortType.BUBBLE_SORT)
            # 或者抛出异常: raise ValueError(f"Unknown sort type: {sort_type}")


    def sort(self, data: list):
        """
        对给定的列表进行排序。排序是原地进行的（修改原始列表）。

        Args:
            data: 需要排序的列表。
        """
        if self.current_sort_method:
            print(f"Sorting list using {self._current_sort_type_name}...")
            self.current_sort_method(data) # 调用当前选定的排序函数
            self.sort_count += 1 # 排序次数加一
            print("Sorting complete.")
        else:
            print("Error: No sorting method selected!", file=sys.stderr)


    def get_sort_count(self):
        """
        获取此排序机实例执行排序的次数。

        Returns:
            int: 排序次数。
        """
        return self.sort_count

    # --- 具体的排序算法实现 (私有方法，通常以单下划线开头) ---
    # 这些方法会修改传入的列表（原地排序）

    def _bubble_sort(self, data: list):
        """原地实现冒泡排序。"""
        n = len(data)
        # 遍历所有数组元素
        for i in range(n):
            # Last i elements are already in place
            # 内层循环遍历数组
            for j in range(0, n - i - 1):
                # 如果当前元素大于下一个元素，交换它们
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j] # Python 风格的交换

    def _insertion_sort(self, data: list):
        """原地实现插入排序。"""
        # 遍历从第二个元素到最后一个元素
        for i in range(1, len(data)):
            key = data[i]
            # 将 data[0..i-1] 中比 key 大的元素向后移动一位
            j = i - 1
            while j >= 0 and key < data[j]:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key

    # 在这里添加更多排序算法的实现，例如：
    # def _merge_sort(self, data: list):
    #     # 实现归并排序...
    #     pass # Placeholder
    #
    # def _quick_sort(self, data: list):
    #     # 实现快速排序...
    #     pass # Placeholder

    def _selection_sort(self, data: list):
        for i in range(1, len(data),++i):
            key = data[i]
            minindex = i
            for j in range(i+1, j<n,++j):
                if(data[j]<minindex):
                    minindex = j

# 辅助函数：打印列表（Python 的默认打印就很好了）
def print_list(data: list):
    print(data)

# --- 示例用法 ---
if __name__ == "__main__":
    # 准备数据
    numbers1 = [5, 2, 8, 1, 9, 4, 7, 3, 6]
    numbers2 = [10, 0, 5, -3, 12]
    numbers3 = [3.14, 1.618, 2.718, 0.577]

    print("--- Using Bubble Sort ---")
    # 1. 初始化 SortingMachine 对象，指定使用冒泡排序
    bubble_sorter = SortingMachine(SortType.BUBBLE_SORT)

    # 2. 输入 / 准备数据 (已定义)

    print("Original list 1:")
    print_list(numbers1)

    # 3. 调用 sort 方法进行排序
    bubble_sorter.sort(numbers1)

    # 4. 输出结果
    print("Sorted list 1:")
    print_list(numbers1)
    print("BubbleSorter sort count:", bubble_sorter.get_sort_count())

    print("\n--------------------\n")

    print("--- Using Insertion Sort ---")
    # 1. 初始化另一个 SortingMachine 对象，指定使用插入排序
    insertion_sorter = SortingMachine(SortType.INSERTION_SORT)

    # 2. 输入 / 准备数据 (已定义)
    print("Original list 2:")
    print_list(numbers2)

    # 3. 调用 sort 方法进行排序
    insertion_sorter.sort(numbers2)

    # 4. 输出结果
    print("Sorted list 2:")
    print_list(numbers2)
    print("InsertionSorter sort count:", insertion_sorter.get_sort_count())

    print("\n--------------------\n")

    print("--- Using Insertion Sort on floats ---")
     # SortingMachine 可以用于 float 类型的列表
    float_list = [3.14, 1.618, 2.718, 0.577]
    float_sorter = SortingMachine(SortType.INSERTION_SORT)

    print("Original list 3:")
    print_list(float_list)

    float_sorter.sort(float_list)

    print("Sorted list 3:")
    print_list(float_list)
    print("FloatSorter sort count:", float_sorter.get_sort_count())

    print("\n--------------------\n")

    print("--- Reusing Bubble Sort object ---")
    numbers4 = [99, 11, 33, 22]
    print("Original list 4:")
    print_list(numbers4)
    bubble_sorter.sort(numbers4) # 再次使用 bubble_sorter 对象
    print("Sorted list 4:")
    print_list(numbers4)
    print("BubbleSorter sort count (after sorting list 4):", bubble_sorter.get_sort_count()) # 查看累加的次数

    print("\n--------------------\n")

    print("--- Changing sorting method on the fly ---")
    numbers5 = [1, 2, 3, 4, 5]
    print("Original list 5:")
    print_list(numbers5)
    # 改变 bubble_sorter 的排序方法为插入排序
    bubble_sorter.set_sorting_type(SortType.INSERTION_SORT)
    bubble_sorter.sort(numbers5) # 现在将使用插入排序
    print("Sorted list 5:")
    print_list(numbers5)
    print("BubbleSorter sort count (after changing method):", bubble_sorter.get_sort_count()) # 查看累加的次数