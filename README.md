# Orðavensl 2.0 - nú með orðavektorum

Python-bakendi fyrir orðavenslaleik í námskeiðinu Málleg gagnasöfn í Háskóla Íslands vorönn 2019. Leikurinn notar orðavigra sem lærðir voru úr [Risamálheildinni](http://malfong.is/?pg=rmh) Framendinn er á https://github.com/svanhviti16/Word-Association-2.0-frontend/.

Til að spila leikinn verður að sækja orðavigralíkan, [sem nálgast má hér](https://drive.google.com/open?id=1fTmy_H_IdCM1-mKbQOy9aAVt_jbj4KNk). Skráin RMH2_w2v.model er lesin inn sem færibreyta þegar forritið er keyrt.

Til að setja upp nauðsynlega Python-pakka skal keyra skipunina

```pip install -r requirements.txt```

Svo er bara að keyra ```api.py``` (í Python 3) með ```.model```-skrána sem færibreytu:

```python api.py SLÓÐ/Á/RMH2_w2v.model```

Þá má ræsa upp [framendann](https://github.com/svanhviti16/Word-Association-2.0-frontend) og spila leikinn.
