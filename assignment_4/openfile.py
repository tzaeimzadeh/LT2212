import os, argparse, gzip

parser = argparse.ArgumentParser(description="Convert text to features")

parser.add_argument("inputfile", type=str, help="The file name containing the text data.")

args = parser.parse_args()

folder_path = os.listdir(args.inputfile)    #get file names from the source folder                                                                                                                       
with gzip.open(os.path.join(args.inputfile, folder_path[0])) as source_file, gzip.open(os.path.join(args.inputfile, folder_path[1])) as target_file, open("UN-french.txt", "w") as f1, open("UN-english.\
txt", "w") as f2:
    f1.write(source_file.read().decode('utf-8'))
    f2.write(target_file.read().decode('utf-8'))
