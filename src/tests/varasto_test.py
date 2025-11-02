import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_konstruktori_ei_hyvaksy_negatiivista_tilavuutta(self):
        v = Varasto(-1)
        self.assertAlmostEqual(v.tilavuus, 0.0)

    def test_konstruktori_asettaa_alkusaldo_nollaksi_jos_negatiivinen(self):
        v = Varasto(10, -5)
        self.assertAlmostEqual(v.saldo, 0.0)

    def test_konstruktori_rajoittaa_alkusaldo_tilavuuteen(self):
        v = Varasto(5, 10)
        self.assertAlmostEqual(v.saldo, 5)

    def test_lisaa_varastoon_ei_sallii_negatiivista(self):
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisaa_varastoon_yli_tilavuuden_tayttaa(self):
        self.varasto.lisaa_varastoon(15)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ota_varastosta_negatiivinen_palauttaa_nolla_ei_muuta(self):
        self.varasto.lisaa_varastoon(5)
        saatu = self.varasto.ota_varastosta(-3)
        self.assertAlmostEqual(saatu, 0.0)
        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_ota_varastosta_suurempi_kuin_saldo_palauttaa_kaiken_ja_nollaa(self):
        self.varasto.lisaa_varastoon(5)
        saatu = self.varasto.ota_varastosta(10)
        self.assertAlmostEqual(saatu, 5)
        self.assertAlmostEqual(self.varasto.saldo, 0.0)

    def test_str_palauttaa_oikean_muodon(self):
        self.varasto.lisaa_varastoon(3)
        s = str(self.varasto)
        expected = f"saldo = {self.varasto.saldo}, vielä tilaa {self.varasto.paljonko_mahtuu()}"
        self.assertEqual(s, expected)

    def test_paljonko_mahtuu_kun_tilavuus_nolla(self):
        v = Varasto(0, 0)
        self.assertAlmostEqual(v.paljonko_mahtuu(), 0.0)
