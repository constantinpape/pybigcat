# Pybigcat

Python scripts to write files in [bigcat data format](https://github.com/saalfeldlab/bigcat).

## Usage

The script `to_bigcat_format.py` transforms input raw data and segmentations (in tiff or hdf5 format) into
the bigcat data format. For tiff inputs, use it like this:
```
python to_bigcat_format.py </path/to/raw.tif> </path/to/seg.tif> </path/to/output.h5>
```

For hdf5 inputs, use it like this
```
python to_bigcat_format.py </path/to/raw.tif> </path/to/seg.tif> </path/to/output.h5> --raw_key <raw_dataset_name> --seg_key <seg_dataset_name>
```

TODO `to_bigcat_format_with_assignments` for the case where we already have a fragment segment lut.

## Dependencies

You need `h5py` and `imageio` in order to use the scripts.
