import sys

def retrieve_file(input_file, offset, size, output_file):
    f = open(input_file, 'r')

    adjustment = 0
    corrected_offset = offset + adjustment

    f.seek(corrected_offset,0)

    content = f.read(size)
    fw = open(output_file, 'w')
    fw.write(content)
    fw.close()


if len(sys.argv) < 2:
    print 'Not enough arguments! Use format: %s <blob_file>' % (sys.argv[0])
    sys.exit()

file_name = sys.argv[1]

retrieve_file(file_name, 52943601, 485, 'ivan.json')
retrieve_file(file_name, 68, 31788704, 'sqoop_manual.pdf')
retrieve_file(file_name, 41480863, 6805556, 's3_manual.pdf')

retrieve_file(file_name, 52944106, 10026035, 'aurora.pdf')
retrieve_file(file_name, 31788794, 9692048, 'dynamodb.pdf')
retrieve_file(file_name, 48286440, 4657140, 'elasticache_redis.pdf')

