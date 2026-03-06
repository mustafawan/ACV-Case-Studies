import pandas as pd
import numpy as np

def load_data(verbose=True):

    file_path = "../data/elektrik_veri.xlsx"
    xls = pd.ExcelFile(file_path)

    # Her sayfayı ayrı DataFrame'e yükle
    df_tahsilat = pd.read_excel(xls, sheet_name='Tahsilat')
    df_tahsilat_1 = pd.read_excel(xls, sheet_name='Tahsilat 1')
    df_tahakkuk = pd.read_excel(xls, sheet_name='Tahakkuk')      # Hamamözü
    df_tahakkuk_1 = pd.read_excel(xls, sheet_name='Tahakkuk 1')  # Gümüşhacıköy
    df_tahakkuk_2 = pd.read_excel(xls, sheet_name='Tahakkuk 2')  # Göynücek

    if verbose:
        print("Veriler başarıyla yüklendi.\n")
        print("Sheet Names:", xls.sheet_names)
        print("\nDataFrame Boyutları:")
        print("Tahsilat:", df_tahsilat.shape)
        print("Tahsilat 1:", df_tahsilat_1.shape)
        print("Tahakkuk (Hamamözü):", df_tahakkuk.shape)
        print("Tahakkuk 1 (Gümüşhacıköy):", df_tahakkuk_1.shape)
        print("Tahakkuk 2 (Göynücek):", df_tahakkuk_2.shape)

    return df_tahsilat, df_tahsilat_1, df_tahakkuk, df_tahakkuk_1, df_tahakkuk_2
