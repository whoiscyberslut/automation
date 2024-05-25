# Example: there are files generated, where the filename contains within itself an integer, but also has a prefix like so:
# e.g. snapshot_data_vss_10000.caffemodel, snapshot_data_vss_iter_1000.caffemodel, snapshot_data_vss_iter_500.caffemodel and so on. 
# Use case: pad the integers with leading zeros

# Solution 1: Using formatted strings
filenames = ['snapshot_data_vss_10000.caffemodel', 'snapshot_data_vss_iter_1000.caffemodel', 'snapshot_data_vss_iter_500.caffemodel']

iters = 500
for file in filenames:
    print(f'snapshot_data_vss_iter_{iters:03}.caffemodel')
    iters += 500

