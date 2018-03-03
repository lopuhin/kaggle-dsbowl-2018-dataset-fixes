#!/usr/bin/env python3
import argparse
from pathlib import Path

import numpy as np
from PIL import Image


def create_masks():
    """ Create masks from red color above original image.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('root')
    args = parser.parse_args()
    root = Path(args.root)
    images_root = root / 'images'
    masks_root = root / 'masks'
    assert images_root.is_dir() and masks_root.is_dir()
    for mask_path in list(images_root.glob('mask*.png')):
        a = np.array(Image.open(mask_path))
        # filter only red color
        mask = (a[:, :, 0] > 127) & (np.max(a[:, :, 1:3], axis=2) < 80)
        out_path = masks_root / mask_path.name
        _save_mask(mask, out_path)
        mask_path.unlink()
        print(f'{mask_path} -> {out_path}')


def ensure_mask():
    """ Ensure that a given (edited) mask shows what is it (clip to 0 or 255).
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('mask_paths', nargs='+')
    args = parser.parse_args()
    mask_paths = []
    for mask_path in map(Path, args.mask_paths):
        if mask_path.is_dir():
            mask_paths.extend((mask_path / 'masks').glob('*.png'))
        else:
            mask_path.append(mask_path)
    for mask_path in mask_paths:
        a = np.array(Image.open(mask_path))
        needs_fixing = False
        if len(a.shape) == 3:
            needs_fixing = True
            print(f'fixing shape (was {a.shape}) for {mask_path}')
            a = a[:, :, :3].max(axis=2)
        if a.dtype != np.uint8:
            print(f'fixing dtype (was {a.dtype}) for {mask_path}')
            needs_fixing = True
            assert a.dtype == np.bool
            a = a.astype(np.uint8) * 255
        assert len(a.shape) == 2
        to_fix = np.sum((a > 0) & (a < 255))
        if to_fix:
            needs_fixing = True
            print(f'fixed {to_fix} pixels for {mask_path}')
        if needs_fixing:
            _save_mask(a > 80, mask_path)


def _save_mask(mask: np.ndarray, path: Path):
    assert mask.dtype == np.bool
    Image.fromarray(mask.astype(np.uint8) * 255).save(path)


if __name__ == '__main__':
    ensure_mask()
