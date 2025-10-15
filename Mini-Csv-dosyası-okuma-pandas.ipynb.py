{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPoOB1uq4aC9oULGuDLZh/c",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Ecemm1/python-mini--projects/blob/main/Mini-Csv-dosyas%C4%B1-okuma-pandas.ipynb.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "THmxPUE8yZPf",
        "outputId": "0849c7f8-4208-4d2c-b5ad-9982d464dd89"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "-----VERİ TABLOSU-----\n",
            "   UrunID UrunAdi  Adet  BirimFiyat\n",
            "0     101   Kalem     5        15.0\n",
            "1     102  Defter     2        40.0\n",
            "2     103   Silgi    10         5.5\n",
            "3     101   Kalem     3        15.0\n",
            "4     104    Bant     1        20.0\n",
            "-----TOPLAM FIYATLAR-----\n",
            "   UrunID UrunAdi  Adet  BirimFiyat  Toplam Fiyat\n",
            "0     101   Kalem     5        15.0          75.0\n",
            "1     102  Defter     2        40.0          80.0\n",
            "2     103   Silgi    10         5.5          55.0\n",
            "3     101   Kalem     3        15.0          45.0\n",
            "4     104    Bant     1        20.0          20.0\n",
            "5     102  Defter     4        40.0         160.0\n",
            "6     101   Kalem     2        15.0          30.0\n",
            "7     103   Silgi     5         5.5          27.5\n",
            "-----ÜRÜN SATIŞ ADETLERİ-----\n",
            "UrunAdi\n",
            "Bant       1\n",
            "Defter     6\n",
            "Kalem     10\n",
            "Silgi     15\n",
            "Name: Adet, dtype: int64\n",
            "-----EN ÇOK SATILAN ÜRÜN-----\n",
            "Silgi\n"
          ]
        }
      ],
      "source": [
        "import pandas as pd\n",
        "try:\n",
        "  df=pd.read_csv('satislar.csv')\n",
        "\n",
        "  print(\"-----VERİ TABLOSU-----\")\n",
        "  print(df.head())\n",
        "  df['Toplam Fiyat']=df['Adet']*df['BirimFiyat']\n",
        "  print(\"-----TOPLAM FIYATLAR-----\")\n",
        "  print(df)\n",
        "  urun_satis_adetleri=df.groupby('UrunAdi')['Adet'].sum()\n",
        "  print(\"-----ÜRÜN SATIŞ ADETLERİ-----\")\n",
        "  print(urun_satis_adetleri)\n",
        "  en_cok_satilan_urun=urun_satis_adetleri.idxmax()\n",
        "  print(\"-----EN ÇOK SATILAN ÜRÜN-----\")\n",
        "  print(en_cok_satilan_urun)\n",
        "\n",
        "except FileNotFoundError:\n",
        "    print(\"dosya bulunamadı\")\n",
        "\n",
        "except Exception as e:\n",
        "    print(f\"bir hata oluştu:\",{e})"
      ]
    }
  ]
}