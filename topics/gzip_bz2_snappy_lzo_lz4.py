## Reference 
https://www.cloudera.com/documentation/enterprise/5-6-x/topics/admin_data_compression_performance.html

## Choosing a Data Compression Format

## General Guidelines
1) Balance:
   The processing capacity required to compress and uncompress the data;
   The disk IO required to read and write the data; 
   The network bandwidth required to send the data across the network.
   The correct balance of these facotrs depends upon the characteristics of cluster and data,
   as well as the usage patterns.
2) Compression is NOT recommended if your data is already compressed, such as images in JPEG format.
   In fact, the resulting file can actually be larger than the original.
3) BZ2 and GZip compression uses more CPU resources than Snappy or LZO,LZ4, but provides a higher 
   compression ratio. 
   GZip/BZ2 is often a good choice for cold data, which is accessed infrequently.
   Snappy or LZO are a better choice for hot data, which is accessed frequently.
4) BZip2 can also produce MORE compression than GZip for some types of files, 
   at the cost of some speed when compressing and decompressing.
   HBase does NOT support BZip2 compression.
5) Snappy often performs better than LZO. It is worth running tests to see if you detect a significant difference.

6) For MapReduce, if you need your compressed data to be splittable, BZip2 and LZO formats can be split.
   Snappy and GZip blocks are not splittable, but files with Snappy blocks inside a container file format
   such as SequenceFile or Avro can be split.
   Snappy is intended to be used with a container format, like SequenceFiles or Avro data files, 
   rather than being used directly on plain text, for example, since the latter is not splittable and cannot be processed
   in parallel using MapReduce. 
   Splittability is NOT relevant to HBase data.
7) For MapReduce, you can compress either the intermediate data, the output, or both.
   Adjust the parameters you provide for the MapReduce job accordingly. 
   

   



