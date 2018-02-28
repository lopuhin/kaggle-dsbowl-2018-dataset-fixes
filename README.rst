Kaggle Data Science Bowl 2018 dataset fixes
===========================================

This repo contains unofficial fixes for the
`Kaggle Data Science Bowl 2018 <https://www.kaggle.com/c/data-science-bowl-2018>`_
stage 1 train dataset. The dataset was created by the
Carpenter lab at the Broad Institute of Harvard
and MIT for 2018 Data Science Bowl
and released under Creative Commons license 0 (CC0 public domain):
https://www.kaggle.com/c/data-science-bowl-2018/discussion/47864

Fixes are released under the same license: Creative Commons license 0 (CC0 public domain).
All fixes are in master, this is a drop-in replacement for the original dataset.
You don't need to use ``mask_tools.py`` in order to use the dataset - these tools were used
for creating the annotations.
Pull requests welcome!

Summary of fixes:

- ``7b38c9173ebe69b4c6ba7e703c0c27f39305d9b2910f46405993d2ea7a963b80``
  removed, as no nuclei were annotated
- ``12aeefb1b522b283819b12e4cfaf6b13c1264c0aadac3412b4edd2ace304cb40``
  removed, missing ~20 clear nuclei (could be fixed)
- ``58c593bcb98386e7fd42a1d34e291db93477624b164e83ab2afa3caa90d1d921``
  added 1 nuclei bottom right
- ``a7f767ca9770b160f234780e172aeb35a50830ba10dc49c526f4712451abe1d2``
  added 1 nuclei bottom left
- ``74a7785530687a11ecd073e772f90912d9967d02407a192bfab282c35f55ab94``
  removed, as it has many out of focus nuclei not annotated (could be fixed)
- ``b1eb0123fe2d8c825694b193efb7b923d95effac9558ee4eaf3116374c2c94fe``
  added 3 missing nuclei, removed one bad
- ``19f0653c33982a416feed56e5d1ce6849fd83314fd19dfa1c5b23c6b66e9868a``
  removed, as many nuclei are not separated (could be fixed by watershed)
- ``9bb6e39d5f4415bc7554842ee5d1280403a602f2ba56122b87f453a62d37c06e``
  removed bar mask a09ae9559f817b104e049e5bb01cf4ad1b87e3ef7fad3dcf932b6585ca3edc05
- ``1f0008060150b5b93084ae2e4dabd160ab80a95ce8071a321b80ec4e33b58aca``
  separated 2 pairs of nuclei
- ``5d21acedb3015c1208b31778561f8b1079cca7487399300390c3947f691e3974``
  filled holes in mask 5e6e650a28e22f651817b2edeacbf93a960adf633f1dbef69ecea585ef35d544
- ``55f98f43c152aa0dc8bea513f8ba558cc57494b81ae4ee816977816e79629c50``
  fixed mask e5b2747c30db016c8318c1df1391708b85c290d8a80d62e013b14ceb759c998e
- ``0a7d30b252359a10fd298b638b90cb9ada3acced4e0c0e5a3692013f432ee4e9``
  separated mask 8246970b0d108736b3e8a1a45872737a30a2332dc00fce23534c86b1cbc80f73
- ``0121d6759c5adb290c8e828fc882f37dfaf3663ec885c663859948c154a443ed``
  filled mask 56618a746e807cc8c794c06d34ade16117d6661ab5da530045e88248e3493d0e
- ``adc315bd40d699fd4e4effbcce81cd7162851007f485d754ad3b0472f73a86df``
  removed, as several nuclei not annotated (could be easily fixed)
- ``af576e8ec3a8d0b57eb6a311299e9e4fd2047970d3dd9d6f52e54ea6a91109da``
  added 1 missing mask
- ``1bd0f2b3000b7c7723f25335fabfcdddcdf4595dd7de1b142d52bb7a186885f0``
  separated 2 pairs of nuclei
- ``c304a1fdf3bca2f4b4580d2cac59942e2224a7678001bf5ed9d9852f57708932``
  removed, as many nuclei are not separated (could be fixed)
