from lld.design_pattern.strategy.bubble_sort import BubbleSort
from lld.design_pattern.strategy.mergeSort import MergeSort
from lld.design_pattern.strategy.quick_sort import QuickSort


class SortingFactory:

    @staticmethod
    def getSortingObj(algo):
        if algo == "Bubble sort":
            return BubbleSort()
        elif algo == "Quick":
            return QuickSort()
        elif algo == "Merge":
            return MergeSort()