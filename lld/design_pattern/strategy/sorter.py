from lld.design_pattern.strategy.bubble_sort import BubbleSort
from lld.design_pattern.strategy.factory.sortingFactory import SortingFactory
from lld.design_pattern.strategy.quick_sort import QuickSort


class Sorter:

    def sort_date(self,data, algo):
        strategy = SortingFactory.getSortingObj(algo)
        strategy.sort(data)
