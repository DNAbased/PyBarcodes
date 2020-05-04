import random
import itertools
from polyleven import levenshtein

class BarcodeHandler:
    def __init__(self):
        pass

    @staticmethod
    def remove_below_edit_dist(barcode_list, n=3, randomize=True):
        """remove barcodes below a set levenshtein edit-distance n"""
        min_dist = range(n)  # set the minimum distance
        if randomize:
            random.shuffle(barcode_list)  # shuffle barcodes (to avoid always starting with the same barcode)
        filtered = {barcode_list[0]}  # set first barcode as 'seed'
        barcode_list = set(barcode_list)  # convert barcodes to set (for performance reasons)
        for i in barcode_list:
            broken = 0
            for j in filtered:
                current_dist = levenshtein(i, j, n - 1)  # calculate distance to every barcode added so far
                if current_dist in min_dist:  # only use 'acceptable' barcodes
                    broken = 1  # stop looking if a 'match' is found
                    break
            if broken == 0:
                filtered.add(i)
        return list(filtered)

    @staticmethod
    def remove_incomplete(barcode_list):
        """remove barcodes which do not contain each base at least once"""
        filtered = []
        bases = ['A', 'C', 'G', 'T']
        for barcode in barcode_list:
            if all(x in barcode for x in bases):  # check for presence of all nucleotides
                filtered.append(barcode)
        return filtered

    @staticmethod
    def remove_blacklist(barcode_list, blacklist):
        """remove barcodes which have matches in a provided blacklist"""
        filtered = []
        with open(blacklist) as file:
            remove = list(file)
        remove = [x.strip() for x in remove]
        for barcode in barcode_list:
            if not any(x in barcode for x in remove):
                filtered.append(barcode)
        return(filtered)

    @staticmethod
    def remove_trinucleotide_repeats(barcode_list):
        filtered = []
        repeats = ['AAA', 'CCC', 'GGG', 'TTT']
        for barcode in barcode_list:
            if not any(x in barcode for x in repeats):  # check for repeats
                filtered.append(barcode)
        return filtered

    @staticmethod
    def adjust_gc_level(barcode_list, lower_gc_level=40, upper_gc_level=60):
        """adjust GC level of barcodes"""
        filtered = []
        for barcode in barcode_list:
            current_gc_level = (barcode.count('G') + barcode.count('C')) / len(barcode) * 100  # get gc content
            if lower_gc_level < current_gc_level < upper_gc_level:
                filtered.append(barcode)
        return filtered

    @staticmethod
    def create_barcodes(n):
        """create all barcodes for length n as cartesian product of the bases"""
        barcodes = []
        bases = ['A', 'C', 'G', 'T']
        for length in itertools.product(bases, repeat=n):
            current_barcode = ''.join(length)
            barcodes.append(current_barcode)
        return barcodes
