


from shapely.geometry import *

def make_bounds(s):

    bounds = s.bounds # (minx, miny, maxx, maxy)

    b = '([%.3f, %.3f],[%.3f, %.3f])' % (bounds[0], bounds[2], bounds[1], bounds[3])

    return b


def compute_pipeline(args):
    args.gdal_resolution = args.resolution
    args.ept_resolution = args.resolution


    pipeline = open(args.pipeline,'rb').read().decode('utf-8')

    plot = Point(args.x, args.y).buffer(args.buffer, resolution=32)

    args.ept_bounds = make_bounds(plot.buffer(args.buffer + 50))
    args.gdal_bounds = make_bounds(plot.buffer(args.buffer + 50))
    args.crop_polygon = plot.wkt

    pipeline = pipeline % args.__dict__
    return pipeline

def main():
    import argparse

    parser = argparse.ArgumentParser(description='Create PDAL pipeline for a MNDNR Plot')
    parser.add_argument('--url', type=str, default='https://landrush.io/data/shares/3yoo64bbcxgyhmj1/ept.json',
                        help='EPT URL for data')
    parser.add_argument('pipeline', type=str, default='plots.json',
                        help='Pipeline template')
    parser.add_argument('x', type=float,
            help='Plot X in EPSG:26195')
    parser.add_argument('y', type=float,
            help='Plot Y in EPSG:26195')
    parser.add_argument('id', type=str,
            help='Plot ID')
    parser.add_argument('--buffer', type=float, default = "11.3",
                        help='Plot buffer size')
    parser.add_argument('--resolution', type=float, default = "1.0",
                        help='box buffer for query')


    args = parser.parse_args()
    pipeline = compute_pipeline(args)

    import sys
    sys.stdout.write(pipeline)

if __name__ == "__main__":
    main()
