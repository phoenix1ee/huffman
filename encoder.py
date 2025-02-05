#Shun Fai Lee Lab3
#process the encode of strings from a file

def encoder(in_file, out_file, in_tree, a_msg: bool):
    in_count = 0
    out_count = 0
    skipped = ""
    tempskipped = ""
    for line in in_file:
        in_s = line.strip().replace(" ", "")
        output = ""
        valid = True
        for x in in_s:
            temp = in_tree.finds(x.upper(), 0, len(in_tree.codetable)-1)
            if temp >= 0:
                output = output + in_tree.encode2(temp)
            else:
                tempskipped = tempskipped + x
                valid = False
        in_count += len(in_s)
        out_count += len(output)
        if valid and len(output) > 0:
            out_file.write(output)
        elif valid and len(output) == 0:
            out_file.write("{an empty line}")
        else:
            out_file.write(output + "\n" + "The above line has unsupported character ")
            for x in tempskipped:
                out_file.write(f'[{x}] ')
            out_file.write("skipped")
        out_file.write("\n")
        skipped = skipped + tempskipped
        tempskipped = ""
    if a_msg:
        out_file.write("---------------------------------------------" + "\n")
        out_file.write(f'Total input characters in bits: {(in_count-len(skipped))*8}' + "\n")
        out_file.write(f'Total output bits: {out_count}' + "\n")
        out_file.write(f'Compression percentage: ~ {int((1-out_count/(in_count*8))*100)}%' + "\n")
    out_file.write("\n")