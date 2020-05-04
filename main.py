import sys
import importlib
from handlers import BarcodeHandler


class BarcodeParser:
    def __init__(self):
        self.config = importlib.import_module(sys.argv[1][0:-3])

    def parse(self):
        bh = BarcodeHandler()
        barcodes = bh.create_barcodes(self.config.length)
        if self.config.repeats == 1:
            barcodes = bh.remove_trinucleotide_repeats(barcodes)

        if self.config.each_nt == 1:
            barcodes = bh.remove_incomplete(barcodes)

        if self.config.blacklist:
            barcodes = bh.remove_blacklist(barcodes, self.config.blacklist)

        barcodes = bh.adjust_gc_level(barcodes, self.config.gc_lower, self.config.gc_upper)

        if self.config.levenshtein > 0:
            barcodes = bh.remove_below_edit_dist(barcodes, self.config.levenshtein)

        if self.config.output_mode == 'json':
            import json
            final_filename = self.config.output_prefix + 'json'
            with open(final_filename, 'w') as f:
                json.dump(barcodes, f, indent=1)
        else:
            final_filename = self.config.output_prefix + '.tsv'
            with open(final_filename, 'w') as f:
                for bc in barcodes:
                    f.write('%s\n' % bc)


if __name__ == '__main__':
    BarcodeParser().parse()
