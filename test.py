#!/usr/bin/env python3

from pathlib import Path
from argparse import ArgumentParser
from pprint import pprint

from openslide import OpenSlide, PROPERTY_NAME_MPP_X, PROPERTY_NAME_MPP_Y
from openslide.deepzoom import DeepZoomGenerator

DEEPZOOM_TILESIZE=254
DEEPZOOM_OVERLAP=0
DEEPZOOM_LIMIT_BOUNDS=True


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--level", type=int, default=11)
    parser.add_argument("--x", type=int, default=0)
    parser.add_argument("--y", type=int, default=2)
    parser.add_argument("--file-path", type=str, default="/files/data/CMU-1.svs")
    parser.add_argument("--output-file-path", type=str, default="/files/output/out.jpeg")
    parser.add_argument("--img-format", type=str, default="jpeg")
    parser.add_argument("--img-quality", type=int, default=100)
    args = parser.parse_args()

    file_path = Path(args.file_path).expanduser()
    slide = OpenSlide(str(file_path))
    print(slide.level_dimensions)
    print(slide.level_downsamples)
    mpp_x = slide.properties[PROPERTY_NAME_MPP_X]
    mpp_y = slide.properties[PROPERTY_NAME_MPP_Y]
    print(mpp_x, mpp_y)
    pprint(dict(slide.properties))

    dzg = DeepZoomGenerator(
        slide,
        tile_size=DEEPZOOM_TILESIZE,
        overlap=DEEPZOOM_OVERLAP,
        limit_bounds=DEEPZOOM_LIMIT_BOUNDS,
    )

    location = (args.x, args.y)
    region = dzg.get_tile(args.level, location)
    region.save(args.output_file_path, format=args.img_format, quality=args.img_quality)
