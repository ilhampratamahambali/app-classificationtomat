def label_description(label):
    desc = {
        "Mentah": "Tomat berwarna hijau dan belum matang.",
        "Setengah Matang": "Tomat mulai berubah warna hijau ke merah.",
        "Matang": "Tomat merah dan siap dikonsumsi."
    }
    return desc.get(label, "")
