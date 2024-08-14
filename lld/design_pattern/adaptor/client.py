from lld.design_pattern.adaptor.Phonepe import PhonePe
from lld.design_pattern.adaptor.abapters.iciciBankAdapter import IciciBankAdapter

if __name__ == '__main__':
    b = IciciBankAdapter()
    p = PhonePe(b)
    print(p.checkBalance())
