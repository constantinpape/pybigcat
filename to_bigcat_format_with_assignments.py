# TODO


# This is the expected format for the fragment segment id look-up
# node_ids = np.arange(len(assignments), dtype='uint64')
# lut = np.zeros((2, len(assignments)), dtype='uint64')
# lut[0, :] = node_ids
# max_node_id = len(assignments)
# lut[1, :] = assignments + max_node_id
#
# with h5py.File(self.output_path) as f:
#     ds = f.require_dataset('fragment_segment_lut', shape=lut.shape,
#                            compression='gzip', maxshape=(2, None),
#                            dtype='uint64')
#     ds[:] = lut
