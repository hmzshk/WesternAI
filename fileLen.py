def file_len(fname):
  with open(fname) as f:
    for i, l in enumerate(f):
      pass
  return i + 1

num_classes = file_len(r'C:\Users\hmzsh\Pictures\Train_dir/classes.names')
print("Number of Classes: ",num_classes)
