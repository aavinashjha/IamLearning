Files live in hierarchical namespace of filename

File
- Named collection of data in a file system
- File data: Text, binary, linearized/serialized objects
- File metadata: information about the file
  > Size, modification time, owner, security info
  > Basis for access control
- Operate on streams - sequence of bytes, whether text or data
  with a position
- r+: open for reading and writing
- w+: same but truncates
- char oriented: fputc, fputs, fgetc, fgets
- block oriented: fread, fwrite
- formatted: fprintf, fscanf

Directory
- Folder containing files and directories
- Hierarchical (graphical) naming
  > Path through the directory graph
  > Uniquely identifies a file or directory
  > Links and volumes
  
