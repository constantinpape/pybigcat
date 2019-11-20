import argparse
import numpy as np
import imageio
import h5py


def load_vol(file_path, key=None):
    # if no key is given, we assume that this is a tiff file
    # and will use image io to load.
    # otherwsie, we assume it's hdf5 and use h5py
    if key is None:
        data = np.asarray(imageio.volread(file_path))
    else:
        with h5py.File(file_path, 'r') as f:
            ds = f[key]
            data = ds[:]
    return data


# TODO support different resolutions for raw and seg
def to_bigcat_format(raw_file, seg_file, out_file,
                     raw_key=None, seg_key=None,
                     resolution=[1, 1, 1], offset=[0, 0, 0]):
    """ Convert data into bigcat data format.

    Arguments:
    """

    raw = load_vol(raw_file, raw_key)
    seg = load_vol(seg_file, seg_key)
    if sum(offset) == 0:
        assert raw.shape == seg.shape, "The shape of the raw data and the segmentation must agree"

    with h5py.File(out_file, 'a') as f:
        f.attrs['next_id'] = int(seg.max()) + 1

        ds = f.create_dataset('volumes/raw', data=raw, compression='gzip')
        attrs = ds.attrs
        attrs['resolution'] = resolution

        ds = f.create_dataset('volumes/labels/fragments', data=seg.astype('uint64'),
                              compression='gzip')
        attrs = ds.attrs
        attrs['resolution'] = resolution
        attrs['offset'] = offset


# TODO support offset
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Write data into bigcat data format")
    parser.add_argument("raw_file", type=str, help="Path to the raw file (can be tiff or hdf5)")
    parser.add_argument("seg_file", type=str, help="Path to the segmentation file (can be tiff or hdf5)")
    parser.add_argument("out_file", type=str, help="Path to the output file")
    parser.add_argument("--raw_key", type=str, help="Key to the raw dataset, needs to be passed for hdf5 input",
                        default=None)
    parser.add_argument("--seg_key", type=str,
                        help="Key to the segmentation dataset, needs to be passed for hdf5 input",
                        default=None)
    parser.add_argument("--resolution", type=int, nargs=3, help="Resolution of the data",
                        default=[1, 1, 1])
    args = parser.parse_args()
    to_bigcat_format(args.raw_file, args.seg_file, args.out_file,
                     raw_key=args.raw_key, seg_key=args.seg_key,
                     resolution=args.resolution)
