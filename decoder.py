#Shun Fai Lee Lab3
#process the decode of strings from a file
def decoder(in_file, out_file, in_tree, a_msg: bool):
    line_count = 0
    in_count = 0
    out_count = 0
    for line in in_file:
        in_s = line.strip().replace(" ", "")
        temp_s = in_tree.decode(in_s)
        out_file.write(f'line {line_count + 1}: {temp_s}')
        out_file.write("\n")
        line_count += 1
        if temp_s != "{corrupted line~decoded failed}":
            in_count += len(in_s)
            out_count += len(temp_s)
    if a_msg:
        out_file.write("---------------------------------------------" + "\n")
        out_file.write(f'Total input bits: {in_count}' + "\n")
        out_file.write(f'Total output characters: {out_count}' + "\n")
    out_file.write("\n")