Kaggle Data Science Bowl 2018 dataset fixes
===========================================

This repo contains unofficial fixes for the
`Kaggle Data Science Bowl 2018 <https://www.kaggle.com/c/data-science-bowl-2018>`_
stage 1 train dataset. The dataset was created by
by Carpenter lab at the Broad Institute of Harvard
and MIT for 2018 Data Science Bowl
https://www.kaggle.com/c/data-science-bowl-2018/data
and released under Creative Commons license 0 (CC0 public domain)
https://www.kaggle.com/c/data-science-bowl-2018/discussion/47864

Fixes are released using the same license.
All fixes are in master, this is a drop-in replacement for the original dataset.
Pull requests welcome!

Summary of fixes:

- ``7b38c9173ebe69b4c6ba7e703c0c27f39305d9b2910f46405993d2ea7a963b80``
  removed, as no nuclei were annotated
- ``12aeefb1b522b283819b12e4cfaf6b13c1264c0aadac3412b4edd2ace304cb40``
  removed, missing ~20 clear nuclei (could be fixed)
- ``58c593bcb98386e7fd42a1d34e291db93477624b164e83ab2afa3caa90d1d921``
  added 1 nuclei bottom right
